"""
Sistema de Classificação Inteligente de E-mails
Backend Flask com integração de IA para classificação e geração de respostas
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import PyPDF2
import io
import os
from datetime import datetime
import anthropic

app = Flask(__name__)
CORS(app)

# Configuração da API Claude
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None

# Prompt de sistema otimizado para classificação de e-mails
SYSTEM_PROMPT = """Você é um assistente especializado em classificação de e-mails corporativos do setor financeiro.

Sua tarefa é analisar e-mails e classificá-los em duas categorias:

1. **PRODUTIVO**: E-mails que requerem ação ou resposta específica:
   - Solicitações de suporte técnico
   - Pedidos de atualização sobre casos/requisições
   - Dúvidas sobre sistemas ou processos
   - Questões financeiras ou operacionais
   - Solicitações de documentos ou informações
   - Problemas que precisam ser resolvidos
   - Perguntas que requerem resposta específica

2. **IMPRODUTIVO**: E-mails que não requerem ação imediata:
   - Mensagens de felicitações (aniversário, Natal, etc.)
   - Agradecimentos genéricos
   - Comunicados informativos sem necessidade de resposta
   - Mensagens sociais ou de cortesia
   - Newsletters ou boletins informativos

Para cada e-mail, retorne APENAS um JSON no seguinte formato (sem formatação markdown):
{
  "categoria": "PRODUTIVO" ou "IMPRODUTIVO",
  "confianca": 0.0 a 1.0,
  "motivo": "breve explicação da classificação",
  "resposta_sugerida": "sugestão de resposta profissional e apropriada",
  "acoes_sugeridas": ["lista de ações recomendadas"]
}

A resposta sugerida deve ser:
- Profissional e cordial
- Adequada ao contexto do setor financeiro
- Específica ao conteúdo do e-mail
- Em português brasileiro
- Para e-mails PRODUTIVOS: resposta que aborda a solicitação
- Para e-mails IMPRODUTIVOS: resposta breve e educada"""


def extrair_texto_pdf(arquivo):
    """Extrai texto de arquivo PDF"""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(arquivo.read()))
        texto = ""
        for pagina in pdf_reader.pages:
            texto += pagina.extract_text() + "\n"
        return texto.strip()
    except Exception as e:
        raise Exception(f"Erro ao processar PDF: {str(e)}")


def preprocessar_texto(texto):
    """Pré-processa texto do e-mail"""
    # Remove múltiplos espaços em branco
    texto = re.sub(r'\s+', ' ', texto)
    
    # Remove URLs
    texto = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', texto)
    
    # Remove e-mails
    texto = re.sub(r'\S+@\S+', '', texto)
    
    # Normaliza quebras de linha
    texto = re.sub(r'\n+', '\n', texto)
    
    return texto.strip()


def classificar_email_ia(texto_email):
    """Classifica e-mail usando Claude AI"""
    if not client:
        # Fallback: classificação baseada em regras simples
        return classificar_email_regras(texto_email)
    
    try:
        # Preprocessa o texto
        texto_processado = preprocessar_texto(texto_email)
        
        # Limita tamanho do texto para evitar custos excessivos
        if len(texto_processado) > 3000:
            texto_processado = texto_processado[:3000] + "..."
        
        # Chama a API Claude
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system=SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"Classifique o seguinte e-mail:\n\n{texto_processado}"
                }
            ]
        )
        
        # Extrai resposta
        resposta_texto = message.content[0].text
        
        # Remove markdown code blocks se existirem
        resposta_texto = re.sub(r'```json\s*', '', resposta_texto)
        resposta_texto = re.sub(r'```\s*', '', resposta_texto)
        
        # Parse JSON
        import json
        resultado = json.loads(resposta_texto.strip())
        
        return {
            'categoria': resultado.get('categoria', 'PRODUTIVO'),
            'confianca': resultado.get('confianca', 0.8),
            'motivo': resultado.get('motivo', 'Análise por IA'),
            'resposta_sugerida': resultado.get('resposta_sugerida', ''),
            'acoes_sugeridas': resultado.get('acoes_sugeridas', []),
            'metodo': 'ia'
        }
        
    except Exception as e:
        print(f"Erro na classificação por IA: {str(e)}")
        # Fallback para classificação por regras
        return classificar_email_regras(texto_email)


def classificar_email_regras(texto_email):
    """Classificação por regras (fallback)"""
    texto_lower = texto_email.lower()
    
    # Palavras-chave para e-mails improdutivos
    palavras_improdutivas = [
        'feliz natal', 'feliz ano novo', 'parabéns', 'aniversário',
        'agradec', 'obrigad', 'felicitações', 'bom dia', 'boa tarde',
        'boa noite', 'feliz páscoa', 'felicidades'
    ]
    
    # Palavras-chave para e-mails produtivos
    palavras_produtivas = [
        'solicit', 'precis', 'urgente', 'problema', 'erro', 'dúvida',
        'questão', 'status', 'atualização', 'informação', 'document',
        'quando', 'como', 'por que', 'prazo', 'pendente', 'ajuda',
        'suporte', 'sistema', 'acesso', 'senha', 'não consigo'
    ]
    
    score_improdutivo = sum(1 for palavra in palavras_improdutivas if palavra in texto_lower)
    score_produtivo = sum(1 for palavra in palavras_produtivas if palavra in texto_lower)
    
    # Classifica baseado nos scores
    if score_improdutivo > score_produtivo:
        categoria = 'IMPRODUTIVO'
        resposta = "Obrigado pela mensagem! Retornaremos em breve se necessário."
        acoes = ["Arquivar", "Marcar como lido"]
        confianca = min(0.7, 0.5 + (score_improdutivo - score_produtivo) * 0.1)
    else:
        categoria = 'PRODUTIVO'
        resposta = "Prezado(a),\n\nRecebemos sua solicitação e estamos analisando. Retornaremos com uma resposta em breve.\n\nAtenciosamente,\nEquipe de Suporte"
        acoes = ["Atribuir a um atendente", "Priorizar para resposta", "Abrir ticket"]
        confianca = min(0.7, 0.5 + (score_produtivo - score_improdutivo) * 0.1)
    
    return {
        'categoria': categoria,
        'confianca': confianca,
        'motivo': f'Classificação por regras (score: prod={score_produtivo}, improd={score_improdutivo})',
        'resposta_sugerida': resposta,
        'acoes_sugeridas': acoes,
        'metodo': 'regras'
    }


@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de health check"""
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'ia_disponivel': client is not None
    })


@app.route('/classificar', methods=['POST'])
def classificar_email():
    """Endpoint principal para classificação de e-mails"""
    try:
        texto_email = None
        
        # Verifica se é upload de arquivo
        if 'arquivo' in request.files:
            arquivo = request.files['arquivo']
            
            if arquivo.filename == '':
                return jsonify({'erro': 'Nenhum arquivo selecionado'}), 400
            
            # Processa baseado no tipo de arquivo
            if arquivo.filename.endswith('.pdf'):
                texto_email = extrair_texto_pdf(arquivo)
            elif arquivo.filename.endswith('.txt'):
                texto_email = arquivo.read().decode('utf-8')
            else:
                return jsonify({'erro': 'Formato de arquivo não suportado. Use .txt ou .pdf'}), 400
        
        # Verifica se é texto direto
        elif request.is_json and 'texto' in request.json:
            texto_email = request.json['texto']
        
        else:
            return jsonify({'erro': 'Nenhum conteúdo fornecido'}), 400
        
        # Valida conteúdo
        if not texto_email or len(texto_email.strip()) < 10:
            return jsonify({'erro': 'Conteúdo do e-mail muito curto ou vazio'}), 400
        
        # Classifica o e-mail
        resultado = classificar_email_ia(texto_email)
        
        # Adiciona metadados
        resultado['timestamp'] = datetime.now().isoformat()
        resultado['tamanho_texto'] = len(texto_email)
        resultado['preview'] = texto_email[:200] + '...' if len(texto_email) > 200 else texto_email
        
        return jsonify(resultado), 200
        
    except Exception as e:
        return jsonify({
            'erro': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500


@app.route('/estatisticas', methods=['GET'])
def obter_estatisticas():
    """Endpoint para estatísticas do sistema"""
    return jsonify({
        'versao': '1.0.0',
        'categorias': ['PRODUTIVO', 'IMPRODUTIVO'],
        'formatos_suportados': ['.txt', '.pdf'],
        'ia_disponivel': client is not None,
        'metodos_classificacao': ['ia', 'regras']
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)

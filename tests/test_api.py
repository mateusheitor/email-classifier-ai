"""
Testes automatizados para o sistema de classificação de e-mails
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
from backend.app import app


class TestEmailClassifier(unittest.TestCase):
    """Testes para o classificador de e-mails"""
    
    def setUp(self):
        """Configuração antes de cada teste"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_health_check(self):
        """Testa endpoint de health check"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'ok')
        self.assertIn('timestamp', data)
    
    def test_estatisticas(self):
        """Testa endpoint de estatísticas"""
        response = self.app.get('/estatisticas')
        self.assertEqual(response.status_code, 200)
        
        data = json.loads(response.data)
        self.assertIn('PRODUTIVO', data['categorias'])
        self.assertIn('IMPRODUTIVO', data['categorias'])
    
    def test_classificar_email_produtivo(self):
        """Testa classificação de e-mail produtivo"""
        email_text = """
        De: João Silva
        Para: Suporte
        Assunto: Problema urgente no sistema
        
        Olá, estou com um problema crítico no sistema.
        Não consigo acessar e preciso dos relatórios urgentemente.
        Podem me ajudar?
        """
        
        response = self.app.post('/classificar',
            data=json.dumps({'texto': email_text}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Verifica estrutura da resposta
        self.assertIn('categoria', data)
        self.assertIn('confianca', data)
        self.assertIn('resposta_sugerida', data)
        
        # Verifica se foi classificado como produtivo
        self.assertEqual(data['categoria'], 'PRODUTIVO')
    
    def test_classificar_email_improdutivo(self):
        """Testa classificação de e-mail improdutivo"""
        email_text = """
        Olá equipe!
        
        Feliz Natal a todos!
        Desejo um ano novo cheio de realizações.
        
        Abraços,
        Maria
        """
        
        response = self.app.post('/classificar',
            data=json.dumps({'texto': email_text}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Verifica se foi classificado como improdutivo
        self.assertEqual(data['categoria'], 'IMPRODUTIVO')
    
    def test_classificar_email_vazio(self):
        """Testa erro com e-mail vazio"""
        response = self.app.post('/classificar',
            data=json.dumps({'texto': ''}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('erro', data)
    
    def test_classificar_sem_conteudo(self):
        """Testa erro sem conteúdo"""
        response = self.app.post('/classificar',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)


class TestTextProcessing(unittest.TestCase):
    """Testes para processamento de texto"""
    
    def setUp(self):
        from backend.app import preprocessar_texto
        self.preprocessar = preprocessar_texto
    
    def test_preprocessar_espacos(self):
        """Testa remoção de espaços múltiplos"""
        texto = "Olá    mundo    teste"
        resultado = self.preprocessar(texto)
        self.assertNotIn('    ', resultado)
    
    def test_preprocessar_urls(self):
        """Testa remoção de URLs"""
        texto = "Veja em https://example.com/page mais detalhes"
        resultado = self.preprocessar(texto)
        self.assertNotIn('https://', resultado)
    
    def test_preprocessar_emails(self):
        """Testa remoção de endereços de e-mail"""
        texto = "Contato: joao@empresa.com.br para mais info"
        resultado = self.preprocessar(texto)
        self.assertNotIn('@', resultado)


if __name__ == '__main__':
    # Executa os testes
    unittest.main(verbosity=2)

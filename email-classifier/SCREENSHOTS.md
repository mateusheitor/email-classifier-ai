# 📸 Screenshots e Demonstrações

## Interface Principal

### 1. Tela Inicial - Upload de Arquivo
```
┌─────────────────────────────────────────────────────────────┐
│  🤖 Classificador Inteligente de E-mails                    │
│  Solução com IA para automatizar análise de e-mails         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [📁 Upload de Arquivo]  [✍️ Digitar E-mail]                │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                      📎                              │   │
│  │   Arraste um arquivo ou clique para selecionar      │   │
│  │                                                      │   │
│  │         Formatos aceitos: .txt, .pdf                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  [🚀 Classificar E-mail]                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2. Tela de Entrada de Texto
```
┌─────────────────────────────────────────────────────────────┐
│  [📁 Upload de Arquivo]  [✍️ Digitar E-mail]                │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Cole ou digite o conteúdo do e-mail aqui...         │   │
│  │                                                      │   │
│  │ De: João Silva                                      │   │
│  │ Para: Suporte Técnico                               │   │
│  │ Assunto: Sistema não está abrindo                   │   │
│  │                                                      │   │
│  │ Olá, estou com problema para acessar...            │   │
│  │                                                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                              │
│  [🚀 Classificar E-mail]                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3. Tela de Loading
```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│                      ⭕ [Spinner]                           │
│                                                              │
│        Analisando e-mail com Inteligência Artificial...     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4. Resultado - E-mail Produtivo
```
┌─────────────────────────────────────────────────────────────┐
│  Resultado da Classificação              [PRODUTIVO]        │
│  Método: 🤖 IA Generativa                                   │
│  ────────────────────────────────────────────────────────   │
│                                                              │
│  📊 Confiança da Análise                                    │
│  ████████████████████░░ 95%                                 │
│  95.0% de confiança                                         │
│                                                              │
│  💡 Motivo da Classificação                                 │
│  E-mail contém solicitação de suporte técnico urgente       │
│  com problema de acesso ao sistema                          │
│                                                              │
│  ✉️ Resposta Sugerida                                       │
│  ┌────────────────────────────────────────────────────┐    │
│  │ Prezado João,                                       │    │
│  │                                                     │    │
│  │ Recebemos seu relato sobre o erro de acesso ao    │    │
│  │ sistema. Nossa equipe técnica já foi notificada   │    │
│  │ e está trabalhando para resolver o problema.      │    │
│  │                                                     │    │
│  │ Enquanto isso, você pode tentar:                  │    │
│  │ 1. Limpar o cache do navegador                    │    │
│  │ 2. Tentar em modo anônimo                         │    │
│  │                                                     │    │
│  │ Retornaremos em breve com uma solução.           │    │
│  │                                                     │    │
│  │ Atenciosamente,                                    │    │
│  │ Equipe de Suporte Técnico                         │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ⚡ Ações Recomendadas                                      │
│  [✓ Atribuir a técnico de plantão]                         │
│  [✓ Priorizar como urgente]                                │
│  [✓ Abrir ticket #12345]                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 5. Resultado - E-mail Improdutivo
```
┌─────────────────────────────────────────────────────────────┐
│  Resultado da Classificação            [IMPRODUTIVO]        │
│  Método: 🤖 IA Generativa                                   │
│  ────────────────────────────────────────────────────────   │
│                                                              │
│  📊 Confiança da Análise                                    │
│  ██████████████████░░░░ 92%                                 │
│  92.0% de confiança                                         │
│                                                              │
│  💡 Motivo da Classificação                                 │
│  Mensagem de felicitações sem necessidade de ação           │
│  ou resposta específica                                     │
│                                                              │
│  ✉️ Resposta Sugerida                                       │
│  ┌────────────────────────────────────────────────────┐    │
│  │ Olá Maria,                                          │    │
│  │                                                     │    │
│  │ Muito obrigado pelas felicitações! Desejamos      │    │
│  │ a você também um excelente Natal e um Ano Novo    │    │
│  │ repleto de realizações.                            │    │
│  │                                                     │    │
│  │ Conte sempre conosco!                              │    │
│  │                                                     │    │
│  │ Abraços,                                           │    │
│  │ Equipe                                             │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ⚡ Ações Recomendadas                                      │
│  [✓ Arquivar]                                              │
│  [✓ Marcar como lido]                                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Fluxo de Uso

### Cenário 1: Upload de PDF
```
1. Usuário seleciona arquivo PDF
   ↓
2. Sistema extrai texto do PDF
   ↓
3. Envia para API de classificação
   ↓
4. IA analisa o conteúdo
   ↓
5. Retorna classificação + resposta
   ↓
6. Exibe resultados com formatação
```

### Cenário 2: Texto Direto
```
1. Usuário cola texto do e-mail
   ↓
2. Clica em "Classificar"
   ↓
3. Sistema valida entrada
   ↓
4. IA processa e classifica
   ↓
5. Gera resposta contextual
   ↓
6. Mostra resultado completo
```

## Cores e Design

### Paleta de Cores
```
Primary:      #2563eb (Azul vibrante)
Secondary:    #10b981 (Verde sucesso)
Danger:       #ef4444 (Vermelho erro)
Background:   Gradiente Roxo (#667eea → #764ba2)
Cards:        #ffffff (Branco)
Text:         #1e293b (Cinza escuro)
```

### Animações
```
✓ Fade in ao carregar
✓ Slide up nos resultados
✓ Spinner durante processamento
✓ Hover effects nos botões
✓ Drag & drop visual feedback
```

## Responsividade

### Desktop (>768px)
```
┌────────────────────────────────────────┐
│  [Full Width Container]                │
│  ┌──────────────────────────────────┐ │
│  │  Card com tabs lado a lado       │ │
│  │  Botões em linha                 │ │
│  └──────────────────────────────────┘ │
└────────────────────────────────────────┘
```

### Mobile (<768px)
```
┌──────────────┐
│  [Container] │
│  ┌─────────┐ │
│  │ Tabs    │ │
│  │ Stack   │ │
│  └─────────┘ │
│  ┌─────────┐ │
│  │ Botões  │ │
│  │ Full W  │ │
│  └─────────┘ │
└──────────────┘
```

## Exemplos de Interação

### 1. Drag & Drop
```
Estado Normal:
┌────────────────┐
│     📎         │
│  Arraste aqui  │
└────────────────┘

Estado Hover:
┌════════════════┐  ← Border azul
║     📎         ║  ← Background claro
║  Solte aqui!   ║
└════════════════┘
```

### 2. Barra de Confiança
```
0%                    50%                   100%
├──────────────────────┼──────────────────────┤
████████████████░░░░░░░                  80%
└─ Gradiente verde → azul ─┘
```

### 3. Badges de Categoria
```
[PRODUTIVO]          [IMPRODUTIVO]
Verde escuro         Amarelo escuro
Background verde     Background amarelo
```

## Mensagens de Erro

### Erro de Validação
```
┌─────────────────────────────────────────┐
│ ❌ Erro: Conteúdo muito curto           │
│                                         │
│ Por favor, digite um e-mail com pelo   │
│ menos 10 caracteres.                   │
└─────────────────────────────────────────┘
```

### Erro de Conexão
```
┌─────────────────────────────────────────┐
│ ❌ Erro: Não foi possível conectar     │
│                                         │
│ Verifique se o backend está rodando    │
│ corretamente e tente novamente.        │
└─────────────────────────────────────────┘
```

## Performance

### Métricas
```
⏱️  Tempo de resposta: < 2 segundos
📊  Precisão (IA):     ~95%
📊  Precisão (Regras): ~70%
💾  Tamanho página:    ~50 KB
🚀  First Paint:       < 1 segundo
```

---

**Nota:** Esta é uma representação em texto ASCII. A interface real é muito mais bonita com:
- Gradientes suaves
- Sombras elegantes
- Animações fluidas
- Ícones modernos
- Typography profissional

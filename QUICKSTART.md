# ⚡ Guia Rápido de Instalação

## 🚀 Setup em 5 Minutos

### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/seu-usuario/email-classifier.git
cd email-classifier
```

### 2️⃣ Instale as Dependências
```bash
cd backend
pip install -r requirements.txt
```

### 3️⃣ Configure a API Key
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite .env e adicione sua chave:
# ANTHROPIC_API_KEY=sk-ant-api03-xxx
```

**Obtenha sua chave API gratuitamente:**
- Acesse: https://console.anthropic.com/
- Crie uma conta
- Gere uma API key
- Cole no arquivo `.env`

### 4️⃣ Execute o Backend
```bash
python app.py
```

✅ Backend rodando em: `http://localhost:5000`

### 5️⃣ Abra o Frontend
```bash
# Em outro terminal
cd ../frontend
python -m http.server 8000
```

✅ Acesse: `http://localhost:8000`

---

## 🧪 Teste Rápido

### Via Interface Web
1. Abra `http://localhost:8000`
2. Cole este texto:
```
Olá, preciso de ajuda urgente com o sistema!
Não consigo acessar minha conta.
```
3. Clique em "Classificar"

### Via cURL
```bash
curl -X POST http://localhost:5000/classificar \
  -H "Content-Type: application/json" \
  -d '{"texto":"Preciso de ajuda com o sistema!"}'
```

---

## 🎯 Arquivos de Exemplo

Teste com os e-mails de exemplo em `data/examples/`:
- `email_produtivo_1.txt` - Solicitação de suporte
- `email_produtivo_2.txt` - Pedido de atualização
- `email_improdutivo_1.txt` - Felicitações
- `email_improdutivo_2.txt` - Agradecimento

---

## ⚠️ Problemas Comuns

### Erro: "Module not found"
```bash
pip install -r requirements.txt
```

### Erro: "ANTHROPIC_API_KEY not found"
- Verifique se o arquivo `.env` existe
- Confirme que a chave está correta
- Reinicie o servidor Flask

### Erro de CORS
- Verifique se o backend está rodando
- Confirme a URL no `frontend/index.html`

---

## 📚 Próximos Passos

1. ✅ Teste todos os exemplos
2. 📝 Leia o README completo
3. ☁️ Faça deploy na nuvem (veja README)
4. 🎨 Customize para suas necessidades

---

**Precisa de ajuda?** Abra uma issue no GitHub!

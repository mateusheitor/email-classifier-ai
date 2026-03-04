# ☁️ Guia de Deploy em Produção

Este guia mostra como fazer deploy completo da aplicação na nuvem gratuitamente.

## 🎯 Opções de Deploy

### Backend
- ✅ **Render** (Recomendado - 750h grátis/mês)
- Heroku (Plano pago)
- Railway (Créditos grátis)
- Google Cloud Run

### Frontend
- ✅ **Netlify** (Recomendado - Grátis)
- Vercel (Grátis)
- GitHub Pages (Grátis)

---

## 🚀 Deploy do Backend no Render

### Passo 1: Preparar o Projeto

1. Faça commit de todas as alterações:
```bash
git add .
git commit -m "Preparando para deploy"
git push origin main
```

### Passo 2: Criar Conta no Render

1. Acesse: https://render.com
2. Crie uma conta (pode usar GitHub)
3. Confirme seu e-mail

### Passo 3: Criar Web Service

1. Click em "New +" → "Web Service"
2. Conecte seu repositório GitHub
3. Configure:

**Build & Deploy:**
```
Name: email-classifier-api
Region: Oregon (US West)
Branch: main
Root Directory: backend
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

**Instance Type:**
```
Free (750h/mês grátis)
```

### Passo 4: Configurar Variáveis de Ambiente

Na seção "Environment Variables", adicione:

```
ANTHROPIC_API_KEY = sk-ant-api03-xxxxx
DEBUG = False
PORT = 10000
```

### Passo 5: Deploy

1. Clique em "Create Web Service"
2. Aguarde o deploy (3-5 minutos)
3. Copie a URL gerada (ex: `https://email-classifier-api.onrender.com`)

### Passo 6: Testar

```bash
curl https://email-classifier-api.onrender.com/health
```

---

## 🌐 Deploy do Frontend no Netlify

### Método 1: Netlify Drop (Mais Fácil)

1. Acesse: https://app.netlify.com/drop
2. **Antes de arrastar**, edite `frontend/index.html`:

```javascript
// Linha ~565
const API_URL = 'https://email-classifier-api.onrender.com'; // Sua URL do Render
```

3. Arraste a pasta `frontend` para o Netlify
4. Aguarde o deploy
5. Copie a URL gerada (ex: `https://amazing-app-123.netlify.app`)

### Método 2: Netlify CLI

```bash
# Instale Netlify CLI
npm install -g netlify-cli

# Faça login
netlify login

# Deploy
cd frontend
netlify deploy --prod
```

### Método 3: GitHub + Netlify (Continuous Deployment)

1. No Netlify, clique "New site from Git"
2. Conecte seu repositório
3. Configure:
```
Build command: (deixe vazio)
Publish directory: frontend
```
4. Deploy!

---

## 🔧 Configurações Adicionais

### Custom Domain (Opcional)

**No Render:**
1. Settings → Custom Domains
2. Adicione seu domínio
3. Configure DNS conforme instruções

**No Netlify:**
1. Domain Settings → Add custom domain
2. Configure DNS conforme instruções

### SSL/HTTPS

✅ Automático em Render e Netlify!

### Environment Variables (Frontend)

Se precisar de variáveis no frontend:

**Netlify:**
1. Site Settings → Environment Variables
2. Adicione variáveis
3. Redeploy

---

## 📊 Monitoramento

### Render

- Logs em tempo real: Dashboard → Logs
- Métricas: Dashboard → Metrics
- Health checks automáticos

### Netlify

- Deploy logs: Deploys → Deploy log
- Analytics: Analytics (plano pago)
- Forms: Forms (se usar)

---

## 🔐 Segurança em Produção

### 1. Rate Limiting

Adicione ao `backend/app.py`:

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100 per hour"]
)

@app.route('/classificar', methods=['POST'])
@limiter.limit("30 per minute")
def classificar_email():
    # ...
```

Adicione ao `requirements.txt`:
```
Flask-Limiter==3.5.0
```

### 2. CORS Específico

Em produção, configure CORS apenas para seu domínio:

```python
CORS(app, resources={
    r"/*": {
        "origins": ["https://seu-dominio.netlify.app"]
    }
})
```

### 3. API Key Rotation

- Troque a API key regularmente
- Use secrets manager em produção avançada
- Monitore uso no console.anthropic.com

### 4. HTTPS Only

```python
@app.before_request
def before_request():
    if not request.is_secure and not app.debug:
        return redirect(request.url.replace('http://', 'https://'))
```

---

## 💰 Custos Estimados

### Setup Gratuito

| Serviço | Plano | Custo |
|---------|-------|-------|
| Render | Free Tier | $0/mês (750h) |
| Netlify | Free | $0/mês |
| Anthropic API | Pay-as-you-go | ~$0.50-$5/mês* |

*Baseado em ~1000 classificações/mês

### Setup Escalável

| Serviço | Plano | Custo |
|---------|-------|-------|
| Render | Starter | $7/mês |
| Netlify | Pro | $19/mês |
| Anthropic API | Pay-as-you-go | Variável |

---

## 🐛 Troubleshooting

### Backend não responde

```bash
# Verifique logs no Render
# Dashboard → Logs

# Teste health check
curl https://sua-api.onrender.com/health
```

### CORS Error

- Verifique se a URL do backend está correta no frontend
- Confirme configuração CORS no backend
- Use DevTools → Network para debug

### API Key inválida

- Verifique no Render → Environment Variables
- Regenere a key no console.anthropic.com
- Redeploy após alterar variáveis

### Deploy falhou

**Render:**
- Verifique Build logs
- Confirme `requirements.txt` está correto
- Teste localmente primeiro

**Netlify:**
- Verifique se todos os arquivos foram enviados
- Confirme estrutura de pastas

---

## 📈 Escalabilidade

### Aumentar Performance

1. **Caching**:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
```

2. **Database** (para logs):
```python
# Use PostgreSQL no Render
# Adicione SQLAlchemy
```

3. **CDN**:
- Netlify já usa CDN global
- Para arquivos estáticos maiores, use Cloudflare

### Limites Grátis

**Render Free Tier:**
- 750h/mês (31 dias = 744h)
- Sleep após 15min inatividade
- 512 MB RAM
- 0.1 CPU

**Solução**: Uso Starter ($7/mês) para produção séria

---

## ✅ Checklist de Deploy

Antes de ir para produção:

- [ ] Testes locais passando
- [ ] API Key configurada
- [ ] CORS configurado corretamente
- [ ] Frontend aponta para backend correto
- [ ] SSL/HTTPS funcionando
- [ ] Logs monitorados
- [ ] Rate limiting configurado
- [ ] Backups configurados (se usar DB)
- [ ] Documentação atualizada
- [ ] Usuários de teste validaram

---

## 🆘 Suporte

**Render:**
- Docs: https://render.com/docs
- Community: https://community.render.com

**Netlify:**
- Docs: https://docs.netlify.com
- Community: https://answers.netlify.com

**Anthropic:**
- Docs: https://docs.anthropic.com
- Support: https://support.anthropic.com

---

**🎉 Parabéns!** Sua aplicação está agora em produção e acessível globalmente!

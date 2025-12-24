# Gerenciador-Pro

Plataforma de orquestração conversacional baseada em agentes, projetada para gerenciar conversas comerciais de forma inteligente, contextual e orientada a resultado, rodando de forma independente em uma VPS via Docker. Não é sistema de disparo em massa e não é um bot que fala sem critério.

## O que é o sistema

Um conjunto de agentes especializados coordenados por um motor de decisão que analisa contexto, histórico e intenção antes de qualquer interação. O valor está na decisão, não no envio.

## Intuito do sistema

Transformar contatos em conversas reais e conversas em ações úteis:

- Qualificar leads
- Conduzir vendas consultivas
- Agendar reuniões
- Encerrar interações no momento certo
- Transferir para um humano quando necessário

Tudo isso sem insistência, sem spam e sem comportamento artificial.

## O problema que ele resolve

A maioria das automações falha porque:

- Dispara mensagens sem contexto
- Insiste sem resposta
- Trata todo contato igual
- Prioriza volume em vez de decisão

Este sistema resolve isso ao:

- Decidir quando falar e quando ficar em silêncio
- Escolher qual agente deve atuar
- Respeitar limites claros de interação
- Encerrar conversas de forma definitiva quando necessário

## Como funciona (em essência)

1. Um evento entra no sistema (mensagem recebida, novo contato, gatilho manual).
2. O motor de decisão analisa o estado da conversa.
3. O sistema escolhe se deve agir ou não.
4. Um agente especializado é acionado.
5. O agente executa um objetivo específico.
6. O sistema registra o resultado e atualiza o estado.
7. A conversa segue ou é encerrada.

O sistema não busca conversar mais, busca conversar melhor.

## O que o sistema NÃO faz

- Não dispara mensagens em massa sem critério.
- Não insiste após rejeição.
- Não tenta simular comportamento humano artificial.
- Não reabre conversas encerradas automaticamente.
- Não promete evitar bloqueios de plataforma.

Essas limitações são parte do design, não falhas.

## Para quem o sistema foi pensado

- Produtores e infoprodutores
- Agências e SDRs
- Times pequenos de vendas
- Consultores e prestadores de serviço
- Pessoas que querem automação com controle e responsabilidade

Não é para quem busca atalhos ou volume sem contexto.

## Valor central do produto

Menos mensagens, mais contexto, mais resultado, menos risco.

**Resumo em uma frase:** um sistema de agentes inteligentes que sabem quando falar, o que falar e quando parar — focado em conversão, não em disparo.

## Como subir

```bash
docker compose up -d
```

## Rodar local sem banco/Redis

Para desenvolvimento local sem banco/Redis, basta subir a API com FastAPI + Uvicorn:

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn
uvicorn backend.main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000` e o health check em
`http://127.0.0.1:8000/health`.

## Rodar em VPS (ex.: EasyPanel com serviço App)

1. Crie um serviço do tipo **App** apontando para este repositório.
2. Configure o start command:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

3. Exponha a porta **8000** no painel.
4. (Opcional) Defina variáveis de ambiente copiando `.env.example`.

Se você já roda Postgres/Redis fora do app, mantenha-os externos e a API sobe
apenas com o Uvicorn.

## Dockerfile (build direto)

Se preferir gerar a imagem direto, use o `Dockerfile` na raiz:

```bash
docker build -t gerenciador-pro .
docker run --rm -p 8000:8000 gerenciador-pro
```

Você também pode usar o Dockerfile específico da API:

```bash
docker build -f docker/api.Dockerfile -t gerenciador-pro-api .
docker run --rm -p 8000:8000 gerenciador-pro-api
```

## Estrutura

```
whats-agent-stack/
├── docker/
│   ├── api.Dockerfile
│   ├── agent.Dockerfile
│   └── frontend.Dockerfile
├── docker-compose.yml
├── .env.example
├── backend/
│   ├── api/
│   ├── agents/
│   ├── core/
│   ├── tools/
│   ├── services/
│   ├── domain/
│   ├── infra/
│   └── main.py
├── frontend/
└── scripts/
```

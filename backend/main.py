from fastapi import FastAPI

from backend.api.routes import agents, campaigns, contacts, conversations, settings

app = FastAPI(title="Gerenciador Pro")

app.include_router(contacts.router)
app.include_router(conversations.router)
app.include_router(agents.router)
app.include_router(campaigns.router)
app.include_router(settings.router)


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}

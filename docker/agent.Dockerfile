FROM python:3.11-slim

WORKDIR /app

COPY backend /app/backend

RUN pip install --no-cache-dir langchain

CMD ["python", "-m", "backend.agents.orchestrator_agent"]

FROM node:20-slim

WORKDIR /app

COPY frontend /app/frontend

CMD ["sleep", "infinity"]

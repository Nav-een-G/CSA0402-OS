# Task B2 – Dockerise the portal
HTML structures the page; CSS styles it; JavaScript validates input and calls the API; Flask serves the page/API; PostgreSQL stores sample data.
Run: `cp .env.example .env`, edit the password, then `docker compose up --build -d`. Browse `http://localhost:8000`; test `/health`.
Evidence: `docker images`, `docker ps`, `docker exec <container> whoami` (should print portal), `docker stats --no-stream`, `docker history result-portal:1.0`.
Compose provides PostgreSQL persistence through named volume `result_data`. `docker compose down` keeps it; `docker compose down -v` deletes it.

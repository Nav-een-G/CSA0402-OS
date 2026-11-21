# CSA04 – Operating Systems – Assignment 5 (CO5)

Student: Naveen G | Register No.: 192411019

### Included technologies
HTML/CSS/JavaScript frontend; Python Flask backend; PostgreSQL database; Bash administration scripts; Dockerfile; Docker Compose; Kubernetes YAML. **Java and C are not required by the supplied assignment brief.** The HTML frontend is an optional portal interface; the required OS work is in Bash, Docker, Compose and Kubernetes.

### Folder structure
- PartA/: add your A1–A5 design answers.
- TaskB1/: Linux scripts, systemd and Nginx templates.
- TaskB2/: complete web app, database, Dockerfile and Compose.
- TaskB3/: Kubernetes Deployment/Service and measurement sheet.
- TaskB4/: second service and capacity/production decision.

### Run the full web application
```bash
cd TaskB2
cp .env.example .env
# Edit .env and set a strong local password
docker compose up --build -d
docker compose ps
```
Open http://localhost:8000. Demo register numbers: STU1001, STU1002, STU1003, STU1004. Health check: http://localhost:8000/health.

Stop without deleting database data:
```bash
docker compose down
```
`docker compose down -v` deletes the database volume.

### Task B1
```bash
chmod +x TaskB1/*.sh
bash TaskB1/log_analysis.sh
bash TaskB1/disk_alert.sh 80
ps aux
top
free -h
vmstat 1 5
df -h
ss -tulnp
```
If installed: `iostat -xz 1 3`. Hourly cron example (replace paths):
```cron
0 * * * * /bin/bash /absolute/path/TaskB1/log_analysis.sh >> /absolute/path/log-analysis.log 2>&1
```
See TaskB1/README.md before installing systemd/Nginx templates; update paths and account names first.

### Task B2 Docker evidence
```bash
cd TaskB2
docker build -t result-portal:1.0 .
docker run -d --name portal-test -p 8000:8000 result-portal:1.0
docker ps
docker exec portal-test whoami
docker stats --no-stream portal-test
docker history result-portal:1.0
docker rm -f portal-test
```
For limits: `docker run -d --name limited --cpus=0.50 --memory=256m -p 8001:8000 result-portal:1.0`, then `docker stats --no-stream limited`.

### Task B3 Kubernetes
Build and load the image into your local cluster:
```bash
cd TaskB2
docker build -t result-portal:1.0 .
minikube image load result-portal:1.0
kubectl apply -f ../TaskB3/deployment.yaml
kubectl get pods -o wide
kubectl get services
kubectl port-forward service/result-portal 8080:80
```
For kind use `kind load docker-image result-portal:1.0 --name <cluster-name>`.
Delete one pod and watch it recover:
```bash
kubectl get pods
kubectl delete pod <pod-name>
kubectl get pods -w
kubectl scale deployment result-portal --replicas=6
kubectl get pods
```
Note: the supplied Kubernetes manifest demonstrates the required replica/resource configuration. To make the portal's search API work in Kubernetes, deploy PostgreSQL too and set `DATABASE_URL` in the portal Deployment.

### Task B4
```bash
docker compose -f TaskB4/lms-compose.yaml up -d
docker compose -f TaskB4/lms-compose.yaml ps
docker compose -f TaskB4/lms-compose.yaml down
```
Fill TaskB3/measurements.csv using your own repeated measurements. Never invent startup time, memory, image size or requests/second. Capture screenshots and command output for each task.

### GitHub
Create repository exactly `CSA04-<RegisterNumber>-Assignment5`. Commit progressively:
```bash
git init
git add README.md .gitignore PartA && git commit -m "Add Part A design"
git add TaskB1 && git commit -m "Complete Linux administration"
git add TaskB2 && git commit -m "Add Flask portal and Docker Compose"
git add TaskB3 && git commit -m "Add Kubernetes deployment and measurements"
git add TaskB4 && git commit -m "Add second service and production decision"
git branch -M main
git remote add origin https://github.com/<username>/CSA04-<RegisterNumber>-Assignment5.git
git push -u origin main
```
Add faculty as collaborator if private. Never commit `.env`, credentials, private keys or real student marks.

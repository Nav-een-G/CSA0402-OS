# Task B3 – Deployment comparison
Deploy the same Flask app on Linux directly, in a VirtualBox/KVM guest, and in Docker. Keep app version, worker count, endpoint and load-test settings identical.
For Minikube: build image in TaskB2, run `minikube image load result-portal:1.0`, then `kubectl apply -f deployment.yaml`. For kind: `kind load docker-image result-portal:1.0 --name <cluster>`.
Check `kubectl get pods`, `kubectl get services`; access with `kubectl port-forward service/result-portal 8080:80`.
Delete one pod and observe recreation: `kubectl delete pod <pod-name>` then `kubectl get pods -w`. Scale: `kubectl scale deployment result-portal --replicas=6`.
Important: for the full result search API to work in Kubernetes, also deploy PostgreSQL and set DATABASE_URL in the portal Deployment. The provided manifest is the requested replica/resource demonstration.
Example local load test: `ab -n 10000 -c 100 http://127.0.0.1:8000/`. Fill measurements.csv with your own results; never invent measurements.

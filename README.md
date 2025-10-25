# CLO835 – Assignment 2  
Student: Baran Heidari  

---

## Overview  
This assignment shows how I deployed a two-tier web application on Kubernetes using a Kind cluster running inside an AWS Cloud9 environment.
 The project includes a MySQL database as the backend and a Flask web application as the frontend.  

The goal was to understand how to create deployments, services, and manage application updates using Kubernetes resources.  
---
## Architecture  
- MySQL Deployment: Uses the `mysql:8.0` image. It runs as a pod inside the “web” namespace and is exposed only inside the cluster using a ClusterIP service.  
- Web Application Deployment: Uses my custom Docker image `bheidari3/clo835-app`. It connects to the MySQL service internally and is exposed to external users through NodePort `30001`.
  
Both applications communicate inside the same namespace through Kubernetes DNS.  
---
## Kubernetes Components  


| Component | Type | Namespace | Description |
| MySQL | Deployment + ClusterIP | web | Database layer |
| Web App | Deployment + NodePort | web | Flask web frontend |
| ReplicaSets | Managed by Deployments | web | Maintain pod count |
| Pods | - | web | Run the containers |
---
## Demonstrated Steps  
1. Verified single-node Kind cluster setup on AWS EC2.  
2. Created namespaces and deployed MySQL and web app pods.  
3. Configured environment variables for database connection.  
4. Exposed the web app on NodePort and accessed it from the browser.  
5. Verified pod logs and checked database connection.  
6. Performed image update to version v2 and observed rolling update.  
7. Managed commits and pushed Kubernetes manifests to GitHub.  
---

## Key Commands Used  

```bash
kind create cluster --name clo835
kubectl get nodes
kubectl apply -f k8s/mysql-deploy.yaml
kubectl apply -f k8s/web-deploy.yaml
kubectl get all -n web
kubectl port-forward svc/web-service -n web 8080:80
kubectl logs -n web -l app=web
kubectl set image deployment/web-deploy web=bheidari3/clo835-app:v2 -n web
git add .
git commit -m "Final version before submission"
git push origin main
Access Links
Web App (Cloud9 URL):
https://1e4d1e5afa5742948626ba7dd17ec73a.vfs.cloud9.us-east-1.amazonaws.com
GitHub Repository:
https://github.com/<your-username>/clo835-assignment2
Assignment Questions
Question	Answer
IP of the Kubernetes API server	127.0.0.1:37067
Can both applications listen on the same port?	Yes, because each pod runs in its own isolated network namespace.
Are ReplicaSets part of Deployments?	Yes. Each Deployment automatically creates and manages its ReplicaSet.
Why do we use different service types?	The database uses ClusterIP for internal access, and the web app uses NodePort to make it reachable from outside.

Commit History Summary
Initial commit for Assignment 2

Final version before submission

Added Kubernetes deployment manifests for MySQL and web app

All commits were made before the due date and reflect a clear step-by-step progression of my work.

 Assignment 2 completed successfully.
Both applications deployed, connected, and verified on a running Kind cluster in AWS Cloud9.
No credentials or private data were pushed to GitHub.

# 🛍️ E-Commerce App

A full-stack e-commerce application built using **Angular (Frontend)** and **Python Flask (Backend)**. The application is containerized using **Docker** and deployed on **Kubernetes** with separate services and deployments for each component.

---

## 📦 Tech Stack

- **Frontend**: Angular
- **Backend**: Python (Flask)
- **Web Server**: NGINX
- **Containerization**: Docker
- **Orchestration**: Kubernetes

---

## 📁 Project Structure
Ecomm/ ├── backend/ │ ├── app.py │ ├── Dockerfile │ └── requirements.txt │ ├── frontend/ │ ├── src/ │ ├── dockerfile │ ├── nginx.conf │ ├── angular.json │ ├── package.json │ └── ... │ ├── k8s/ │ ├── backend-deployment.yaml │ ├── backend-service.yaml │ ├── frontend-deployment.yaml │ └── frontend-service.yaml │ 


---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/shubkrsnha/Ecomm.git
cd Ecomm

cd backend
docker build -t ecomm-backend .

cd ../frontend
docker build -t ecomm-frontend .


☸️ Kubernetes Deployment

kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml

kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml

🌐 Accessing the App

Access the frontend via the exposed NodePort or LoadBalancer IP.

kubectl get svc
ecomm-frontend   NodePort   <Cluster-IP>   <none>   80:30000/TCP
ecomm-backend    ClusterIP  <Cluster-IP>   <none>   5000/TCP


You can access the frontend at http://<node-ip>:30000.




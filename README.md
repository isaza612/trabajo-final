# Proyecto trabajo-final

Este proyecto despliega una API en Python dentro de Kubernetes usando Helm y ArgoCD, siguiendo el enfoque GitOps.

Repositorio: https://github.com/isaza612/trabajo-final.git

---

## 🛠️ Tecnologías

- Python (FastAPI)
- PostgreSQL
- Docker
- Kubernetes + Helm
- ArgoCD (GitOps)
- GitHub Actions (CI/CD)

---

## 🚀 Despliegue manual con Helm

Clona el repositorio y realiza el despliegue en tu clúster:

```bash
git clone https://github.com/isaza612/trabajo-final.git
cd trabajo-final
helm install trabajo-final ./charts/trabajo-final -n trabajo-final --create-namespace

eks-gitops-microservice-pipeline/
├── .gitignore
├── README.md
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── versions.tf
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── .github/
    └── workflows/
        └── ci-cd.yml

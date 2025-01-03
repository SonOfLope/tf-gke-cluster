# Terraform GKE demo

## Prerequisites

- Terraform
- GCP account
- GCP project
- GCP service account

## Initial setup

```bash
!#/bin/bash
gcloud auth login account@example.com

gcloud config set project <projectid>

gcloud services enable compute.googleapis.com container.googleapis.com \
  --project <projectid>

gcloud projects add-iam-policy-binding <projectid> \
  --member="serviceAccount:serviceaccoutname@<projectid>.iam.gserviceaccount.com" \
  --role="roles/container.admin"

gcloud projects add-iam-policy-binding <projectid> \
  --member="serviceAccount:serviceaccoutname@<projectid>.iam.gserviceaccount.com" \
  --role="roles/compute.networkAdmin"

gcloud iam service-accounts keys create key.json \
  --iam-account=serviceaccoutname@<projectid>.iam.gserviceaccount.com \
  --project=<projectid>
  
```

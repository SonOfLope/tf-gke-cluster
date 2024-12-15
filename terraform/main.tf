terraform {
  required_version = ">= 1.10.0"
  
  backend "gcs" {
    bucket = "tf-state-bucket-sonoflope"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

locals {
  services = [
    "compute",
    "container"
  ]
}

resource "google_project_service" "default" {
  for_each           = toset(local.services)
  service            = "${each.value}.googleapis.com"
  disable_on_destroy = false
}

resource "google_service_account" "gke_sa" {
  account_id   = "gke-service-account"
  display_name = "GKE Service Account"
}

module "vpc" {
  source             = "./modules/vpc"
  
  vpc_name           = "prod-vpc"
  vpc_description    = "VPC for prod"
  subnet_name        = "prod-subnet"
  subnet_description = "Subnet for prod"
  
  region             = var.region
  cidrBlock          = "10.0.0.0/16"
}

module "gke_cluster" {
  source = "./modules/gke-cluster"

  cluster_name           = "prod-gke-cluster"
  project_id             = var.project_id
  region                 = var.region
  network                = module.vpc.vpc_name
  subnetwork             = module.vpc.subnet_name
  machine_type           = var.machine_type
  service_account_email  = google_service_account.gke_sa.email
}

module "dns_zone_gcp" {
  source      = "./modules/gke-dns-zone"
  project_id  = var.project_id
  zone_name   = var.zone_name
  subdomain   = var.subdomain
  ip_address  = var.ip_address
  subdomains  = var.subdomains
}

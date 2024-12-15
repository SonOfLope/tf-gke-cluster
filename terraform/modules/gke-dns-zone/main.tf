terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.74.0"
    }
  }
}

resource "google_dns_managed_zone" "dns_zone" {
  name        = var.zone_name
  dns_name    = "${var.subdomain}."
  description = "Managed zone for ${var.subdomain}"

  project = var.project_id
}

resource "google_dns_record_set" "a_records" {
  for_each    = toset(var.subdomains)
  name        = "${each.value}.${var.subdomain}."
  type        = "A"
  ttl         = 300
  managed_zone = google_dns_managed_zone.dns_zone.name
  rrdatas     = [var.ip_address]
}

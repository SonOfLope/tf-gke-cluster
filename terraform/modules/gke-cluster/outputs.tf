output "cluster_id" {
  value       = google_container_cluster.primary.id
}

output "cluster_master_version" {
  value       = google_container_cluster.primary.master_version
}

output "client_certificate" {
  value       = google_container_cluster.primary.master_auth.0.client_certificate
  sensitive   = true
}

output "client_key" {
  value       = google_container_cluster.primary.master_auth.0.client_key
  sensitive   = true
}

output "cluster_ca_certificate" {
  value       = google_container_cluster.primary.master_auth.0.cluster_ca_certificate
  sensitive   = true
}

output "endpoint" {
  value       = google_container_cluster.primary.endpoint
}
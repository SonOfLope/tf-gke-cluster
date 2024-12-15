output "name_servers" {
  description = "The nameservers for the managed zone."
  value       = google_dns_managed_zone.dns_zone.name_servers
}

output "zone_name" {
  value = google_dns_managed_zone.dns_zone.name
}

output "dns_name" {
  value = google_dns_managed_zone.dns_zone.dns_name
}

variable "project_id" {
  type = string
}

variable "region" {
  type    = string
  default = "us-central1"
}

variable "machine_type" {
  type    = string
  default = "e2-medium"
}

variable "zone_name" {
  type = string
}

variable "subdomain" {
  type = string
}

variable "ip_address" {
  type = string
}

variable "subdomains" {
  description = "List of subdomains to create A records for"
  type        = list(string)
}

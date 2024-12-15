variable "project_id" {
  type = string
}

variable "zone_name" {
  type = string
}

variable "subdomain" {
  type        = string
}

variable "ip_address" {
  type        = string
}

variable "subdomains" {
  description = "List of subdomains to create A records for"
  type        = list(string)
}

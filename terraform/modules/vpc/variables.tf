variable "vpc_name" {
  type        = string
}

variable "vpc_description" {
  type        = string
  default     = ""
}

variable "subnet_name" {
  type        = string
}

variable "subnet_description" {
  type        = string
  default     = ""
}

variable "cidrBlock" {
  type        = string
}

variable "region" {
  type        = string
}
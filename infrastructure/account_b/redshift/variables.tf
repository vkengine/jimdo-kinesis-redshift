variable "redshift_master_username" {
  type = string
}

variable "redshift_master_password_v1" {
  type = string
}

variable "redshift_cluster_name" {
  type = string
}

variable "redshift_database_name" {
  type = string
}

variable "redshift_node_type" {
  type = string
}

variable "redshift_cluster_type" {
  type = string
}

variable "redshift_cluster_region" {
  type = string
  default = "eu-central-1"
}
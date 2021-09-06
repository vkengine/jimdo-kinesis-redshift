provider "aws" {
  profile = "buildyourjazz"
  region  = var.redshift_cluster_region
}

resource "aws_redshift_cluster" "default" {
  cluster_identifier = var.redshift_cluster_name
  database_name      = var.redshift_database_name
  master_username    = var.redshift_master_username
  master_password    = var.redshift_master_password_v1
  node_type          = var.redshift_node_type
  cluster_type       = var.redshift_cluster_type
  skip_final_snapshot = "true"
  final_snapshot_identifier = "random"
}
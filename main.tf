provider "aws" {
  region = "eu-central-1"
}


/*
# this is to enable backend in case needed

terraform {
  backend "s3" {
    bucket = "jimdo-terraform-backend-bucket"
    key = "s3-redshift-lambda"
    region = "us-west-2"
  }
}
*/

/* Account A resources */

module "buckets" {
  source = "./infrastructure/account_a/buckets"
}

module "roles" {
  source = "./infrastructure/account_a/roles"
}

module "policy" {
  source = "./infrastructure/account_a/policy"
  kinesis_role_name = module.roles.kinesis_role_name
}


module "firehose_stream" {
  source = "./infrastructure/account_a/kinesis"
  user_event_bucket_arn = module.buckets.user_event_bucket_arn
  user_utm_bucket_arn = module.buckets.user_utm_bucket_arn
  kinesis_role_arn = module.roles.kinesis_role_arn
}


/*Account B resources*/

module "redshift_cluster" {
  source = "./infrastructure/account_b/redshift"
  redshift_cluster_name = "jimdo-redshift-cluster"
  redshift_database_name = "jimdo"
  redshift_node_type = "dc2.Large"
  redshift_cluster_type = "single-node"
  redshift_master_username = var.redshift_master_username
  redshift_master_password_v1 = var.redshift_mastr_password
}

module "account_b_security_group" {
  source = "./infrastructure/account_b/security_group"
}

module "account_b_bucket" {
  source = "./infrastructure/account_b/buckets"
}

module "account_b_roles" {
  source = "./infrastructure/account_b/roles"
}

module "account_b_lambda" {
  source = "./infrastructure/account_b/lambda"
}
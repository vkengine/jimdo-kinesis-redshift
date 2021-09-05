module "buckets" {
  source = "./infrastructure/account_a/buckets"
}

module "roles" {
  source = "./infrastructure/account_a/roles"
}

module "firehose_stream" {
  source = "./infrastructure/account_a/kinesis"
  user_event_bucket_arn = module.buckets.user_event_bucket_arn
  user_utm_bucket_arn = module.buckets.user_utm_bucket_arn
  kinesis_role = module.roles.kinesis_role
}
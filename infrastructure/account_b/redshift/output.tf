output "redshift_cluster_security_groups" {
  description = "The security groups associated with the cluster"
  value       = aws_redshift_cluster.default.cluster_security_groups
}

output "redshift_cluster_arn" {
  description = "The Redshift cluster ARN"
  value       = aws_redshift_cluster.default.arn
}

output "redshift_cluster_id" {
  description = "The security groups associated with the cluster"
  value       = aws_redshift_cluster.default.id
}

output "redshift_cluster_identifier" {
  description = "The Redshift cluster identifier"
  value       = aws_redshift_cluster.default.cluster_identifier
}

output "redshift_cluster_endpoint" {
  description = "The connection endpoint"
  value       = aws_redshift_cluster.default.endpoint
}

output "redshift_cluster_hostname" {
  description = "The hostname of the Redshift cluster"
  value = replace(
    aws_redshift_cluster.default.endpoint,
    format(":%s", aws_redshift_cluster.default.port),
    "",
  )
}

output "redshift_cluster_port" {
  description = "The port the cluster responds on"
  value       = aws_redshift_cluster.default.port
}

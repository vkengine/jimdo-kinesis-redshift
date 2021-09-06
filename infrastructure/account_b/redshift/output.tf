output "redshift_cluster_security_groups" {
  description = "The security groups associated with the cluster"
  value       = aws_redshift_cluster.default.cluster_security_groups
}
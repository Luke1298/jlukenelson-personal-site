resource "aws_codestarconnections_connection" "repo_connection" {
  name          = "jlukenelson-personal-connect"
  provider_type = "GitHub"
}

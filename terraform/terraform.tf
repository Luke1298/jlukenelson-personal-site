resource "aws_s3_bucket" "terraform_state_bucket" {
  bucket = "terraform-state-jlukenelson-personal-site"
  acl    = "private"
}

resource "aws_codebuild_project" "jln_terraform_codebuild" {
  name          = "jln-personal-site-terraform"
  service_role  = aws_iam_role.default.arn
  build_timeout = "60"

  artifacts {
    type                = "NO_ARTIFACTS"
  }

  cache {
    type  = "LOCAL"
    modes = ["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE"]
  }

  environment {
    compute_type    = "BUILD_GENERAL1_SMALL"
    image           = "aws/codebuild/standard:5.0"
    image_pull_credentials_type = "CODEBUILD"
    type            = "LINUX_CONTAINER"
    privileged_mode = "true"

    environment_variable {
      name = "TERRAFORM_STATE_BUCKET"
      value = aws_s3_bucket.terraform_state_bucket.id
      type = "PLAINTEXT"
    }
  }

  source {
    type      = "GITHUB"
    location  = "https://github.com/Luke1298/jlukenelson-personal-site.git"
    git_clone_depth = 1
    buildspec = "terraform/buildspec.yml"
  }
}

resource "aws_codebuild_webhook" "jln_terraform_codebuild_webhook" {
  project_name = aws_codebuild_project.jln_terraform_codebuild.name

  filter_group {
    filter {
      type    = "EVENT"
      pattern = "PUSH"
    }

    filter {
      type    = "HEAD_REF"
      pattern = "main"
    }

    filter {
      type    = "FILE_PATH"
      pattern = "^terraform\\/.*"
    }
  }
}

resource "aws_iam_role" "default" {
  name               = "jlukenelsonPersonalSiteTerraformCodebuildRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume_role_policy.json
}

resource "aws_iam_policy" "default" {
  name        = "jlukenelsonPersonalSiteTerraformCodebuildPolicy"
  policy      = data.aws_iam_policy_document.codebuild_policy.json
}

resource "aws_iam_role_policy_attachment" "default" {
  role       = aws_iam_role.default.name
  policy_arn = aws_iam_policy.default.arn
}

locals {
  log_group_arn = "arn:aws:logs:${local.region}:${local.account_id}:log-group:/aws/codebuild/jlukenelson-personal-site-terraform"

  region     = data.aws_region.current.name
  account_id = data.aws_caller_identity.current.account_id
}

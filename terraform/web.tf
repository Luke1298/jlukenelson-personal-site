resource "aws_codebuild_project" "jln_web_codebuild" {
  name          = "jlukenelson-dot-com"
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
  }

  source {
    type      = "GITHUB"
    location  = "https://github.com/Luke1298/jlukenelson-personal-site.git"
    git_clone_depth = 1
    buildspec = "frontend/buildspec.yml"
  }
}

resource "aws_codebuild_webhook" "jln_web_codebuild_webhook" {
  project_name = aws_codebuild_project.jln_web_codebuild.name

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
      pattern = "^frontend\\/.*"
    }
  }
}

resource "aws_s3_bucket" "j_luke_nelson_site" {
  bucket = "j-luke-nelson-personal-site"
  acl    = "private"
}

data "aws_iam_policy_document" "front_end_post_build_lambda_role" {
  statement {
    sid = "1"
    effect = "Allow"
    actions = [
      "logs:*",
      "codepipeline:PutJobFailureResult",
      "codepipeline:PutJobSuccessResult",
      "cloudfront:GetDistribution",
      "cloudfront:CreateInvalidation" # Invalidation isn't that dangerous, so it's ok to grant for everything
    ]
    resources = ["*"]
  }
}

resource "aws_iam_role" "jln_front_end_default" {
  name               = "jlukenelsonPersonalSiteWebCodePipline"
  assume_role_policy = data.aws_iam_policy_document.codepipeline_assume_role_policy.json
}

resource "aws_iam_policy" "jln_front_end_default" {
  name        = "front-end-default-policy"
  policy      = data.aws_iam_policy_document.codepipeline_policy.json
}

resource "aws_iam_role_policy_attachment" "jln_front_end_default" {
  role                 = aws_iam_role.jln_front_end_default.name
  policy_arn           = aws_iam_policy.jln_front_end_default.arn
}

resource "aws_s3_bucket" "jln_personal_site_artifact_bucket" {
  bucket = "jln-personal-site-artifact-bucket"
  acl    = "private"
}

resource "aws_codepipeline" "jln_web_codepipeline" {
  name                 = "jln-front-end"
  role_arn             = aws_iam_role.jln_front_end_default.arn

  depends_on = [
    aws_iam_role_policy_attachment.jln_front_end_default,
    aws_codestarconnections_connection.repo_connection
  ]

  artifact_store {
    location           = aws_s3_bucket.jln_personal_site_artifact_bucket.id
    type               = "S3"
  }

  stage {
    name = "Source"

    action {
      name             = "Source"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = "1"
      output_artifacts = ["SourceArtifact"]
      configuration = {
        ConnectionArn    = aws_codestarconnections_connection.repo_connection.arn
        FullRepositoryId = "Luke1298/jlukenelson-personal-site"
        BranchName       = "main"
      }
    }
  }

  stage {
    name = "Build"

    action {
      name     = "Build"
      category = "Build"
      owner    = "AWS"
      provider = "CodeBuild"
      version  = "1"

      input_artifacts  = ["SourceArtifact"]
      output_artifacts = ["BuildArtifact"]

      configuration = {
        ProjectName = aws_codebuild_project.jln_web_codebuild.name
      }
    }
  }

  stage {
    name = "Deploy"

    action {
      name            = "Deploy"
      category        = "Deploy"
      owner           = "AWS"
      provider        = "S3"
      input_artifacts = ["BuildArtifact"]
      version         = "1"

      configuration = {
                        BucketName = aws_s3_bucket.j_luke_nelson_site.id
                        Extract = true
                      }
    }
  }
}

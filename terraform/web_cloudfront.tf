locals {
  bucket_name = "j-luke-nelson-personal-site"
}

resource "aws_cloudfront_origin_access_identity" "default" {
  comment = "Cloudfront Origin Access Identity for user images distribution"
}

data "aws_iam_policy_document" "cloudfront_distro" {
  statement {
    sid = "S3GetObjectForCloudFront"

    actions   = ["s3:GetObject"]
    resources = ["arn:aws:s3:::${local.bucket_name}/*"]

    principals {
      type        = "AWS"
      identifiers = [aws_cloudfront_origin_access_identity.default.iam_arn]
    }
  }

  statement {
    sid = "S3ListBucketForCloudFront"

    actions   = ["s3:ListBucket"]
    resources = ["arn:aws:s3:::${local.bucket_name}"]

    principals {
      type        = "AWS"
      identifiers = [aws_cloudfront_origin_access_identity.default.iam_arn]
    }
  }
}

resource "aws_s3_bucket" "j_luke_nelson_site" {
  bucket = local.bucket_name
  acl    = "private"
  policy        = data.aws_iam_policy_document.cloudfront_distro.json
  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["GET", "HEAD", "POST", "PUT"]
    allowed_origins = ["*"]
    max_age_seconds = 3000
  }
}


resource "aws_cloudfront_distribution" "web_s3_distribution" {
  enabled             = true
  is_ipv6_enabled     = true
  price_class         = "PriceClass_All"
  aliases             = var.domain_names
  default_root_object = "index.html"

  custom_error_response {
    # Single page applications need to have all routes go to the default_root_object so that www.example.com/foo/bar will load the root page, then JS picks up the routing
    error_code = 404
    response_code = 200
    response_page_path = "/index.html"
  }

  origin {
    domain_name = aws_s3_bucket.j_luke_nelson_site.bucket_regional_domain_name
    origin_id   = "S3-${aws_s3_bucket.j_luke_nelson_site.bucket}"

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.default.cloudfront_access_identity_path
    }
  }

  viewer_certificate {
    minimum_protocol_version       = "TLSv1"
    acm_certificate_arn = var.ssl_certificate
    cloudfront_default_certificate = false
    ssl_support_method = "sni-only"
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-${aws_s3_bucket.j_luke_nelson_site.bucket}"
    trusted_signers  = null

    forwarded_values {
      query_string = false
      headers      = ["Access-Control-Request-Headers", "Access-Control-Request-Method", "Origin"]

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    default_ttl            = 60
    min_ttl                = 0
    max_ttl                = 86400
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }
}

variable "domain_names" {
  description = "The domain names for jlukenelson.com"
  default = ["www.jlukenelson.com", "jlukenelson.com"]
}

variable "ssl_certificate" {
  description = "The ssl_certificate for jlukenelson.com"
  default = "arn:aws:acm:us-east-1:277168111148:certificate/0405987d-beb3-4ea8-a0dc-20cf3da5fe7f"
}

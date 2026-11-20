# Course 1: Introduction to the AWS Developer Learning Plan

This foundational course sets up your local development environment, establishes programmatic access to AWS, and introduces the core security rules every AWS developer must follow before writing application code.

---

## 1. The AWS Shared Responsibility Model (Developer Perspective)

Before interacting with AWS services, you must understand where AWS’s operational security ends and yours begins.

* **AWS Responsibility ("Security of the Cloud"):** Physical data centers, hardware, networking infrastructure, virtualization layers, and the underlying host OS/hypervisors for managed services (such as AWS Lambda or Amazon DynamoDB).
* **Developer/Customer Responsibility ("Security in the Cloud"):**
  * Managing IAM users, roles, and least-privilege policies.
  * Securing application code and dependencies.
  * Encrypting data in transit (TLS) and at rest (KMS).
  * Protecting API keys, database credentials, and environment variables.

---

## 2. Identity and Access Management (IAM) Essentials

Developers rarely interact with AWS using the account root user. Instead, access is controlled through IAM entities and policies.

### Core IAM Entities

* **IAM User:** A long-term identity representing a person or specific service, authenticated via a password (Console) or Access Keys (CLI/SDK). *Best practice: Avoid long-term access keys on local machines in favor of temporary credentials.*
* **IAM Group:** A collection of IAM users. Permissions are attached to the group—not individual users—to simplify role management (e.g., `Developers`, `ReadOnlyAuditors`).
* **IAM Role:** An identity with specific permissions that can be assumed temporarily by trusted entities (an EC2 instance, a Lambda function, or a federated developer via AWS IAM Identity Center). Roles issue temporary security credentials via AWS STS (Security Token Service).

### Anatomy of an IAM Policy

Permissions are defined in JSON documents. By default, everything is **implicitly denied**, and an **explicit Deny** always overrides an **explicit Allow**.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3BucketRead",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::my-dev-app-bucket",
        "arn:aws:s3:::my-dev-app-bucket/*"
      ]
    }
  ]
}
```

* **Effect:** `Allow` or `Deny`.
* **Action:** The specific API call(s) permitted or restricted (`service:Operation`).
* **Resource:** The exact Amazon Resource Name (ARN) the action applies to. Avoid `"Resource": "*"` in production to enforce the Principle of Least Privilege.

---

## 3. Programmatic Access: AWS CLI & SDKs

Every action in the AWS Management Console is an HTTP API call under the hood. Developers automate and integrate AWS into applications using two primary interfaces:

### A. AWS Command Line Interface (CLI)

Allows you to control AWS services directly from your terminal and automate tasks via shell scripts.

* **Configuration:** Running `aws configure` stores credentials in `~/.aws/credentials` and default settings (region, output format) in `~/.aws/config`.
* **Named Profiles:** Crucial for separating `dev`, `staging`, and `production` environments locally:
  ```bash
  aws configure --profile dev-env
  aws s3 ls --profile dev-env
  ```
* **Modern Authentication (IAM Identity Center / SSO):** Instead of static access keys, modern setups run `aws configure sso` to generate short-lived tokens that automatically refresh in the background.

### B. AWS Software Development Kits (SDKs)

Libraries that wrap raw AWS REST APIs into idiomatic code for your language (e.g., Boto3 for Python, AWS SDK for JavaScript v3, AWS SDK for Java 2.x).

* **Automatic Credential Chain:** When your code initializes an AWS client, the SDK automatically searches for credentials in a strict order—meaning you never hardcode keys in your source code:
  1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`)
  2. Shared credentials file (`~/.aws/credentials` or SSO cache)
  3. Container credentials (ECS task roles)
  4. Instance profile credentials (EC2 IAM roles) or Lambda execution roles

* **Example (Python / Boto3):**
  ```python
  import boto3

  # Automatically uses local CLI profile or cloud IAM role
  s3 = boto3.client("s3", region_name="us-east-1")
  response = s3.list_buckets()

  for bucket in response["Buckets"]:
      print(bucket["Name"])
  ```

---

## 4. Developer Environment & Tooling Stack

To complete hands-on labs and build cloud-native applications, configure your local workstation with the following tools:

1. **IDE + AWS Toolkit:** Visual Studio Code (or JetBrains) with the AWS Toolkit extension to browse resources, view CloudWatch logs, and invoke functions locally.
2. **Git & Version Control:** Managing source code and infrastructure-as-code (IaC) templates.
3. **Docker:** Building container images and simulating AWS Lambda environments locally.
4. **AWS SAM CLI (Serverless Application Model):** An open-source framework and CLI tool used to build, test, debug, and deploy serverless applications directly from your machine.

---

## Key Exam & Best-Practice Takeaways

* **Protect Secrets:** Never commit `~/.aws/credentials` or hardcode API keys into Git repositories.
* **Lock Down Root:** Always enable MFA (Multi-Factor Authentication) on the root account and lock away root credentials.
* **Prefer Temporary Credentials:** Use IAM Roles for compute services (Lambda, EC2, ECS) and IAM Identity Center (SSO) for human developers rather than static IAM User access keys.
* **Know Your ARNs:** Understand the standard Amazon Resource Name format:
  `arn:partition:service:region:account-id:resource-type/resource-id`

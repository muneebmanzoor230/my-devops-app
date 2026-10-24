# 🚀 AWS Serverless CI/CD Pipeline & Infrastructure Dashboard

An end-to-end DevOps project demonstrating continuous integration, containerization, and serverless deployment on Amazon Web Services (AWS). 

This project takes a Python Flask application from a raw source code repository all the way to a highly available, zero-downtime production environment using Jenkins and AWS ECS Fargate.

## 🏗️ Architecture Flow

`Developer Push` ➡️ `GitHub` ➡️ `Jenkins CI` ➡️ `Amazon ECR` ➡️ `AWS ECS Fargate` ➡️ `Application Load Balancer (ALB)`

## 🛠️ Tech Stack & Tools
* **Application:** Python (Flask), HTML/CSS
* **Containerization:** Docker
* **CI/CD Automation:** Jenkins, Groovy (Jenkinsfile)
* **Cloud Provider:** Amazon Web Services (AWS)
* **AWS Services Used:** EC2, IAM Roles, ECR, ECS (Fargate), Application Load Balancer (ALB), VPC Networking.

## 🌟 Key Features
* **Serverless Compute:** Deployed on AWS Fargate, eliminating the need to provision or manage underlying EC2 operating systems.
* **Automated CI/CD:** A declarative `Jenkinsfile` automatically triggers on code commits, builds the Docker image, tags it, and pushes it to ECR.
* **Zero-Downtime Deployments:** Configured ECS rolling updates. New containers are spun up and verified via ALB `/health` checks before old containers are terminated.
* **Secure Authentication:** Implemented AWS IAM Instance Profiles for the Jenkins server, adhering to security best practices by avoiding hardcoded AWS Access Keys.
* **Modern UI:** Features a dark-mode infrastructure monitoring dashboard displaying real-time container IP and UTC timestamps.

## 🐛 Real-World Troubleshooting & Lessons Learned
During the development of this pipeline, I encountered and resolved several industry-standard infrastructure challenges:

1. **ALB Routing Conflicts (Instance vs. IP):** Transitioning from a manual EC2 deployment to ECS Fargate caused Load Balancer 502 errors. *Resolution:* Identified that Fargate uses `awsvpc` networking. Created a new Target Group utilizing `IP` routing instead of `Instance` routing and updated the ALB listener rules.
2. **Container Caching Traps:** ECS failed to pull new UI updates despite successful Jenkins builds. *Resolution:* Identified that relying on the `:latest` Docker tag causes Fargate to use cached images. Terminated the old tasks to force a fresh pull, and learned the best practice of tagging images with unique Build IDs.
3. **Jenkins Service Failures:** Jenkins crashed on startup due to system daemon loops. *Resolution:* Debugged Linux logs using `journalctl` and `systemctl`, identifying a deprecated Java 17 environment. Upgraded the EC2 instance to

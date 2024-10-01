# Multi-Environment REST-API Deployment on AWS Using Terraform
## Introduction

I wanted to share a workflow I’ve implemented for deploying a Python-based Flask REST API across multiple environments (Dev, Staging, and Prod) using Terraform and Jenkins on AWS. This is all automated and managed via three GitHub repositories that each play a crucial role in the setup.

## Project Overview
- **Python-app**: https://github.com/krishchadha/python-terraform
- **Infrastructure**: https://github.com/krishchadha/infra-terraform
- **Jenkins-terraform**: https://github.com/krishchadha/jenkins-terraform

## Structure:
![Alt text](https://github.com/krishchadha/Devop_projects/blob/main/Multi-Environment%20REST%20API%20Deployment%20on%20AWS%20Using%20Jenkins%2C%20Terraform%2C%20and%20MySQL%20RDS/Screenshot%202024-09-28%20200238.png)

## Overview
I use Jenkins for CI/CD and Terraform for infrastructure-as-code, ensuring seamless and scalable infrastructure management. The workflow enables us to spin up resources in AWS, configure environments, and deploy the application automatically.

1. Jenkins Infrastructure Repo
This repository houses the Terraform code that automates the setup of the Jenkins infrastructure.
**Components**:
- AWS Certificate Manager (ACM)
- Hosted Zone
- Application Load Balancer (ALB) and Target Groups
- Networking (VPC, Subnets, etc.)
- Security Groups
- Jenkins Server and Configuration Scripts
Once the Jenkins server is up and running, it is the backbone of the CI/CD process.

2. Python App Repo
This repository contains the Python Flask REST API code.
The app is packaged and deployed on EC2 instances created during infrastructure provisioning.

3. AWS Infrastructure Repo
This repo holds the Terraform code responsible for creating AWS infrastructure for different environments (Dev, Staging, Prod).
Resources created include:
- ACM, Hosted Zone
- ALB & Target Groups
- EC2 for app deployment
- RDS (PostgreSQL) for data persistence
- S3 for object storage
- Networking and Security Groups

## Jenkins Pipeline 🚀

1. **Select Environment**: In Jenkins, we can choose which environment (Dev, Staging, Prod) we want to deploy to.
2. **Terraform Plan/Apply/Destroy**: Based on the selected environment, Jenkins triggers the respective Terraform action:
- Plan: Review the changes.
- Apply: Create or update the infrastructure.
- Destroy: Tear down the infrastructure (useful for testing and development environments).
3. **Deploy App**: After the infrastructure is up, Jenkins deploys the Flask REST API on the provisioned EC2 instances in the selected environment.

Accessing Jenkins via custom Domain:

![Alt text](https://github.com/krishchadha/Devop_projects/blob/main/Multi-Environment%20REST%20API%20Deployment%20on%20AWS%20Using%20Jenkins%2C%20Terraform%2C%20and%20MySQL%20RDS/Screenshot%202024-10-01%20154736.png)

## Why this Workflow?
- Automation: No manual configuration. Everything is controlled via code.
- Scalability: The infrastructure can be easily expanded as traffic and demand grow.
- Multi-Environment Setup: Easily manage different environments with isolated resources.
- Simplicity: Jenkins pipelines make the deployment process straightforward and easy to track.


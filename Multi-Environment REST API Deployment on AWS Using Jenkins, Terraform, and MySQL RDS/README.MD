# Multi-Environment REST-API Deployment on AWS Using Terraform
## Introduction

This project demonstrates the automation of CI/CD pipelines using Jenkins to deploy a Python Flask REST-API across multiple environments: Development, Staging, and Production. The infrastructure is managed using Terraform, and the deployment integrates various AWS services, ensuring a highly available, scalable, and secure architecture.

## Project Overview
- **Python-app**: https://github.com/krishchadha/python-terraform
- **Infrastructure**: https://github.com/krishchadha/infra-terraform
- **Jenkins-terraform**: https://github.com/krishchadha/jenkins-terraform

Structure:
https://github.com/krishchadha/Devop_projects/blob/main/Multi-Environment%20REST%20API%20Deployment%20on%20AWS%20Using%20Jenkins%2C%20Terraform%2C%20and%20MySQL%20RDS/Screenshot%202024-09-28%20200238.png

## Features
- **Automated CI/CD**: Jenkins pipeline automates testing, building, and deploying the Flask REST-API.
- **Multi-Environment Setup**: Infrastructure is provisioned and managed for Dev, Staging, and Production environments.

### Architecture:
- **EC2**: Flask REST-API runs on EC2 instances.
- **MySQL RDS**: Persistent database storage using AWS RDS.
- **AWS Lambda**: Serverless functions for specific asynchronous tasks.
- **High Availability**: Ensured with Elastic Load Balancer (ELB).
- **VPC Networking**: Custom Virtual Private Cloud (VPC) setup with subnets, Internet Gateway, Route tables, and Security Groups provisioned via Terraform.
- **HTTPS & Domain Security**: Secured using custom domains, AWS Route 53 for DNS management, and AWS ACM for SSL/TLS certificates.

### Infrastructure Overview
- **Jenkins**: Handles continuous integration and deployment tasks. The pipeline deploys infrastructure and application code automatically across different environments.

### AWS Resources:

- **EC2 Instances**: Hosts the Flask application.
- **RDS MySQL**: Database backend for the REST API.
- **Elastic Load Balancer (ELB)**: Distributes traffic across EC2 instances to ensure availability.
- **VPC**: Custom network configuration to isolate resources and control access via:
- **Subnets**
- **Internet Gateway**
- **Route Tables**
- **Security Groups**
- **Terraform**: Infrastructure as code (IaC) tool used to provision AWS resources. Terraform scripts manage:
- **ELB**
- **Route 53 (DNS)**
- **ACM (SSL/TLS certificates)**

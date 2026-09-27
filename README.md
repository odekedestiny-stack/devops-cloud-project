# Automated AWS Cloud Infrastructure with Terraform

## 🚀 Project Overview
This project serves as the foundational milestone for a production-ready cloud environment. It uses Infrastructure as Code (IaC) to automatically provision an AWS EC2 virtual server wrapped inside custom firewall security rules.

   vvvvvvbb b                                                     * **Infrastructure as Code:** Terraform
* **Cloud Platform:** Amazon Web Services (AWS)
* **Base OS:** Ubuntu 24.04 LTS Linux

## 📋 Implementation Details
1. **Workspace Setup:** Configured a local environment on Windows 11 using VS Code.
2. **Provider Block:** Set up the `hashicorp/aws` integration plugin to point safely to `us-east-1`.
3. **Security Firewall:** Configured an inbound traffic rule on port `80` (HTTP) to prepare the server 
for a future web application container.
4. **Compute Instance:** Defined a free-tier eligible `t2.micro` Ubuntu virtual machine.


# My First GitHub Actions

This repository contains a simple Python project that uses GitHub Actions for Continuous Integration (CI). The workflow runs on a self-hosted runner hosted on an AWS EC2 instance.

## Setup Instructions

### 1. Setting Up the EC2 Instance as a Self-Hosted Runner

Follow these steps to configure your EC2 instance as a self-hosted runner for GitHub Actions:

#### Launch an EC2 Instance:

- Go to the AWS Management Console.
- Launch a new EC2 instance with an operating system of your choice (e.g., Ubuntu, Amazon Linux).
- Ensure the instance has a public IP and that security groups allow SSH access (port 22).

#### Connect to Your EC2 Instance:

Use SSH to connect to your EC2 instance.

```bash
ssh -i /path/to/your-key.pem ubuntu@<EC2-public-IP>
```
#### Set Up GitHub Runner on EC2:

- Go to your GitHub repository.
- Click on **Settings > Actions > Runners > New self-hosted runner**.
- Follow the on-screen instructions to download, install, and configure the GitHub Actions runner.
 #### Run the Runner:

Start the runner using the following command:

```bash
./run.sh
```

### 2. GitHub Actions Workflow

The GitHub Actions workflow is defined in the `.github/workflows/first-actions.yml` file.

The workflow:
- Triggers on every `push` to the repository.
- Uses the self-hosted runner on your EC2 instance.
- Tests a Python script (`prime_numbers.py`) across Python versions 3.8 and 3.9.

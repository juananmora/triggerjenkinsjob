# TriggerJenkinsJob GitHub Action

This GitHub Action triggers a Jenkins job from your GitHub Actions workflow.

## Inputs

- `urljenkins`: The Jenkins Job URL. (required)
- `user`: The username for HTTP basic auth. (required)
- `password`: The password (or token) for HTTP basic auth. (required)
- `job`: The Job Name. (required)
- `params`: Job Params in Json format. (required)

## Workflow
The Action follows these steps:

- Checkout repository: It checkouts the 'juananmora/jenkins_actions' repository at the 'development' reference using 'actions/checkout@v4'.

- Setup Python: It sets up a Python environment with version 3.9 using 'actions/setup-python@v4'.

- Setup Node.js environment: It sets up a Node.js environment with version 16 using 'actions/setup-node@v4'.

- Install dependencies: It installs the necessary Python packages using pip (requests, argparse, and jenkinsapi).

- Run the script: It runs the 'jenkins_job.py' script with the entered inputs.

This script is run within a bash shell with the inputs mentioned above.

The primary aim of this GitHub Action is to aid the process of triggering Jenkins jobs from a GitHub workflow simple and straightforward.

## Note
This action uses the Node version 16 and Python version 3.9 environment to run the Python script that triggers the Jenkins job. Please ensure that the Jenkins job is compatible with these versions.

## Usage

```yaml
- name: Trigger Jenkins Job
  uses: juananmora/triggerjenkinsjob@v1
  with:
    urljenkins: 'http://my_jenkins_url'
    user: 'my_username'
    password: 'my_token'
    job: 'my_job'
    params: '{"field1":"value1"}'


TriggerJenkinsJob GitHub Action
This Action triggers a Jenkins job directly from your GitHub workflows.

Inputs
urljenkins
Required The Jenkins Job URL.
user
Required The username for HTTP basic auth - used to authenticate with the Jenkins server.
password
Required The password (or token) for HTTP basic auth - used to authenticate with the Jenkins server.
job
Required The name of the Job to be triggered in Jenkins.
params
Required The parameters for the Job to be triggered.
Example Usage
- name: Trigger Jenkins Job
  uses: juananmora/TriggerJenkinsJob@v1
  with:
    urljenkins: 'http://my_jenkins_url'
    user: 'my_username'
    password: 'my_password'
    job: 'my_job'
    params: 'my_params'
Workflow
The Action follows these steps:

Checkout repository: It checkouts the 'juananmora/jenkins_actions' repository at the 'development' reference using 'actions/checkout@v4'.

Setup Python: It sets up a Python environment with version 3.9 using 'actions/setup-python@v4'.

Setup Node.js environment: It sets up a Node.js environment with version 16 using 'actions/setup-node@v4'.

Install dependencies: It installs the necessary Python packages using pip (requests, argparse, and jenkinsapi).

Run the script: It runs the 'jenkins_job.py' script with the entered inputs.

This script is run within a bash shell with the inputs mentioned above.

The primary aim of this GitHub Action is to aid the process of triggering Jenkins jobs from a GitHub workflow simple and straightforward.

Note
This action uses the Node version 16 and Python version 3.9 environment to run the Python script that triggers the Jenkins job. Please ensure that the Jenkins job is compatible with these versions.


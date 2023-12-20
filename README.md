TriggerJenkinsJob GitHub Action
This GitHub Action triggers a Jenkins job.

Inputs
This action requires the following inputs:

urljenkins
The Jenkins Job URL. This is required for the action to know where to trigger the job.

user
The username for HTTP basic auth. This is required to authenticate with the Jenkins server.

password
The password (or token) for HTTP basic auth. This, too, is required to authenticate with the Jenkins server.

job
The Job Name. The action requires this to know which job to trigger.

params
Job Params. This input is required and it specifies the parameters for the job.

Workflow
The Action follows these steps:

Checkout repository: It uses the version 4 of 'actions/checkout' to checkout the repository 'juananmora/jenkins_actions' at the reference 'development'.

Setup Python: It uses 'actions/setup-python@v4' to set up a Python environment with version 3.9.

Setup Node.js environment: It uses 'actions/setup-node@v4' to set up a Node.js environment with version 16.

Install dependencies: It installs pip, requests, argparse, and jenkinsapi packages using pip.

Run the script: It runs the 'jenkins_job.py' script with various inputs.

The script will be run in a bash shell with the mentioned inputs.

Example Usage
- name: Trigger Jenkins Job
  uses: juananmora/TriggerJenkinsJob@v1
  with:
    urljenkins: 'http://my_jenkins_url'
    user: 'my_username'
    password: 'my_password'
    job: 'my_job'
    params: 'my_params'
This GitHub Action aims to make the process of triggering Jenkins jobs from a GitHub workflow easy and straightforward.


TriggerJenkinsJob GitHub Action
This GitHub Action triggers a Jenkins job.

Inputs
This action requires the following inputs:

urljenkins: The Jenkins Job URL. This is required for the action to know where to trigger the job.

user: The username for HTTP basic auth. This is required to authenticate with the Jenkins server.

password: The password (or token) for HTTP basic auth. This, too, is required to authenticate with the Jenkins server.

job: The Job Name. The action requires this to know which job to trigger.

params: Job Params. This input is required and it specifies the parameters for the job.

Workflow
The Action follows these steps:

Checkout repository: It uses the version 4 of 'actions/checkout' to checkout the repository 'juananmora/jenkins_actions' at the reference 'development'.

Setup Python: It uses 'actions/setup-python@v4' to set up a Python environment with version 3.9.

Setup Node.js environment: It uses 'actions/setup-node@v4' to set up a Node.js environment with version 16.

Install dependencies: It installs pip, requests, argparse, and jenkinsapi packages using pip.

Run the script: It runs the 'jenkins_job.py' script with various inputs.

The script will be run in a bash shell with the mentioned inputs.

Example Usage
- name: Trigger Jenkins Job
  uses: juananmora/TriggerJenkinsJob@v1
  with:
    urljenkins: 'http://my_jenkins_url'
    user: 'my_username'
    password: 'my_password'
    job: 'my_job'
    params: 'my_params'
This GitHub Action aims to make the process of triggering Jenkins jobs from a GitHub workflow easy and straightforward.

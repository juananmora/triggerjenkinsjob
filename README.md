# TriggerJenkinsJob GitHub Action

This GitHub Action triggers a Jenkins job from your GitHub Actions workflow.

## Inputs

- `urljenkins`: The Jenkins Job URL. (required)
- `user`: The username for HTTP basic auth. (required)
- `password`: The password (or token) for HTTP basic auth. (required)
- `job`: The Job Name. (required)
- `params`: Job Params. (required)

## Usage

```yaml
name: Trigger Jenkins Job

on:
  push:
    branches:
      - main

jobs:
  trigger-jenkins-job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          repository: juananmora/jenkins_actions
          ref: development

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: '16'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install requests argparse jenkinsapi
        shell: bash

      - name: Run the script
        run: |
          python jenkins_job.py ${{ inputs.urljenkins }} ${{ inputs.user }} ${{ inputs.password }} ${{ inputs.job }} '${{ inputs.params }}'
        shell: bash

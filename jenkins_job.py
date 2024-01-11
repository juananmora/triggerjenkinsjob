import argparse
import logging
import json
import time
import sys
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.custom_exceptions import UnknownJob
from requests.exceptions import RequestException

logging.basicConfig(level=logging.INFO)

def get_jenkins_job_url(jenkins_url, job_name, build_number):
    return "{url}/job/{job}/build/{build}/".format(url=jenkins_url, job=job_name, build=build_number)


def get_jenkins_server_instance(url, username, password):
    try:
        return Jenkins(url, username=username, password=password)
    except RequestException as e:
        logging.error("Failed to connect to Jenkins server: %s", e)
        sys.exit(1)

def trigger_jenkins_job(jenkins_url, username, password, job, params):
    server = get_jenkins_server_instance(jenkins_url, username, password)

    job_name = job  # or use params['jobName'] if jobName is a passed parameter
    if job_name not in server.keys():
        logging.error("Job '%s' not found.", job_name)
        sys.exit(1)

    try:
        job = server[job_name]
        queue_item = job.invoke(build_params=params)
        queue_item.block_until_complete()
       
        build = queue_item.get_build()
        build_number = build.get_number() # obtener el número del build

       
        logging.info(build.get_console())
        
        logging.info("Job status: %s", build.get_status())
        

        # Obtener la URL completa del job
        job_url = get_jenkins_job_url(jenkins_url, job_name, build_number)
        logging.info("Jenkins Job URL: %s", job_url)
        
        if build.get_status() != 'SUCCESS':
            sys.exit(1)

    except UnknownJob as e:
        logging.error("Job '%s' not found: %s", job_name, e)
        sys.exit(1)

    except Exception as e:
        logging.error("Failed to build job '%s': %s", job_name, e)
        sys.exit(1)
        
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trigger Jenkins Job")
    parser.add_argument('urljenkins', type=str, help='url of Jenkins')
    parser.add_argument('user', type=str, help='username for authentication')
    parser.add_argument('token', type=str, help='token for authentication')
    parser.add_argument('job', type=str, help='job of Jenkins')
    parser.add_argument('parameters', type=str, help='other parameters in JSON format')

    args = parser.parse_args()
    params = json.loads(args.parameters)

    trigger_jenkins_job(args.urljenkins, args.user, args.token, args.job,params)
        if build.get_status() != 'SUCCESS':
            sys.exit(1)

    except UnknownJob as e:
        logging.error("Job '%s' not found: %s", job_name, e)
        sys.exit(1)

    except Exception as e:
        logging.error("Failed to build job '%s': %s", job_name, e)
        sys.exit(1)
        
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trigger Jenkins Job")
    parser.add_argument('urljenkins', type=str, help='url of Jenkins')
    parser.add_argument('user', type=str, help='username for authentication')
    parser.add_argument('token', type=str, help='token for authentication')
    parser.add_argument('job', type=str, help='job of Jenkins')
    parser.add_argument('parameters', type=str, help='other parameters in JSON format')

    args = parser.parse_args()
    params = json.loads(args.parameters)

    trigger_jenkins_job(args.urljenkins, args.user, args.token, args.job,params)

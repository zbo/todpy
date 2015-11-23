__author__ = "ian.zhang"
from jenkinsapi.jenkins import Jenkins

class JenkinsConnector:

    def __init__(self, args):
        self.jenkins = Jenkins(args['url'],args['username'],args['password'])

    def getJenkins(self):
        return self.jenkins

    def start_job_with_params(self, job_name, params):
        self.jenkins.build_job(job_name, params)

    def query_build(self, job_name):
        job = self.jenkins.get_job(job_name)
        build = job.get_last_build()
        return build

    def query_job(self, job_name):
        job = self.jenkins.get_job(job_name)
        return job
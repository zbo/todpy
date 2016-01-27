__author__ = 'bob.zhu'

from auto.generator import FeatureFileGenerator
from workspace.models import WorkSpace
from config.models import AppSetting
import os
import git
import shutil
import urllib
import httplib
import exceptions
import json

class GitRepoSaver:
    def __init__(self):
        pass

    @staticmethod
    def delete_remote_branch(branch):
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Connection": "Keep-Alive"}
        params = urllib.urlencode({'private_token': 'nc4jzpZaxnDxer4s8mL2'})
        conn = httplib.HTTPConnection("10.32.36.71")
        conn.request(method="DELETE", url="http://10.32.36.71/api/v3/projects/1/repository/branches/{0}".format(branch),
                     body=params,
                     headers=headers)
        response = conn.getresponse()
        return response

    @staticmethod
    def accept_merge_request(mr_id):
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Connection": "Keep-Alive"}
        params = urllib.urlencode({'private_token': 'nc4jzpZaxnDxer4s8mL2'})
        conn = httplib.HTTPConnection("10.32.36.71")
        conn.request(method="PUT", url="http://10.32.36.71/api/v3/projects/1/merge_request/{0}/merge".format(mr_id), body=params,
                     headers=headers)
        response = conn.getresponse()
        return response

    @staticmethod
    def create_merge_request(branch):
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Connection": "Keep-Alive"}
        params = urllib.urlencode({
            'private_token': 'nc4jzpZaxnDxer4s8mL2',
            'source_branch': branch,
            'target_branch': 'master',
            'title': 'test merge request'})
        conn = httplib.HTTPConnection("10.32.36.71")
        conn.request(method="POST", url="http://10.32.36.71/api/v3/projects/1/merge_requests", body=params,
                     headers=headers)
        response = conn.getresponse()
        resp_obj=json.loads(response.read())
        mr_id=resp_obj['id']
        return mr_id

    @staticmethod
    def update_feature_file_to_git(feature, folder_name, json_data):
        try:
            project_base = AppSetting.getSetting('projectbase')
            work_space = AppSetting.getSetting('gitlocal')
            workspace_path = os.path.join(project_base[0], work_space[0])
            git_obj = git.cmd.Git(workspace_path)
            user_folder = os.path.join(git_obj.working_dir, "todrepo", folder_name)
            feature_file_name = "{0}-{1}".format(str(feature.id),feature.name.replace(' ', '-'))
            file_path = os.path.join(user_folder, feature_file_name)
            os.remove(file_path)
            GitRepoSaver.save_feature_file_to_git(feature, folder_name, json_data)

        except exceptions:
            pass

    @staticmethod
    def save_feature_file_to_git(feature, folder_name, json_data):
        try:
            plain_text = FeatureFileGenerator.generate_feature(feature, json_data)
            project_base = AppSetting.getSetting('projectbase')
            work_space = AppSetting.getSetting('gitlocal')
            workspace_path = os.path.join(project_base[0], work_space[0])
            git_repo_address = AppSetting.getSetting("todrepo")
            git_obj = git.cmd.Git(workspace_path)
            if not os.path.exists(workspace_path):
                git_obj.clone(git_repo_address)
            git_repo = git.Repo(os.path.join(git_obj.working_dir, "todrepo"))
            # checkout branch
            new_branch = git_repo.create_head(folder_name)
            git_repo.head.reference = new_branch
            new_branch.checkout()
            user_folder = os.path.join(git_obj.working_dir, "todrepo", folder_name)
            if not os.path.exists(user_folder):
                os.mkdir(user_folder)
            feature_file_name = "{0}-{1}".format(str(feature.id),feature.name.replace(' ', '-'))
            file_path = os.path.join(user_folder, feature_file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
            file_object = open(file_path, 'a')
            for line in plain_text:
                file_object.write(line+'\r\n')
            file_object.close()
            git_repo.index.add([file_path])
            git_repo.index.commit("trigger from tod test new file")
            git_repo.git.push('--set-upstream', 'origin', folder_name)
            git_repo.git.checkout('master')
            git_repo.git.branch('-D', folder_name)
            mr_id = GitRepoSaver.create_merge_request(folder_name)
            GitRepoSaver.accept_merge_request(mr_id)
            GitRepoSaver.delete_remote_branch(folder_name)
            git_repo.remotes.origin.pull()
            pass
        except exceptions:
            print exceptions

        pass

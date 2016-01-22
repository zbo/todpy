__author__ = 'bob.zhu'
import sys
import os
import django

current_dir = path = sys.path[0]
path_len= current_dir.index('todpy')+len('todpy')
root_path=current_dir[:path_len]
web_path=os.path.join(root_path,'web')
web_web_path=os.path.join(root_path,'web/web')
tests_path=os.path.join(root_path,'tests')
workspace_path=os.path.join(root_path,'workspaces_git/git')
unittests_path=os.path.join(root_path,'tests/unittests')
sys.path.append(web_path)
sys.path.append(web_web_path)
sys.path.append(tests_path)
sys.path.append(unittests_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from config.models import AppSetting, FeatureLocation


import git
import shutil

def new_feature():
    feature_root = os.path.join(workspace_path, "todrepo")
    file_path = os.path.join(feature_root, "test.py")
    test_file = open(file_path, 'a')
    test_file.write("hello world\n")
    test_file.close()
    return file_path

def delete_feature():
    feature_root = os.path.join(workspace_path, "todrepo")
    file_path = os.path.join(feature_root, "test.py")
    os.remove(file_path)
    return file_path

def test():
    django.setup()
    if os.path.exists(workspace_path):
        shutil.rmtree(workspace_path)
    os.mkdir(workspace_path)
    git_repo_address = AppSetting.getSetting("todrepo")
    git_obj = git.cmd.Git(workspace_path)
    git_obj.clone(git_repo_address)
    git_repo = git.Repo(os.path.join(git_obj.working_dir, "todrepo"))
    # checkout branch
    new_branch = git_repo.create_head('bob-branch')
    git_repo.head.reference = new_branch
    new_branch.checkout()

    # test new file to repo
    file_path = new_feature()

    git_repo.index.add([file_path])
    git_repo.index.commit("trigger from tod test new file")
    git_repo.git.push('--set-upstream', 'origin', 'bob-branch')
    git_repo.git.checkout('master')
    git_repo.git.branch('-D', 'bob-branch')
    print 'finished'



if __name__ == '__main__':
    test()
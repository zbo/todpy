__author__ = 'bob.zhu'
import sys
import os
import django
import json
import uuid
import unittest

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
# Shell Plus Model Imports
from auto.models import Feature, Scenario, Step
from auto.dto import StepDto
from auto.saver import StepDtoPostSaver
from workspace.saver import WorkSpaceGenerater
from auto.generator import FeatureFileGenerator
from config.models import AppSetting, FeatureLocation
from workspace.models import WorkSpace
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
# Shell Plus Django Imports
from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from django.db.models import Avg, Count, F, Max, Min, Sum, Q, Prefetch
from django.core.urlresolvers import reverse
from django.db import transaction
from django.contrib import admin

import git
import shutil

def new_feature():
    feature_root = os.path.join(workspace_path, "todrepo")
    file_path = os.path.join(feature_root, "test.py")
    test_file = open(file_path, 'a')
    test_file.write("hello world\n")
    test_file.close()
    return file_path

def update_feature():
    pass

def test():
    django.setup()
    if os.path.exists(workspace_path):
        shutil.rmtree(workspace_path)
    os.mkdir(workspace_path)
    git_repo_address = AppSetting.getSetting("todrepo")
    git_obj = git.cmd.Git(workspace_path)
    git_obj.clone(git_repo_address)
    file_path = new_feature()
    git_repo = git.Repo(os.path.join(git_obj.working_dir, "todrepo"))
    git_repo.index.add([file_path])
    git_repo.index.commit("trigger from tod test")
    origin = git_repo.remote('origin')
    origin.push()
    return ''


if __name__ == '__main__':
    test()

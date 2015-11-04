from django.db import models

import sys
import os
import shutil
sys.path.append('../')
sys.path.append('../../') # Create your models here.
from config.models import AppSetting, FeatureLocation

class WorkSpace(models.Model):
    type=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    rootlocation=models.CharField(max_length=755)
    createat=models.DateTimeField(auto_now_add=True)
    updateat=models.DateTimeField(auto_now=True)

    def fill(self, type, name, rootlocation):
        self.type = type.lower()
        self.name = name
        self.rootlocation = rootlocation

    def generate_ws_folder(self):
        folder_path = self.getFolderPath()
        os.makedirs(folder_path)
        return folder_path

    def getFolderPath(self):
        project_base = AppSetting.getSetting('projectbase')
        work_space = AppSetting.getSetting('workspace')
        folder_path = project_base[0] + work_space[0] + '/' + str(self.rootlocation)
        return folder_path

    def move_lib_folders(self):
        lib_path = []
        all = FeatureLocation.getLocation(self.type)
        for item in all:
            source_folder = AppSetting.getSetting('projectbase')[0] + item
            shutil.copytree(source_folder, self.getFolderPath()+'/'+str(self.type))
            lib_path.append(item)
        return lib_path


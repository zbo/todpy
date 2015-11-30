__author__ = 'bob.zhu'
import models
import shutil
import os
import pdb
import json
class FeatureFileGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_feature(feature, json_str):
        plain_text = []
        feature_description= feature.description
        feature_name = feature.name
        json_obj = json.loads(json_str)
        plain_text.append("Feature: {0}".format(feature_name))
        plain_text.append("  {0}".format(feature_description))
        scenarios = json_obj['feature']['scenarios']
        for sce in scenarios:
            plain_text.append("  Scenario: {0}".format(sce['scenario_name']))
            for s1 in sce['steps']:
                step_data=s1[s1.keys()[0]]
                plain_text.append("    {0} {1}".format(step_data['action_type'],step_data['description']))
        return plain_text

    @staticmethod
    def save_feature_file(feature, workspace, json_data):
        plain_text = FeatureFileGenerator.generate_feature(feature, json_data)
        base_location = workspace.getFolderPath()
        feature_file_name = "{0}-{1}".format(str(feature.id),feature.name.replace(' ','-'))
        file_path = "{0}/{1}/features/{2}.feature".format(base_location,workspace.type,feature_file_name)
        file_object = open(file_path, 'a')
        for line in plain_text:
            file_object.write(line+'\r\n')
        file_object.close()
        workspace.entrance = feature_file_name
        workspace.save()
        return feature_file_name
        #print file_path

    @staticmethod
    def update_feature_file(feature, workspace, json_data):
        base_location = workspace.getFolderPath()
        # [bob] here feature have been updated, so name can not be use, but workspace entrance still keep the file name
        feature_file_name = workspace.entrance
        file_path = "{0}/{1}/features/{2}.feature".format(base_location,workspace.type,feature_file_name)
        # [bob] workspace entrance name will be updated by save_feature_file
        if os.path.isfile(file_path):
            os.remove(file_path)
        FeatureFileGenerator.save_feature_file(feature,workspace,json_data)
        pass




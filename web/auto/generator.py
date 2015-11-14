__author__ = 'bob.zhu'
import models
import shutil
import os
import pdb
class FeatureFileGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_feature(feature):
        plain_text = []
        feature_description= feature.description
        feature_name = feature.name

        plain_text.append("Feature: {0}".format(feature_name))
        plain_text.append("  {0}".format(feature_description))
        for scenario in feature.scenario_set.filter(deleted=0):
            plain_text.append("  Scenario: {0}".format(scenario.description))
            sequence = scenario.step_sequence
            sequence = sequence[0:len(sequence)-1]
            sequence_array = sequence.split('|')
            for id in sequence_array:
                step = models.Step.objects.get(pk=id)
                plain_text.append("    {0} {1}".format(step.action_type,step.description_with_agrs))
        return plain_text

    @staticmethod
    def save_feature_file(feature, workspace):
        plain_text = FeatureFileGenerator.generate_feature(feature)
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
    def update_feature_file(feature, workspace):
        base_location = workspace.getFolderPath()
        # [bob] here feature have been updated, so name can not be use, but workspace entrance still keep the file name
        feature_file_name = workspace.entrance
        file_path = "{0}/{1}/features/{2}.feature".format(base_location,workspace.type,feature_file_name)
        # [bob] workspace entrance name will be updated by save_feature_file
        if os.path.isfile(file_path):
            os.remove(file_path)
        FeatureFileGenerator.save_feature_file(feature,workspace)
        pass




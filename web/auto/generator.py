__author__ = 'bob.zhu'
import models
import pdb
class FeatureFileGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_feature(feature):
        plain_text = []
        feature_description= feature.description
        feature_file_name = "{0}-{1}".format(str(feature.id),feature_description.replace(' ','-'))
        plain_text.append("Feature: {0}".format(feature_description))
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

        file_path = "{0}/{1}/features/{2}.feature".format(base_location,workspace.type,feature.name.replace(' ','-'))
        file_object = open(file_path, 'a')
        for line in plain_text:
            file_object.write(line+'\r\n')
        file_object.close()
        print file_path




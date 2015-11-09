__author__ = 'bob.zhu'
import models
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

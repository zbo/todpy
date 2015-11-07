__author__ = 'bob.zhu'

class FeatureFileGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_feature(feature):
        plain_text = []
        feature_description= feature.description
        feature_file_name = "{0}-{1}".format(str(feature.id),feature_description.replace(' ','-'))
        plain_text.append("Feature: {0}".format(feature_description))
        for scenario in feature.scenario_set.all():
            plain_text.append("  Scenario: {0}".format(scenario.description))
        return plain_text

__author__ = 'bob.zhu'
from auto.models import Feature, Scenario, Step


def assert_all(instance, feature):
    instance.assertEqual(feature.name, 'test okcoin user reg form')
    instance.assertEqual(feature.description, 'just for test')
    # instance.assertEqual(feature.scenario_set.count(), 3)
    # instance.assertEqual(feature.scenario_set.first().step_sequence, '1|7|3|8|9|10|11|12|13|4|')
    # instance.assertEqual(feature.scenario_set.get(id=2).step_sequence, '5|6|')
    # instance.assertEqual(feature.scenario_set.get(id=3).step_sequence, '14|15|16|')
    # instance.assertEqual(feature.scenario_set.first().deleted, 0)
    # instance.assertEqual(feature.scenario_set.get(id=2).deleted, 1)
    # instance.assertEqual(feature.scenario_set.get(id=3).deleted, 0)
    # instance.assertEqual(Step.objects.get(pk=1).deleted, 0)
    # instance.assertEqual(Step.objects.get(pk=2).deleted, 1)
    # instance.assertEqual(Step.objects.get(pk=3).deleted, 0)
    # instance.assertEqual(Step.objects.get(pk=4).deleted, 0)
    # instance.assertEqual(Step.objects.get(pk=5).deleted, 1)
    # instance.assertEqual(Step.objects.get(pk=6).deleted, 1)
    # instance.assertEqual(Step.objects.get(pk=7).deleted, 0)
    # instance.assertEqual(Step.objects.get(pk=3).description_with_agrs, "I click element with text 'Trade'")

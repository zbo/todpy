__author__ = 'bob.zhu'

def assert_all(instance, feature):
    instance.assertEqual(feature.name,'change name feature name')
    instance.assertEqual(feature.description,'not fun now')
    instance.assertEqual(feature.scenario_set.count(),3)
    instance.assertEqual(feature.scenario_set.first().step_sequence,'1|7|3|4|')
    instance.assertEqual(feature.scenario_set.get(id=2).step_sequence,'5|6|')
    instance.assertEqual(feature.scenario_set.get(id=3).step_sequence,'8|9|')
    instance.assertEqual(feature.scenario_set.first().deleted,0)
    instance.assertEqual(feature.scenario_set.get(id=2).deleted,1)
    instance.assertEqual(feature.scenario_set.get(id=3).deleted,0)
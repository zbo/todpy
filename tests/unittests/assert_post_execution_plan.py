__author__ = 'bob.zhu'

def assert_all(instance, result, feature):
    instance.assertEqual(result, 'ok')
    instance.assertEqual(feature.executionLock, True)

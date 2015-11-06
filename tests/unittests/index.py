#!/usr/bin/env python 
# encoding: utf-8
import unittest
import sys
import os
import django
import json
import uuid
sys.path.append('../../web')
sys.path.append('../')
sys.path.append('../../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
from config.models import AppSetting, FeatureLocation



class app_setting_tests(unittest.TestCase):
    def setUp(self):
        django.setup()
        # import tool_clear_workspace
        # tool_clear_workspace.do()
        # import tool_reset_db
        # tool_reset_db.do()

    def tearDown(self):
        pass

    def test_aa_app_setting(self):
        results= AppSetting.getSetting('workspace')
        self.assertEqual(len(results),1)
        self.assertEqual(results[0],'workspaces')

    def test_ab_gen_workspace(self):
        import test_gen_workspace
        test_gen_workspace.test()

    def test_ac_step_dto(self):
        import test_step_dto
        test_step_dto.test()

    def test_ad_step_dto_post_save(self):
        import test_step_dto_post_save
        result = test_step_dto_post_save.test()
        all_steps = result.scenario_set.all().first().step_set.all()
        sequence_text = ''
        for s in all_steps:
            sequence_text += str(s.id) + '|'
        self.assertEquals(sequence_text, result.scenario_set.all().first().step_sequence)

    def test_ba_get_all_by_feature(self):
        import test_get_all_by_feature
        test_get_all_by_feature.test()

    def test_bb_update_all_by_feature(self):
        import test_update_all_by_feature
        feature = test_update_all_by_feature.test()
        self.assertEqual(feature.name,'change name feature name')
        self.assertEqual(feature.description,'not fun now')
        self.assertEqual(feature.scenario_set.count(),3)
        self.assertEqual(feature.scenario_set.first().step_sequence,'1|7|3|4|')
        self.assertEqual(feature.scenario_set.get(id=2).step_sequence,'5|6|')
        self.assertEqual(feature.scenario_set.get(id=3).step_sequence,'8|9|')

if __name__ == '__main__':
    unittest.main()

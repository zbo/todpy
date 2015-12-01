#!/usr/bin/env python 
# encoding: utf-8
import unittest
import sys
import os
import django
import json
import uuid
current_dir = path = sys.path[0]
path_len= current_dir.index('todpy')+len('todpy')
root_path=current_dir[:path_len]
web_path=os.path.join(root_path,'web')
web_web_path=os.path.join(root_path,'web/web')
tests_path=os.path.join(root_path,'tests')
unittests_path=os.path.join(root_path,'tests/unittests')
sys.path.append(web_path)
sys.path.append(web_web_path)
sys.path.append(tests_path)
sys.path.append(unittests_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from config.models import AppSetting, FeatureLocation
from auto.models import Feature
import tool_reset_db
tool_reset_db.do()




class app_setting_tests(unittest.TestCase):
    def setUp(self):
        django.setup()

    def tearDown(self):
        pass

    def test_aa_app_setting(self):
        print '.'*20+'test_aa_app_setting'+'.'*20
        results= AppSetting.getSetting('workspace')
        self.assertEqual(len(results),1)
        self.assertEqual(results[0],'workspaces')

    @unittest.skip("covered by others")
    def test_ab_gen_workspace(self):
        print '.'*20+'test_ab_gen_workspace'+'.'*20
        from unittest import test_gen_workspace
        test_gen_workspace.test()

    def test_ac_step_dto(self):
        print '.'*20+'test_ac_step_dto'+'.'*20
        import test_step_dto
        result = test_step_dto.test()
        json.dumps(result, cls=test_step_dto.DateEncoder)

    def test_ad_step_dto_post_save(self):
        print '.'*20+'test_ad_step_dto_post_save'+'.'*20
        import test_step_dto_post_save
        result = test_step_dto_post_save.test()
        all_steps = result.scenario_set.all().first().step_set.all()
        sequence_text = ''
        for s in all_steps:
            sequence_text += str(s.id) + '|'
        self.assertEquals(sequence_text, result.scenario_set.all().first().step_sequence)

    def test_ba_get_all_by_feature(self):
        print '.'*20+'test_ba_get_all_by_feature'+'.'*20
        import test_get_all_by_feature
        import assert_get_all_by_feature
        json_data = test_get_all_by_feature.test()
        assert_get_all_by_feature.assert_before_update(self,json_data)

    def test_bb_update_all_by_feature(self):
        print '.'*20+'test_bb_update_all_by_feature'+'.'*20
        import test_update_all_by_feature
        import assert_update_feature
        feature = test_update_all_by_feature.test()
        assert_update_feature.assert_all(self, feature)

    @unittest.skip("covered by others")
    def test_bc_feature_file_generator(self):
        print '.'*20+'test_bc_feature_file_generator'+'.'*20
        import test_feature_file_generator
        import assert_feature_file
        result = test_feature_file_generator.test()
        assert_feature_file.assert_gen_file(self, result)

    @unittest.skip("save time")
    def test_be_execute_sample(self):
        print '.'*20+'test_bd_execute_sample'+'.'*20
        import test_execute_sample
        result = test_execute_sample.test()

    @unittest.skip("covered by others")
    def test_bf_post_execution_plan(self):
        print '.'*20+'test_bf_execution_plan'+'.'*20
        import test_post_exe_plan
        import assert_post_execution_plan
        result, feature_id = test_post_exe_plan.test()
        feature = Feature.objects.get(pk=feature_id)
        assert_post_execution_plan.assert_all(self, result, feature)




if __name__ == '__main__':
    unittest.main()

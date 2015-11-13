__author__ = 'bob.zhu'
import json
from models import Feature, Scenario, Step
from workspace.models import WorkSpace
import pdb


class CommonSaver:
    def __init__(self):
        pass

    def replace_u(self, str_in):
        tmp = '['
        for s in str_in:
            tmp += s + ','
        return tmp[0:len(tmp) - 1] + ']'

    def update_sequence(self, scenario, sequence):
        scenario.set_sequence(sequence)
        scenario.save()

    def save_new_step(self, sce_save, step):
        step = step[step.keys()[0]]
        step_save = Step().fill(sce_save, step['step_name'], step['co_name'], step['co_file_name'],
                                step['co_firstlineno'], step['co_argcount'],
                                self.replace_u(step['co_varnames']), step['description'], step['action_type'], 
                                json.dumps(step['co_variables']))
        step_save.save()
        return step_save

    def save_new_scenario(self, feature_save, sce):
        sequence = ''
        sce_save = Scenario().fill(feature_save, sce['scenario_name'], '')
        sce_save.save()
        steps = sce['steps']
        for step in steps:
            step_save = self.save_new_step(sce_save, step)
            sequence += str(step_save.id) + '|'
        self.update_sequence(sce_save, sequence)
        return sce_save

    def update_existing_scenario(self, feature_update, sce_update, sce_exist):
        sequence = ''
        sce_exist.fill(feature_update, sce_update['scenario_name'], '')
        sce_exist.save()
        steps = sce_update['steps']
        updated = []
        newed = []
        for step in steps:
            step_id = step.keys()[0]

            if str(step_id).lower() == 'new':
                step_saved = self.save_new_step(sce_exist, step)
                sequence += str(step_saved.id) + '|'
                newed.append(step_saved.id)
            else:
                step_existed = self.update_exist_step(sce_exist, step)
                sequence += str(step_id) + '|'
                updated.append(step_existed.id)
        self.update_sequence(sce_exist, sequence)
        self.mark_deleted_steps(sce_exist, updated, newed)

    def mark_deleted_steps(self, scenario, updated_steps, newed_steps):
        #pdb.set_trace()
        for step in scenario.step_set.all():
            if step.id in updated_steps or step.id in newed_steps:
                continue
            else:
                step.deleted = True;
                step.save()

    def update_exist_step(self, sce_exist, step):
        step_id = step.keys()[0]
        step = step[step.keys()[0]]
        step_exist = Step.objects.get(pk=step_id)
        step_exist.fill(sce_exist, step['step_name'], step['co_name'], step['co_file_name'],
                        step['co_firstlineno'], step['co_argcount'],
                        self.replace_u(step['co_varnames']), step['description'], step['action_type'], 
                        json.dumps(step['co_variables']))
        step_exist.save()
        return step_exist


class StepDtoPostSaver:
    def __init__(self):
        self.CommonSaver = CommonSaver()

    def save(self, json_str):
        json_obj = json.loads(json_str)
        feature_name = json_obj['feature']['feature_name']
        feature_desc = json_obj['feature']['feature_description']
        feature_save = Feature().fill(feature_name, feature_desc, '', '')
        feature_save.save()
        scenarios = json_obj['feature']['scenarios']
        for sce in scenarios:
            self.CommonSaver.save_new_scenario(feature_save, sce)
        return feature_save


class StepDtoPostUpdater:
    def __init__(self):
        self.CommonSaver = CommonSaver()

    def update(self, json_str):
        json_obj = json.loads(json_str)
        feature_name = json_obj['feature']['feature_name']
        feature_desc = json_obj['feature']['feature_description']
        feature_id = json_obj['feature']['feature_id']
        feature_update = Feature.objects.get(id=feature_id)
        workspace_id = feature_update.workspace
        workspace = WorkSpace.objects.get(id=workspace_id)
        feature_update.fill(feature_name, feature_desc, '', '')
        feature_update.update_workspace(workspace)

        feature_update.save()
        scenarios = json_obj['feature']['scenarios']
        updated = []
        newed = []
        for sce in scenarios:
            scenario_id = sce['scenario_id']
            if str(scenario_id).lower() == 'new':
                sce_saved = self.CommonSaver.save_new_scenario(feature_update, sce)
                newed.append(sce_saved.id)
            else:
                updated.append(scenario_id)
                scenario_exist = Scenario.objects.get(id=scenario_id)
                self.CommonSaver.update_existing_scenario(feature_update, sce, scenario_exist)
        self.mark_delete_scenarios(feature_update, updated, newed)
        return feature_update

    def mark_delete_scenarios(self, feature, scenario_updated, newed):
        for scenario in feature.scenario_set.all():
            if scenario.id in scenario_updated or scenario.id in newed:
                continue
            else:
                scenario.deleted=True
                scenario.save()
                for step in scenario.step_set.all():
                    step.deleted = True
                    step.save()
        pass

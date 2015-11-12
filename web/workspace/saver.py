__author__ = 'bob.zhu'
from models import WorkSpace
from auto.models import Feature
import uuid

class WorkSpaceGenerater:

    @staticmethod
    def gen_workspace(type):
        workspace = WorkSpace()
        workspace_root = uuid.uuid4()
        workspace.fill(type, 'test-work-space', workspace_root)
        root_path = workspace.generate_ws_folder()
        lib_path = workspace.move_lib_folders()
        workspace.save()
        return workspace

class ExecutionPlanSaver:

    @staticmethod
    def save_execution_plan(feature_id):
        feature = Feature.objects.get(pk=feature_id)
        if feature.executionLock:
            return "execution already started"
        else:
            feature.lock_feature()
            return "ok"

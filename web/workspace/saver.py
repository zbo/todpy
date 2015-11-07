__author__ = 'bob.zhu'
from models import WorkSpace
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
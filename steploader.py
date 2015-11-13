import sys

sys.path.append("..")
import lettuce
import copy


class StepMeta:
    def __init__(self):
        self.STEP_REGISTRY = []
        self.CALLBACK_REGISTRY = []


def clear_global(m):
    m.STEP_REGISTRY.clear()
    m.CALLBACK_REGISTRY.clear()


def load_steps(base_path):
    filesystem = lettuce.fs.FileSystem
    all = []
    files = filesystem.locate(base_path, '*.py')
    for filename in files:
        root = filesystem.dirname(filename)
        sys.path.insert(0, root)
        to_load = filesystem.filename(filename, with_extension=False)
        try:
            module = __import__(to_load)
        except ValueError as e:
            import traceback

            err_msg = traceback.format_exc(e)
            if 'empty module name' in err_msg.lower():
                continue
            else:
                e.args = ('{0} when importing {1}'.format(e, filename)),
                raise e

        reload(module)  # always take fresh meat :)
        step_meta = StepMeta()
        if hasattr(module, "STEP_REGISTRY"):
            step_meta.STEP_REGISTRY = copy.deepcopy(module.STEP_REGISTRY)
            step_meta.CALLBACK_REGISTRY = copy.deepcopy(module.CALLBACK_REGISTRY)
            all.append(step_meta)
            clear_global(module)
        sys.path.remove(root)
    return all

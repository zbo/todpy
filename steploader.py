import sys
sys.path.append("..")
import lettuce

def load_steps(base_path):
    filesystem = lettuce.fs.FileSystem
    all=[]
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
        all.append(module)
        sys.path.remove(root)
    return all



from steploader import load_steps

__author__ = 'bob.zhu'
import lettuce


base_path='../simple-selenium'
tags=None
l_runner = lettuce.Runner(
        base_path=base_path
    )
modules = load_steps(base_path)

for i in range(len(modules)):
    print modules[i].STEP_REGISTRY


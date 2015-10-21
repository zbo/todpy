from steploader import load_setps

__author__ = 'bob.zhu'
import lettuce


base_path='../simple-selenium'
tags=None
l_runner = lettuce.Runner(
        base_path=base_path
    )


# [file can be loaded]
# ffs=l_runner.loader.find_feature_files()
load_setps()

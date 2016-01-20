__author__ = "ian.zhang"

import sys
import os
import django

sys.path.append('../web/')
sys.path.append('../web/web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from auto.models import Project


def test():
    django.setup()
    project = Project().fill('Test on demand', 'TOD', 'TOD is a system that can do automation on demand and test on demand')
    result = project.save()
    print project.__dict__
    return result

if __name__ == '__main__':
    test()
__author__ = "ian.zhang"

import sys
import os
import django

sys.path.append('../web/')
sys.path.append('../web/web/')
sys.path.append('../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from auto.models import Project, TestSuite

def test():
    django.setup()
    _project = Project.objects.get(id=1)

    root_testsuite = TestSuite().fill(name="tod", description="tod features", project=_project, parent_id=-1, level=0)
    root_testsuite.save()
    level1_testsuite = TestSuite().fill(name="login", description="login features", project=_project, parent_id=root_testsuite.__dict__.get('id'), level=(root_testsuite.level+1))
    level1_testsuite.save()
    pass




__author__ = 'bob.zhu'
import os

cmd = 'lettuce ../workspaces/01'
# print '-' * 30 + 'popen'
# tmp = os.popen(cmd, 'r', 100).readlines()
# print tmp

import subprocess
# p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# for line in p.stdout.readlines():
#     print line
#
# retval = p.wait()

subprocess.call([cmd, "arg1", "arg2"], shell=True)

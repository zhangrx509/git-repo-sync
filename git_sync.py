#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys
import os
import subprocess
import re

if len(sys.argv) != 4:
    print('''Usage:
    git_sync.py <repo_root_path> <source_remote> <destination_remote>''')
    quit()

repo_root_path = sys.argv[1]
src_remote = sys.argv[2]
des_remote = sys.argv[3]

#change dir to git repo
old_dir = os.getcwd()
os.chdir(repo_root_path)

pout = subprocess.check_output('git branch --all', shell=True)  
brs = pout.split('\n')

for br in brs:
    secs = br.split('/')
    if re.search(r'remotes', secs[0]):
        if (re.match(r'HEAD', secs[2]) == None) and re.match(src_remote, secs[1]):
            print(secs[2])
            subprocess.call('git checkout {0}'.format(secs[2]), shell=True)
            subprocess.call('git pull {0} {1}'.format(src_remote, secs[2]), shell=True)
            subprocess.call('git push {0} {1}'.format(des_remote, secs[2]), shell=True)


subprocess.call('git fetch {0} --tags'.format(src_remote), shell=True)
subprocess.call('git push {0} --tags'.format(des_remote), shell=True)


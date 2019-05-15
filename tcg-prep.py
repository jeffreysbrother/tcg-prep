#!/usr/local/bin/python
import os
from sys import argv
from git import Repo
import tcgPrepConfig


# reload vagrant unless "--skip-vagrant" argument exists
if ('--skip-vagrant' not in argv):
    os.chdir(tcgPrepConfig.tf)
    os.system("vagrant reload")


# checkout master branch if branch is in a detached head state (caused by 'vagrant reload')
for item in tcgPrepConfig.directoryList:
    itemRepo = Repo(item[1])
    if itemRepo.head.is_detached:
        print(item[0] + " repo: detached head state. Checking out master!")
        itemRepo.git.checkout('master')
    else:
        print(item[0] + " repo: " + itemRepo.active_branch.name + " branch.")


# copy production site config to local only if "--copy-configs" argument exists
if ('--copy-configs' in argv):
    for file in tcgPrepConfig.siteConfigFiles:
        with open(file[0]) as f:
            with open(file[1], "w") as f1:
                for line in f:
                    f1.write(line)

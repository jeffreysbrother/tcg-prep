import os
from sys import argv
from git import Repo

tf = "/Users/jamescool/vagrants/public-records/sites/public-records-app/public/truthfinder.com/funnel"
icm = "/Users/jamescool/vagrants/public-records/sites/public-records-app/public/instantcheckmate.com/funnel"
pubrec = "/Users/jamescool/vagrants/public-records/sites/public-records-app"
config = "/Users/jamescool/vagrants/public-records/sites/public-records-site-configs"
dsc = "/Users/jamescool/vagrants/public-records/sites/public-records-app/vendor/tcg/data-service-client-v2"

directoryList = [
    ['TF', tf],
    ['ICM', icm],
    ['PUBREC', pubrec],
    ['CONFIG', config],
    ['DATA SERVICE CLIENT', dsc]
]

# reload vagrant unless "--skip-vagrant" argument exists
if ('--skip-vagrant' not in argv):
    os.chdir(tf)
    os.system("vagrant reload")


# checkout master branch if branch is in a detached head state (caused by 'vagrant reload')
for item in directoryList:
    itemRepo = Repo(item[1])
    if itemRepo.head.is_detached:
        print(item[0] + " repo: detached head state. Checking out master!")
        itemRepo.git.checkout('master')
    else:
        print(item[0] + " repo: " + itemRepo.active_branch.name + " branch.")


# copy production site config to local only if "--copy-configs" argument exists
if ('--copy-configs' in argv):
    siteConfigFiles = [
        [
            "/Users/jamescool/vagrants/public-records/sites/public-records-site-configs/truthfinder.com.json",
            "/Users/jamescool/vagrants/public-records/sites/public-records-site-configs/truthfinder.app.public-records.local.tcg.io.json"
        ],
        [
            "/Users/jamescool/vagrants/public-records/sites/public-records-site-configs/instantcheckmate.com.json",
            "/Users/jamescool/vagrants/public-records/sites/public-records-site-configs/instantcheckmate.app.public-records.local.tcg.io.json"
        ]
    ]

    for file in siteConfigFiles:
        with open(file[0]) as f:
            with open(file[1], "w") as f1:
                for line in f:
                    f1.write(line)

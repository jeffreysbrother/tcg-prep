# TCG Prep

Reload Vagrant, ensure that all relevant repos are not in a detached head state (a common side effect of reloading Vagrant), and copy production site configs to your local site configs.

### Installation

Make sure you have Python and pip installed:

```
python -V
```

```
pip -V
```

Install gitpython:

```
sudo pip install GitPython
```

create a module called `tcgPrepConfig.py` and populate it like this:

```
tf = "/path/to/tf/repo"
icm = "/path/to/icm/repo"
pubrec = "/path/to/pubrec/repo"
config = "/path/to/config/repo"
dsc = "/path/to/dsc/repo"

directoryList = [
    ['TF', tf],
    ['ICM', icm],
    ['PUBREC', pubrec],
    ['CONFIG', config],
    ['DATA SERVICE CLIENT', dsc]
]

siteConfigFiles = [
    [
        "/path/to/tf/production/config.json",
        "/path/to/tf/local/config.json"
    ],
    [
        "/path/to/icm/production/config.json",
        "/path/to/icm/local/config.json"
    ]
]
```

### Using the tool

Running `python tcg-prep.py` will reload Vagrant and ensure that no repo is in a detached head state.

Add the `--copy-configs` argument to ensure that your local site configs match the production ones.

Add the `--skip-vagrant` argument if you do not wish to restart Vagrant.

### Misc

Since you are not me, you'll have to update `directoryList` and `siteConfigFiles` to reflect the repos and config files you commonly use.
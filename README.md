# TCG Prep

This script automates the following tasks:

* Reload Vagrant
* Checkout previous branch if in a detached head state (a common side effect of reloading Vagrant)
* Pull origin if behind
* Copy production site configs to local site configs

### Installation

Make sure you have Python and pip installed:

```
python -V
```

```
pip -V
```

Install GitPython:

```
sudo pip install gitpython
```

In your .bashrc or .zshrc file, add something like this (you might need slightly different formatting for bash):

```
export PATH="/path/to/cloned/repo:$PATH"
```

Run this command in the repo you just cloned in order to make the script executable:

```
chmod +x tcg-prep
```

Create a file called `config.py` alongside `tcg-prep` and populate it like this, making sure to update all paths to reflect their location on your local machine:

```py
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
        "/path/to/tf-production-config.json",
        "/path/to/tf-local-config.json"
    ],
    [
        "/path/to/icm-production-config.json",
        "/path/to/icm-local-config.json"
    ]
]
```

### Using the tool

Running `tcg-prep` will reload Vagrant and ensure that no repo is in a detached head state.

Add the `--copy-configs` argument to copy the contents of the production site configs to the local ones.

Add the `--skip-vagrant` argument to skip the *vagrant reload* command.

### Output

If the command `tcg-prep --copy-configs` is executed, you should see something like the following (once Vagrant is finally reloaded):

```
TF: detached head state. Checking out master.
>>> TF master branch is behind origin. Pulling.
ICM: master branch.
PUBREC: detached head state. Checking out master.
>>> PUBREC master branch is behind origin. Pulling.
CONFIG: master branch.
DATA SERVICE CLIENT: master branch.
----------------
tf-production-config.json copied to local site config.
icm-production-config.json copied to local site config.
```

### Issues

If the program will not run, you might need to modify the first line of `tcg-prep` to reflect the proper location and version of the Python interpreter.
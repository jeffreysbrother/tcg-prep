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

Running `tcg-prep` will reload Vagrant and ensure that no repo is in a detached head state.

Add the `--copy-configs` argument to ensure that your local site configs match the production ones.

Add the `--skip-vagrant` argument if you do not wish to restart Vagrant.

### Issues

If the program will not run, you might need to modify the first line of `tcg-prep` to reflect the proper location and version of the Python interpreter.
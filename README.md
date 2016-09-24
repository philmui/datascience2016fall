# "datascience" class repo

This is a repo for the SCU Data Science with Python class.

## Prerequisites
We assume that you have a Python 2.7 environment supporting Enthought's
venv backward port to Python 2.7.

To install all prerequisites with venv, type:

```
venv dsenv
source dsenv/bin/activate
pip install -r requirements.txt
```

If you are using Anaconda or generic Python's virtualenv, type:

```
virtualenv dsenv
source dsenv/bin/activate
pip install -r requirements.txt
```


## Configurations
Many of the projects here assume the existence of configuration files
which should be in the toplevel directory "cfg".  This is not checked
into github -- as these configuration files likely contain secrets
(key pairs, magic numbers, etc.) which should be private to each
client install.

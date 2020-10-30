# Python project for database restoration of a Mongo database.
# Classification (U)

# Description:
  Database restoration program to restore Mongo database.


###  This README file is broken down into the following sections:
  * Features
  * Prerequisites
  * Installation
  * Configuration
  * Program Help Function
  * Testing
    - Unit


# Features
  * Restore an individual Mongo database dumped by the mongodump program.

# Prerequisites:

  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - lib/cmds_gen
    - lib/arg_parser
    - lib/gen_libs
    - mongo_lib/mongo_class
    - mongo_lib/mongo_libs


# Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-db-restore.git
```

Install/upgrade system modules.

```
cd mongo-db-restore
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create Mongodb configuration file.

```
cd config
cp mongo.py.TEMPLATE mongo.py
```

Make the appropriate change to the environment.
  * Make the appropriate changes to connect to a Mongo database.
    - user = "USER"
    - japd = "PWORD"
    - host = "IP_ADDRESS"
    - name = "HOSTNAME"
    - port = 27017
      -> Default port for Mongo database.
    - conf_file = None
      -> Only set if using a different Mongo configuration file.
    - auth = True
      -> Only set to False if no authentication is taking place.
    - auth_db = "admin"
      -> Name of database to authenticate the user in.
    - use_arg = True
      -> Type of connection format using parameter based.
      -> Recommended choice.
      -> Do not change unless you know the Mongo library modules.
    - use_uri = False
      -> Type of connection format using url command line.
      -> Do not change unless you know the Mongo library modules.

```
vim mongo.py
chmod 600 mongo.py
```


# Program Help Function:

  The program has a -h (Help option) that will show display an usage message.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
{Python_Project}mongo-db-restore/mongo_db_restore.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install these programs using git.
  * Replace **{Python_Project}** with the baseline path of the python program.
  * Replace **{Branch_Name}** with the name of the Git branch being tested.  See Git Merge Request.

```
umask 022
cd {Python_Project}
git clone --branch {Branch_Name} git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/mongo-db-restore.git
```

Install/upgrade system modules.

```
cd mongo-db-restore
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-mongo-lib.txt --target mongo_lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-python-lib.txt --target mongo_lib/lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


### Testing:
  * Replace **{Python_Project}** with the baseline path of the python program.

```
cd {Python_Project}/mongo-db-restore
test/unit/mongo_db_restore/unit_test_run.sh
```

### Code Coverage:
```
cd {Python_Project}/mongo-db-restore
test/unit/mongo_db_restore/code_coverage.sh
```


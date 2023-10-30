# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.0.3] - 2023-10-19
- Upgrade python-lib to v2.10.1
- Upgrade mongo-libs to v4.2.7
- Replaced the arg_parser code with gen_class.ArgParser code.
- Updated to work in Python 3 too

### Changed
- Converted imports to use Python 2.7 or Python 3.
- Multiple functions: Replaced the arg_parser code with gen_class.ArgParser code.
- main, single_db: Removed gen_libs.get_inst call.
- Documentation updates.


## [0.0.2] - 2021-12-22
- Upgrade mongo-libs to v4.2.1
- Upgrade python-lib to v2.9.2

### Changed
- run_program:  Replaced cmds_gen.disconnect with mongo_libs.connect.
- config/mongo.py.TEMPLATE:  Added SSL, authenication method, and replica set entries and removed old entries.
- Documentation updates.

### Removed
- cmds_gen module

## [0.0.1] - 2020-10-29
- Initial creation.
- Restoring a single database using a dump from a mongodump command.


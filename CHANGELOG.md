# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.1.1] - 2025-03-11
- Updated mongo-libs to v4.5.1

### Fixed
- Fixed pre-header where to determine which python version to use.


## [0.1.0] - 2025-02-28
Alpha release

- Add pre-header check on allowable Python versions to run.
- Added pymongo==4.10.1 for Python 3.9 and Python 3.12.
- Added dnspython==2.7.0 for Python 3.9 and Python 3.12.
- Removed support for Python 2.7.
- Updated python-lib v4.0.0
- Updated mongo-lib v4.5.0

### Added
- Support for Mongo 7.0

### Changed
- single_db: Replaced dict() with {} and list() with [].
- main, run_program: Converted strings to f-strings.
- Documentation changes.

### Removed
- Support for Mongo 3.4


## [0.0.8] - 2024-11-22
- Updated distro==1.9.0 for Python 3
- Updated psutil==5.9.4 for Python 3
- Updated python-lib to v3.0.8
- Updated mongo-lib to v4.3.4

### Deprecated
- Support for Python 2.7


## [0.0.7] - 2024-09-27
- Updated pymongo==4.1.1 for Python 3.6
- Updated simplejson==3.13.2 for Python 3
- Updated mongo-lib to v4.3.2
- Updated python-lib to v3.0.5


## [0.0.6] - 2024-09-10

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [0.0.5] - 2024-04-23
- Updated mongo-lib to v4.3.0
- Added TLS capability
- Set pymongo to 3.12.3 for Python 2 and Python 3.

### Changed
- Set pymongo to 3.12.3 for Python 2 and Python 3.
- config/mongo.py.TEMPLATE: Added TLS entries.
- Documentation updates.


## [0.0.4] - 2024-02-29
- Updated to work in Red Hat 8
- Updated mongo-lib to v4.2.9
- Updated python-lib to v3.0.3

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [0.0.3] - 2023-10-19
- Upgrade python-lib to v2.10.1
- Upgrade mongo-libs to v4.2.7
- Replaced the arg_parser code with gen_class.ArgParser code.
- Updated to work in Python 3 too

### Changed
- single_db: Update arguments to mongo_libs.create_cmd call.
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


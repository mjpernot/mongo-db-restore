#!/bin/bash
# Unit testing program for the program module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit testing..."
/usr/bin/python3 test/unit/mongo_db_restore/help_message.py
/usr/bin/python3 test/unit/mongo_db_restore/main.py
/usr/bin/python3 test/unit/mongo_db_restore/run_program.py
/usr/bin/python3 test/unit/mongo_db_restore/single_db.py

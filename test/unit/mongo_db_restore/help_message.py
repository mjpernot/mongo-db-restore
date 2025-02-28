#!/usr/bin/python
# Classification (U)

"""Program:  help_message.py

    Description:  Unit testing of help_message in mongo_db_restore.py.

    Usage:
        test/unit/mongo_db_restore/help_message.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mongo_db_restore                         # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        test_help_message

    """

    def test_help_message(self):

        """Function:  test_help_message

        Description:  Test help_message function.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_restore.help_message())


if __name__ == "__main__":
    unittest.main()

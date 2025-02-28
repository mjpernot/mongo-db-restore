#!/usr/bin/python
# Classification (U)

"""Program:  single_db.py

    Description:  Unit testing of single_db in mongo_db_restore.py.

    Usage:
        test/unit/mongo_db_restore/single_db.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_restore                         # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "rabbitmq", "-d": "config"}


class SubProcess():                                     # pylint:disable=R0903

    """Class:  SubProcess

    Description:  Class which is a representation of the subprocess class.

    Methods:
        __init__
        wait

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the ZipFile class.

        Arguments:

        """

    def wait(self):

        """Method:  wait

        Description:  Mock representation of subprocess.wait method.

        Arguments:

        """


class Server():

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__
        lock_db
        is_locked
        unlock_db

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.db_path = "Database_Directory_Path"
        self.locked = False
        self.auth_db = "Auth_Database"

    def lock_db(self, lock):

        """Method:  lock_db

        Description:  Stub holder for mongo_class.Server.lock_db method.

        Arguments:

        """

        self.locked = lock

    def is_locked(self):

        """Method:  is_locked

        Description:  Stub holder for mongo_class.Server.is_locked method.

        Arguments:

        """

        return self.locked

    def unlock_db(self):

        """Method:  unlock_db

        Description:  Stub holder for mongo_class.Server.unlock_db method.

        Arguments:

        """


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_set_db_auth
        test_db_load

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.subp = SubProcess()
        self.args.args_array = {"-p": "DirectoryPath2"}
        self.req_arg = ["--authenticationDatabase="]

    @mock.patch("mongo_db_restore.subprocess.Popen")
    @mock.patch("mongo_db_restore.mongo_libs.create_cmd")
    def test_set_db_auth(self, mock_cmd, mock_subp):

        """Function:  test_set_db_auth

        Description:  Test with setting the authenication database.

        Arguments:

        """

        mock_cmd.return_value = "LoadCommand"
        mock_subp.return_value = self.subp

        self.assertEqual(
            mongo_db_restore.single_db(
                self.server, self.args, req_arg=self.req_arg), (False, None))

    @mock.patch("mongo_db_restore.subprocess.Popen")
    @mock.patch("mongo_db_restore.mongo_libs.create_cmd")
    def test_db_load(self, mock_cmd, mock_subp):

        """Function:  test_db_load

        Description:  Test with database load successful.

        Arguments:

        """

        mock_cmd.return_value = "LoadCommand"
        mock_subp.return_value = self.subp

        self.assertEqual(
            mongo_db_restore.single_db(self.server, self.args), (False, None))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in mongo_db_restore.py.

    Usage:
        test/unit/mongo_db_restore/run_program.py

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
import mock

# Local
sys.path.append(os.getcwd())
import mongo_db_restore
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


# STOPPED HERE
def single_db2(server, args, **kwargs):

    """Method:  single_db2

    Description:  Function stub holder for mongo_db_restore.single_db.

    Arguments:

    """

    status = True
    err_msg = "Dump Failure"

    if server and args:
        status = True
        err_msg = "Load Failure"

    return status, err_msg


def single_db(server, args, **kwargs):

    """Method:  single_db

    Description:  Function stub holder for mongo_db_restore.single_db.

    Arguments:

    """

    status = False
    err_msg = None

    if server and args:
        status = False
        err_msg = None

    return status, err_msg


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mongo_class.Server class.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "Mongo_name"
        self.auth_db = "Auth_Database"
        self.status = True
        self.errmsg = None

    def connect(self):

        """Method:  connect

        Description:  Stub method holder for mongo_class.Server.connect.

        Arguments:

        """

        return self.status, self.errmsg


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_connect_failure
        test_connect_successful
        test_load_error
        test_load_successful 
        test_run_program

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.func_dict = {"-S": single_db}
        self.func_dict2 = {"-S": single_db2}
        self.args_array = {"-d": True, "-c": True, "-S": True}

    @mock.patch("mongo_db_restore.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_restore.mongo_libs.create_instance")
    def test_connect_failure(self, mock_inst):

        """Function:  test_connect_failure

        Description:  Test with connection is failure.

        Arguments:

        """

        self.server.status = False
        self.server.errmsg = "Connection Failure"

        mock_inst.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_restore.run_program(self.args_array,
                                                          self.func_dict))

    @mock.patch("mongo_db_restore.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_restore.mongo_libs.create_instance")
    def test_connect_successful(self, mock_inst):

        """Function:  test_connect_successful

        Description:  Test with connection is successful.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mongo_db_restore.run_program(self.args_array,
                                                      self.func_dict))

    @mock.patch("mongo_db_restore.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_restore.mongo_libs.create_instance")
    def test_load_error(self, mock_inst):

        """Function:  test_load_error

        Description:  Test with load returning error.

        Arguments:

        """

        mock_inst.return_value = self.server

        with gen_libs.no_std_out():
            self.assertFalse(mongo_db_restore.run_program(self.args_array,
                                                          self.func_dict2))

    @mock.patch("mongo_db_restore.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_restore.mongo_libs.create_instance")
    def test_load_successful(self, mock_inst):

        """Function:  test_load_successful

        Description:  Test with successful load.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mongo_db_restore.run_program(self.args_array,
                                                      self.func_dict))

    @mock.patch("mongo_db_restore.mongo_libs.disconnect",
                mock.Mock(return_value=True))
    @mock.patch("mongo_db_restore.mongo_libs.create_instance")
    def test_run_program(self, mock_inst):

        """Function:  test_run_program

        Description:  Test run_program function.

        Arguments:

        """

        mock_inst.return_value = self.server

        self.assertFalse(mongo_db_restore.run_program(self.args_array,
                                                      self.func_dict))


if __name__ == "__main__":
    unittest.main()

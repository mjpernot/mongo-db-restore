#!/usr/bin/python
# Classification (U)

"""Program:  single_collection.py

    Description:  Unit testing of single_collection in mongo_db_restore.py.

    Usage:
        test/unit/mongo_db_restore/single_collection.py

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


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        arg_file_chk
        get_val
        update_arg

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {
            "-c": "rabbitmq", "-d": "config", "-C": "collname", "-b": "dbname"}
        self.file_perm_chk = None
        self.arg_file_chk2 = True

    def arg_file_chk(self, file_perm_chk):

        """Method:  arg_file_chk

        Description:  Method stub holder for gen_class.ArgParser.arg_file_chk.

        Arguments:

        """

        self.file_perm_chk = file_perm_chk

        return self.arg_file_chk2

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def update_arg(self, arg_key, arg_val, **kwargs):

        """Method:  update_arg

        Description:  Method stub holder for gen_class.ArgParser.update_arg.

        Arguments:

        """

        errmsg = None
        status = True
        insert = kwargs.get("insert", False)

        if arg_key in self.args_array \
           or (arg_key not in self.args_array and insert):
            self.args_array[arg_key] = arg_val

        else:
            status = False
            errmsg = "Arg key does not exists"

        return status, errmsg


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
        self.japd = "JAPD"

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
        test_file_chk_failure
        test_db_load

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.args = ArgParser()
        self.req_arg = ["--authenticationDatabase="]
        self.opt_arg = {
            "-S": "--db=", "-o": "--dir=", "-z": "--gzip",
            "-i": "--tlsInsecure", "-r": "--restoreDbUsersAndRoles",
            "-k": "--drop", "-u": "--dryRun", "-e": "--verbose", "-b": "--db=",
            "-C": "--collection="}

    def test_file_chk_failure(self):

        """Function:  test_file_chk_failure

        Description:  Test with file check failure.

        Arguments:

        """

        self.args.args_array["-o"] = "/basedir"
        self.args.arg_file_chk2 = False

        self.assertFalse(
            mongo_db_restore.single_collection(
                self.server, self.args, opt_arg=self.opt_arg)[0])

    @mock.patch("mongo_db_restore.restore", mock.Mock(return_value=True))
    def test_db_load(self):

        """Function:  test_db_load

        Description:  Test with database load successful.

        Arguments:

        """

        self.args.args_array["-o"] = "/basedir"

        self.assertTrue(
            mongo_db_restore.single_collection(
                self.server, self.args, opt_arg=self.opt_arg)[0])


if __name__ == "__main__":
    unittest.main()

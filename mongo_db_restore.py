#!/usr/bin/python
# Classification (U)

"""Program:  mongo_db_restore.py

    Description:  The mongo_db_restore program loads a database dump into a
        a Mongo database.

    Usage:
        mongo_db_restore.py -c file -d path -o path
            {-S db_name}
            [-p path] [-y flavor_id]
            [-v | -h]

    Arguments:
        -c file => Server configuration file.  Required argument.
        -d dir path => Directory path to config file (-c). Required argument.
        -o dir path => Directory path to datbase dump directory.
            Required argument.
        -S db_name => Database name to be restored to.
        -p dir path => Directory path to mongo programs.
            Only needed if the mongo binary programs do not run properly.
            (i.e. not in the $PATH variable.)
        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.
            NOTE 1:  -v or -h overrides the other options.

    Notes:
        Warning:  If restoring to a Mongo database in a replica set, must
            connect to the primary database to complete this operation.

        Mongo configuration file format (config/mongo.py.TEMPLATE).  The
            configuration file format for the Mongo connection used for
            inserting data into a database.
            There are two ways to connect:  single or replica set.

            1.)  Single database connection:

            # Single Configuration file for Mongo Database Server.
            user = "USER"
            japd = "PSWORD"
            # Mongo DB host information
            host = "IP_ADDRESS"
            name = "HOSTNAME"
            # Mongo database port (default is 27017)
            port = 27017
            # Mongo configuration settings
            conf_file = None
            # Authentication required:  True|False
            auth = True
            # Authentication database
            auth_db = "admin"
            # Use Mongo client arguments
            use_arg = True
            # Use Mongo client uri
            use_uri = False

        Configuration modules -> Name is runtime dependent as it can be used to
            connect to different databases with different names.

    Example:
        mongo_db_restore.py -c mongo -d config -o /db_dump 

"""

# Libraries and Global Variables

# Standard
import sys
import os
import subprocess

# Third-party

# Local
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import lib.arg_parser as arg_parser
import lib.cmds_gen as cmds_gen
import mongo_lib.mongo_class as mongo_class
import mongo_lib.mongo_libs as mongo_libs
import version

__version__ = version.__version__

# Global
AUTH_DB = "--authenticationDatabase="


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def single_db(server, args_array, **kwargs):

    """Function:  single_db

    Description:  Restore single database.

    Arguments:
        (input) server -> Database server instance.
        (input) args_array -> Array of command line options and values.
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add.
            req_arg -> List of options to add to cmd line.
        (output) False -> If an error has occurred.
        (output) None -> Error message.

    """

    global AUTH_DB

    subp = gen_libs.get_inst(subprocess)
    args_array = dict(args_array)
    req_arg = list(kwargs.get("req_arg", []))
    opt_arg = dict(kwargs.get("opt_arg", {}))

    if AUTH_DB in req_arg:
        req_arg.remove(AUTH_DB)
        req_arg.append(AUTH_DB + server.auth_db)

    load_cmd = mongo_libs.create_cmd(
        server, args_array, "mongorestore",
        arg_parser.arg_set_path(args_array, "-p"), req_arg=req_arg,
        opt_arg=opt_arg)

    proc1 = subp.Popen(load_cmd)
    proc1.wait()

    return False, None


def run_program(args_array, func_dict, **kwargs):

    """Function:  run_program

    Description:  Creates class instance(s) and controls flow of the program.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dictionary list of functions and options.
        (input) **kwargs:
            opt_arg -> Dictionary of additional options to add.
            req_arg -> List of options to add to cmd line.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    server = mongo_libs.create_instance(args_array["-c"], args_array["-d"],
                                        mongo_class.Server)
    status, errmsg = server.connect()

    if status:

        # Intersect args_array and func_dict to find which functions to call.
        for item in set(args_array.keys()) & set(func_dict.keys()):
            err_flag, err_msg = func_dict[item](server, args_array, **kwargs)

            if err_flag:
                print(err_msg)

        cmds_gen.disconnect([server])

    else:
        print("Error:  Failed to connect.  Msg: %s" % (errmsg))


def main():

    """Function:  main

    Description:  Initializes program-wide used variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        func_dict -> dictionary list for the function calls or other options.
        opt_arg_list -> contains optional arguments for the command line.
        opt_req_list -> contains the options that are required for the program.
        opt_val_list -> contains options which require values.
        req_arg_list -> contains arguments to add to command line by default.

    Arguments:
        (input) argv -> Arguments from the command line.

    """

    global AUTH_DB

    cmdline = gen_libs.get_inst(sys)
    dir_chk_list = ["-d", "-o", "-p"]
    func_dict = {"-S": single_db}
    opt_arg_list = {"-S": "--db=", "-o": "--dir="}
    opt_req_list = ["-c", "-d", "-o"]
    opt_val_list = ["-c", "-d", "-o", "-p", "-S", "-y"]
    req_arg_list = [AUTH_DB]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(cmdline.argv, opt_val_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list):

        try:
            prog_lock = gen_class.ProgramLock(cmdline.argv,
                                              args_array.get("-y", ""))
            run_program(args_array, func_dict, opt_arg=opt_arg_list,
                        req_arg=req_arg_list)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("WARNING:  Lock in place for mongo_db_restore with id: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())

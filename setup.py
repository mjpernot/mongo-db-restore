# Classification (U)

"""Program:  setup.py

    Description:  A setuptools based setup module.

"""

# Libraries and Global Variables

# Standard
import os
import setuptools

# Third-party

# Local
import version


# Read in long description from README file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f_hdlr:
    LONG_DESCRIPTION = f_hdlr.read()

setuptools.setup(
    name="Mongo_DB_Restore",
    description="Database restoration program for Mongo.",
    author="Mark Pernot",
    author_email="Mark.J.Pernot@coe.ic.gov",
    url="https://sc.appdev.proj.coe.ic.gov/JAC-DSXD/mongo-db-restore",
    version=version.__version__,
    platforms=["Linux"],
    long_description=LONG_DESCRIPTION,

    classifiers=[
        # Common Values:
        #  1 - Pre-Alpha
        #  2 - Alpha
        #  3 - Beta
        #  4 - Field
        #  5 - Production/Stable
        "Development Status :: 1 - Pre-Alpha",
        "Operating System :: Linux",
        "Operating System :: Linux :: Centos",
        "Operating System :: Linux :: Centos :: 7",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: Linux :: RedHat",
        "Operating System :: Linux :: RedHat :: 8",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Topic :: Database",
        "Topic :: Database :: Mongodb",
        "Topic :: Database :: Mongodb :: 3.4",
        "Topic :: Database :: Mongodb :: 4.2"])

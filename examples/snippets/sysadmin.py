#r# =======================
#r#  System Administration
#r# =======================
#r#
#r# This page contains snippets for system administration tasks.
#r#
#r# See also
#r#
#r# * https://docs.python.org/3/library/pathlib.html
#r#

####################################################################################################

import os # os tools
import re # regexp tools
import subprocess # subprocesses tools
import tempfile # temporary file and directory tools

from Tools import *

####################################################################################################

#r# Note: Temporary file and directory are addressed first so as to define a temporary file hierarchy
#r# context manager used afterwards in this page.

#r#
#r# Temporary File and Directory
#r# ----------------------------
#r#
#r# Reference: https://docs.python.org/3/library/tempfile.html

with tempfile.TemporaryFile() as fh:
    fh.write(b'Hello world!')
    fh.seek(0)
    print(fh.read())
#o#

with tempfile.TemporaryDirectory() as tmp_directory:
    print('Created temporary directory', tmp_directory)
#o#

#r# Create a filesystem hierarchy

with tempfile.TemporaryDirectory() as tmp_directory:
    print('Created temporary directory', tmp_directory)
    for directory in ('.', 'subdir'):
        directory_path = os.path.join(tmp_directory, directory)
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
        for name in ('file1.txt', 'file.txt'):
            path = os.path.join(directory_path, name)
            with open(path, 'w') as fh:
                fh.write('...')

#r# Using a context manager

class TemporaryFileHierarchy:

    def __init__(self, *args, **kwargs):

        self._tmp_directory = tempfile.TemporaryDirectory()
        print('Created temporary directory', tmp_directory)

        self._chdir = kwargs.get('chdir', False)

        for directory in ('.', 'subdir'):
            directory_path = os.path.join(self._tmp_directory.name, directory)
            if not os.path.exists(directory_path):
                os.mkdir(directory_path)
            for name in ('file1', 'file2'):
                path = os.path.join(directory_path, name)
                with open(path, 'w') as fh:
                    fh.write(kwargs.get(name, '...'))


    def __enter__(self):
        path = self._tmp_directory.name
        if self._chdir:
            os.chdir(path)
        return path


    def __exit__(self, exc_type, exc_value, traceback):
        # self._tmp_directory.cleanup()
        pass

####################################################################################################

#r#
#r# Filesystem Snippets
#r# -------------------
#r#
#r# Reference: https://docs.python.org/3/library/os.path.html#module-os.path

with TemporaryFileHierarchy() as tmp_directory:

    # change current working directory
    os.chdir(tmp_directory)
    print('curent directory is now:', os.getcwd())

    abs_path = os.path.join(tmp_directory, 'subdir', 'file1') + '.txt'
    pretty_print((
        os.path.dirname(abs_path),
        os.path.basename(abs_path),
        os.path.splitext(abs_path),
    ))
    abs_path = os.path.join(tmp_directory, 'subdir', '..', 'file1')
    pretty_print((
        abs_path,
        os.path.realpath(abs_path), # remove .. and symlinks
    ))
    abs_path = os.path.join('.', 'subdir', 'file1')
    pretty_print((
        abs_path,
        os.path.abspath(abs_path),
    ))
#o#

####################################################################################################

#r#
#r# File Permission
#r# ---------------
#r#
#r# Reference: https://docs.python.org/3/library/os.html

with TemporaryFileHierarchy(chdir=True) as tmp_directory:

    for permission in (
            os.F_OK,
            os.R_OK,
            os.W_OK,
            os.X_OK,
    ):
        print('permission {}: {}'.format(permission, os.access("file1", permission)))
#o#

####################################################################################################

#r#
#r# Walk recursively on the filesystem (find)
#r# -----------------------------------------

#r# This snippet replaces the *find* command:
#r#
#r# Reference: https://docs.python.org/3/library/os.html#os.walk

with TemporaryFileHierarchy() as tmp_directory:

    for path, directories, files in os.walk(tmp_directory):
        print(path, directories, files)
        for filename in files:
            print(os.path.join(path, filename))
#o#

#r# PEP 471 – os.scandir() function – a better and faster directory iterator

with TemporaryFileHierarchy() as tmp_directory:

    for entry in os.scandir(tmp_directory):
        print(entry, entry.is_file(), entry.name)
#o#

####################################################################################################

#r#
#r# pattern Matching/Substitution (grep, sed)
#r# -----------------------------------------

#r# This snippet replaces the *grep* and *sed* commands:

file1_content = '''
Hello John,
It's a beautiful day!
Cheers,
'''

with TemporaryFileHierarchy(file1=file1_content) as tmp_directory:

    for path, directories, files in os.walk(tmp_directory):
        for filename in files:
            abs_path = os.path.join(path, filename)
            matched = False
            with open(abs_path, 'r') as fh:
                for line in fh.readlines():
                    # line = line.rstrip() # strip leading spaces and \n
                    if re.match('.*John.*', line):
                        print(abs_path, ':', line.rstrip())
                        matched = True
            if matched:
                # get content
                with open(abs_path, 'r') as fh:
                    content = fh.read()
                # update content
                content = content.replace('John', 'Paul')
                # write file inplace
                with open(abs_path, 'w') as fh:
                    fh.write(content)
                # new content is
                with open(abs_path, 'r') as fh:
                    print(fh.read())
#o#

####################################################################################################

#r#
#r# Execute subprocesses
#r# --------------------

#r#
#r# Reference: https://docs.python.org/3/library/subprocess.html

file1_content = '''
Hello John,
It's a beautiful day!
Cheers,
'''

with TemporaryFileHierarchy(file1=file1_content, chdir=True) as tmp_directory:

    # subprocess.call
    rc = subprocess.call(('grep', '-i', 'john', 'file1'))
    print('grep john:', rc == 0)

    rc = subprocess.call(('grep', '-i', 'paul', 'file1'))
    print('grep paul:', rc == 0)

    try:
        # subprocess.check_call
        subprocess.check_call(('grep', '-i', 'john', 'file1'))
        print('will fail')
        subprocess.check_call(('grep', '-i', 'paul', 'file1'))
    except subprocess.CalledProcessError:
        print('grep failed')

    # subprocess.check_output
    output = subprocess.check_output(('cat', 'file1'))
    print(output.decode('utf-8'))
#o#

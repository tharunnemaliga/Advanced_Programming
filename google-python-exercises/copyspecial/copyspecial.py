#!/usr/bin/env python
# coding: utf-8

# In[25]:


#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import shutil
import subprocess
import sys

"""Copy Special exercise
"""


# LAB(begin solution)
def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = []
    paths = os.listdir(dirname)  # list of paths in that dir
    for fname in paths:
        match = re.search(r'__(\w+)__', fname)
        if match:
            result.append(os.path.abspath(os.path.join(dirname, fname)))
    return result


def copy_to(paths, to_dir):
    """Copy all of the given files to the given dir, creating it if necessary."""
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for path in paths:
        fname = os.path.basename(path)
        shutil.copy(path, os.path.join(to_dir, fname))


def zip_to(paths, zipfile):
    """Zip up all of the given files into a new zip file with the given name."""
    cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
    print("Command I'm going to do:" + cmd)
    (status, output) = subprocess.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)

# LAB(end solution)

def process_special_files(dirs, todir='', tozip=''):
    # Gather all the special files
    paths = []
    for dirname in dirs:
        paths.extend(get_special_paths(dirname))

    if todir:
        copy_to(paths, todir)
    elif tozip:
        zip_to(paths, tozip)
    else:
        return paths


dirs = [r'C:\Users\varun\OneDrive\Documents\GitHub\Assignments']
todir = ''
tozip = ''

special_files = process_special_files(dirs, todir, tozip)
for file in special_files:
    print(file)
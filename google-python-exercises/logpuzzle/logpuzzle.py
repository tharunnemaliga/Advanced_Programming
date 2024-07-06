#!/usr/bin/env python
# coding: utf-8

# In[56]:


#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

# LAB(begin solution)
def url_sort_key(url):
    """Used to order the urls in increasing order by 2nd word if present."""
    match = re.search(r'-(\w+)-(\w+)\.\w+', url)
    if match:
        return match.group(2)
    else:
        return url
# LAB(end solution)

def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # Extract the hostname from the filename
    underbar = filename.find('_')
    if underbar == -1:
        raise ValueError("Filename does not contain an underscore")
    
    host = filename[underbar + 1:]

    # Store the urls into a dict to screen out the duplicates
    url_dict = {}

    with open(filename) as f:
        for line in f:
            match = re.search(r'"GET (\S+)', line)
            if match:
                path = match.group(1)
                if 'puzzle' in path:
                    url_dict['http://' + host + path] = 1

    return sorted(url_dict.keys(), key=url_sort_key)


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    index_path = os.path.join(dest_dir, 'index.html')
    with open(index_path, 'w') as index:
        index.write('<html><body>\n')

        for i, img_url in enumerate(img_urls):
            local_name = f'img{i}'
            local_path = os.path.join(dest_dir, local_name)
            print(f'Retrieving... {img_url}')
            urllib.request.urlretrieve(img_url, local_path)

            index.write(f'<img src="{local_name}">\n')

        index.write('</body></html>\n')



def process_logfile(logfile_path, todir=''):
    img_urls = read_urls(logfile_path)
    if todir:
        download_images(img_urls, todir)
    else:
        for url in img_urls:
            print(url)


logfile_path = r'C:\Users\varun\OneDrive\Documents\GitHub\Advanced_Programming\google-python-exercises\logpuzzle'
destination_dir = r'C:\Users\varun\OneDrive\Documents\GitHub\Advanced_Programming\google-python-exercises\logpuzzle'

# Process the log file and download images
process_logfile(logfile_path, todir=destination_dir)
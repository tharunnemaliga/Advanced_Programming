#!/usr/bin/env python
# coding: utf-8

# In[112]:


#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', 'Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    # Extract the year
    year_match = re.search(r'Popularity in (\d{4})', content)
    if not year_match:
        raise ValueError('Year not found in file')
    year = year_match.group(1)
    # Extract the names and rank numbers
    name_rank_matches = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', content)
    # Create a dictionary to store the names with their ranks
    name_rank_dict = {}
    for rank, male_name, female_name in name_rank_matches:
        name_rank_dict[male_name] = rank
        name_rank_dict[female_name] = rank
    # Build the resulting list
    result = [year]
    for name in sorted(name_rank_dict.keys()):
        result.append(f'{name} {name_rank_dict[name]}')
    return result


def process_files(filenames, summary=False):
    for filename in filenames:
        names_list = extract_names(filename)
        text = '\n'.join(names_list)
        if summary:
            with open(f'{filename}.summary', 'w', encoding='utf-8') as summary_file:
                summary_file.write(text + '\n')
        else:
            print(text)            


def main():
    filenames = [r'C:\Users\varun\OneDrive\Documents\GitHub\Advanced_Programming\google-python-exercises\babynames\baby1990.html']
    process_files(filenames, summary=False)
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

if __name__ == '__main__':
    main()


# In[ ]:
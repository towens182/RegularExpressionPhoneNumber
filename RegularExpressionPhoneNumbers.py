# -*- coding: utf-8 -*-
"""
Regular Expression
Tyler Owens
12-5-17
"""

import re

pattern = '^(\d\-)?\(?(\d{3})\)?[\-|\.|\s](\d{3})[\-\.\s](\d{4})\D*(\d{4})?$'

numbers = ['800-555-1212', '800 555 1212', '800.555.1212', '(800) 555-1212',
'1-800-555-1212', '800-555-1212-1234', '800-555-1212x1234', '800-555-1212 ext. 1234',
'1-(800) 555.1212 #1234']

for i in numbers:
    phonepattern = re.compile(pattern)
    pgroup = phonepattern.search(i).groups()
    print(i)
    print('Area code = ', pgroup[1])
    print('Trunk code = ', pgroup[2])
    print('Number code = ', pgroup[3])
    print('Extension = ', pgroup[4])
    print('\n')
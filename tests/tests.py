"""Script for testing python command line interface.
"""

import re
import string
from random import choice
from itertools import product

def random_text(elements, each=5, total=5):
    """Returns a list of random strings chosen from
    an input string elements.
    
    Each string is of length each for a total of 
    total.
    """
    element_list = list(elements)
    out = [''.join(x) for x in
             [[choice(element_list) for _ in range(each)]
                      for _ in range(total)]
           ]

    return out

def setup():
    """
    Setup some fake files for grouping and moving.
    """


    first = random_text('12345', 5, 5)
    second = random_text(string.ascii_letters + '_'*5,
                         20, 5)
    first_second = product(first, second)
    test_names = [''.join(x) for x in first_second]
    return test_names


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PyHandy is a simple Python library for handling basic IO operations.
"""

from pyhandy import remove_multiple_newlines_in_txt

__author__ = 'Jared Peterson'
__license__ = 'apache-2.0'
__maintainer__ = 'Jared Peterson'
__email__ = 'jared.peterson@hey.com'
__version__ = '0.0.3'
__status__ = 'Development'


def test_remove_multiple_newlines_in_txt():
    # create a simple txt str with multiple newlines in it.
    test_txt = """This 
    is
    
    
    a
    
    
    
    test
    
    
    
    
    string
    
    
    """

    cleaned_txt = remove_multiple_newlines_in_txt(test_txt)

    expected_txt = """This 
    is
    
    a
    
    test
    
    string
    
    """.rstrip(' ')  # the multiline string will have spaces at the end... trim them.

    # make sure things look like we'd expect
    assert cleaned_txt == expected_txt

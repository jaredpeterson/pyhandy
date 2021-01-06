#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for txt_utils.py.
"""

from pyhandy import remove_multiple_newlines_in_txt, trim_spaces_and_tabs_from_lines_in_txt


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

"""

    # make sure things look like we'd expect
    assert cleaned_txt == expected_txt


def test_trim_spaces_and_tabs_from_lines_in_txt():
    # create a simple test string
    test_txt = """    This
                                               is
a
\t                  test
      string
\t\t\t
      
      
"""  # noqa: W293

    cleaned_txt = trim_spaces_and_tabs_from_lines_in_txt(test_txt)

    # create a string to compare against
    expected_txt = """This
is
a
test
string



"""

    # make sure things look like we expect them to.
    assert cleaned_txt == expected_txt

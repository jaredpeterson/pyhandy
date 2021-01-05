#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for txt_utils.py.
"""

from pyhandy import remove_multiple_newlines_in_txt


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

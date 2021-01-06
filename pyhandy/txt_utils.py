#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Utility functions for handling basic text IO.
"""

import io


def remove_multiple_newlines_in_txt(txt: str) -> str:
    """ This function will remove multiple, sequential newlines in text (str) data.

    :param txt: a str containing the text to be cleaned.
    :return: a str containing the text with multiple, sequential newlines removed.
    """

    clean_txt = ''

    # convert the text string into a buffer so that we can read lines.
    txt_buffer = io.StringIO(txt)

    last_line = True  # initialize to True so that on our first pass through the loop we'll get the first line.
    next_line = txt_buffer.readline()
    while next_line:
        stripped_next_line = next_line.strip()

        # was our previous line also a new line?
        if last_line:  # strings in Python are "falsey" so '' will not pass.
            # no, was not a newline... add the current line to our cleaned text.
            clean_txt += next_line
        else:
            # yes, our previous line was a newline... is our current?
            if stripped_next_line:
                # must have content... write it out.
                clean_txt += next_line

        # set last_line to our current line (stripped version) and then grab the next line.
        last_line = stripped_next_line
        next_line = txt_buffer.readline()

    return clean_txt


def trim_spaces_and_tabs_from_lines_in_txt(txt: str) -> str:
    """ This function will remove leading spaces and tabs from lines of text.

    :param txt: a str containing the text to be cleaned up.
    :return: a str containing text with all of the leading spaces removed from each line.
    """

    clean_txt = ''

    # convert the text string into a buffer so that we can read lines.
    txt_buffer = io.StringIO(txt)

    # iterate through each line trimming whitespace.
    next_line = txt_buffer.readline()
    while next_line:
        stripped_next_line = next_line.lstrip(' \t')  # just want spaces and tabs.
        clean_txt += stripped_next_line

        # grab the next line.
        next_line = txt_buffer.readline()

    return clean_txt

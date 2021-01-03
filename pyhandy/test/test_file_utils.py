# -*- coding: utf-8 -*-

"""
Unit tests for common file/directory utilities.

Author: Jared Peterson
Email: jared.peterson@hey.com
"""

from pathlib import Path

import pyhandy as ph


def test_write_content_as_file(tmpdir):
    test_content = 'this\nis\ntest\ncontent.'
    test_file_name = 'write_content_as_file_test_file.txt'

    # use our utility method to write the file.
    ph.write_content_as_file(test_content, test_file_name, tmpdir)  # tmpdir should be supplied by pytest.

    # read the contents of the file back out so that we can compare contents.
    with open(Path(tmpdir, test_file_name), 'r') as test_file:
        assert_content = test_file.read()

    assert assert_content == test_content


def test_load_content_from_file(tmpdir):
    test_content = 'this\nis\ntest\ncontent.'
    test_file_name = 'load_content_from_file_test_file.txt'

    # write some content to a test file.
    with open(Path(tmpdir, test_file_name), 'w') as test_file:
        test_file.write(test_content)

    # load the content using our utility method.
    assert_content = ph.load_content_from_file(test_file_name, tmpdir)  # tmpdir should be supplied by pytest.

    assert assert_content == test_content

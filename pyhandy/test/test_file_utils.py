#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for file_utils.py.
"""

from os import makedirs
from pathlib import Path

from pyhandy import create_new_output_dir, \
    list_paths_to_files_in_dir, \
    copy_files_to_dir, \
    write_content_as_file, \
    load_content_from_file


def test_create_new_output_dir(tmpdir):
    output_dir_path = create_new_output_dir(tmpdir)  # tmpdir should be supplied by pytest.

    # make sure that our new output directory got created.
    assert Path(output_dir_path).is_dir()


def test_list_filenames_in_dir(tmpdir):
    # create two different temporary files... use other utilities to do this.
    test_1_content = 'this\nis\ntest\n1\ncontent.'
    test_1_file_name = 'test_1.txt'
    write_content_as_file(test_1_content, test_1_file_name, tmpdir)  # tmpdir should be supplied by pytest.
    test_1_path = str(Path(tmpdir) / Path(test_1_file_name))

    test_2_content = 'this\nis\ntest\n2\ncontent.'
    test_2_file_name = 'test_2.txt'
    write_content_as_file(test_2_content, test_2_file_name, tmpdir)  # tmpdir should be supplied by pytest.
    test_2_path = str(Path(tmpdir) / Path(test_2_file_name))

    # now list the paths to the files in the temp directory.
    paths_to_files_in_dir = list_paths_to_files_in_dir(tmpdir)

    # make sure our list is the right size and has the proper elements.
    assert len(paths_to_files_in_dir) == 2
    assert test_1_path in paths_to_files_in_dir
    assert test_2_path in paths_to_files_in_dir


def test_copy_files_to_dir(tmpdir):
    # create one test directory with two files in it.
    test_dir_1 = Path(tmpdir) / 'test_dir_1'  # tmpdir should be supplied by pytest.
    makedirs(test_dir_1)

    file_1_content = 'file_1'
    file_1_file_name = 'file_1.txt'
    write_content_as_file(file_1_content, file_1_file_name, test_dir_1)
    file_1_path = str(Path(test_dir_1) / Path(file_1_file_name))

    file_2_content = 'file_2'
    file_2_file_name = 'file_2.txt'
    write_content_as_file(file_2_content, file_2_file_name, test_dir_1)
    file_2_path = str(Path(test_dir_1) / Path(file_2_file_name))

    # create a second directory to copy files to.
    test_dir_2 = Path(tmpdir) / Path('test_dir_2')  # tmpdir should be supplied by pytest.
    makedirs(test_dir_2)

    copy_files_to_dir(test_dir_2, [file_1_path, file_2_path])

    # list the files in the second directory
    paths_to_files_in_dir_2 = list_paths_to_files_in_dir(test_dir_2)

    # make sure that things look right.
    assert len(paths_to_files_in_dir_2) == 2
    assert str(Path(test_dir_2) / Path(file_1_file_name)) in paths_to_files_in_dir_2
    assert str(Path(test_dir_2) / Path(file_2_file_name)) in paths_to_files_in_dir_2


def test_write_content_as_file(tmpdir):
    test_content = 'this\nis\ntest\ncontent.'
    test_file_name = 'write_content_as_file_test_file.txt'

    # use our utility method to write the file.
    write_content_as_file(test_content, test_file_name, tmpdir)  # tmpdir should be supplied by pytest.

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
    assert_content = load_content_from_file(test_file_name, tmpdir)  # tmpdir should be supplied by pytest.

    assert assert_content == test_content

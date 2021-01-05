#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PyHandy is a simple Python library for handling basic IO operations.
"""

__author__ = 'Jared Peterson'
__license__ = 'apache-2.0'
__maintainer__ = 'Jared Peterson'
__email__ = 'jared.peterson@hey.com'
__version__ = '0.0.3'
__status__ = 'Development'

# grab everything in file_utils.py
from .file_utils import create_new_output_dir, \
    list_paths_to_files_in_dir, \
    copy_files_to_dir, \
    write_content_as_file, \
    load_content_from_file, \
    generate_csv_for_dir

# grab everything in txt_utils.py
from .txt_utils import remove_multiple_newlines_in_txt

__all__ = [
    'create_new_output_dir',
    'list_paths_to_files_in_dir',
    'copy_files_to_dir',
    'write_content_as_file',
    'load_content_from_file',
    'generate_csv_for_dir',
    'remove_multiple_newlines_in_txt'
]

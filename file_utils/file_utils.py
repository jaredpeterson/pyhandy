# -*- coding: utf-8 -*-

"""
Common file/directory utilities.

Author: Jared Peterson
Email: jared.peterson@gmail.com
"""

from pathlib import Path
from datetime import datetime
from os import makedirs
from os import path
from shutil import copy
from typing import List

import pandas as pd


def create_new_output_dir(prefix='./') -> str:
    """ Creates a new directory that output data can be written to.

    :param prefix a string that will be concatenated with the generated name.
    :return: a string containing the output directory name.
    """

    # use a nice string representation of the date as the directory name... also use prefix.
    output_dir_path = str(Path(f"{prefix}{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"))

    # create the directory and return name... makedirs ensure that parent dirs are created as well.
    makedirs(output_dir_path)
    return output_dir_path


def list_filenames_in_dir(path_to_dir) -> List[str]:
    """ Return a list of only filenames within a directory.

    :param path_to_dir: a string path to the directory.
    :return: a list containing only the filenames in the directory.
    """

    # convert generator to list using the list() function.
    return list((str(file_or_dir) for file_or_dir in Path(path_to_dir).iterdir() if file_or_dir.is_file()))


def copy_files_to_dir(path_to_dir, files_to_copy=None) -> None:
    """ Copy a list of file paths to a destination directory.

    :param path_to_dir: the path to the destination directory.
    :param files_to_copy: a list containing the files to copy.
    """

    if files_to_copy is None:
        files_to_copy = []

    # make sure that the destination directory exists.
    makedirs(path_to_dir)

    # iterate over the files copying them to the destination.
    for file_to_copy in files_to_copy:
        copy(file_to_copy, path_to_dir)


def generate_csv_for_dir(path_to_documents_dir, path_to_csv_file, delimiter='|') -> None:
    """ This function will build a csv file where each row in the csv file represents a document in the directory.

    :param path_to_documents_dir: a string containing the path to the directory to use.
    :param path_to_csv_file: a string containing the path of the .csv file to generate.
    :param delimiter: a string specifying the delimiter to use in the .csv file generation.
    """

    # construct a dataframe to collect the file data in.
    file_data_frame = pd.DataFrame(columns=['filename', 'text'])

    # list the files in the directory.
    filenames_in_documents_dir = list_filenames_in_dir(path_to_documents_dir)

    # iterate over the list of files and read the content
    for filename_in_documents_dir in filenames_in_documents_dir:
        with open(filename_in_documents_dir, 'r') as file_in_documents_dir:
            document_str = file_in_documents_dir.read()

        # for safety... let's remove any instances of the delimiter from the file content.
        document_str = document_str.replace(delimiter, '')

        # add the data to the dataframe
        file_data_frame.loc[len(file_data_frame)] = \
            [path.basename(filename_in_documents_dir), document_str]  # filename_in_dir is a Path object.

    # write the data frame to a .csv file
    file_data_frame.to_csv(path_to_csv_file, sep=delimiter, index_label='id')

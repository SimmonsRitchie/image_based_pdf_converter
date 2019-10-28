"""
MODULE: MISC

Handles miscellaneous operations

"""

import os

def program_intro():
    print("-----------------------------------------------------------------------------")
    print("------------------     IMAGE-BASED PDF CONVERTER     -------------------------")
    print("-----------------------------------------------------------------------------")
    print("")

def linebreak_start():
    print("")
    print("-----------------------------------------------------------------------------")

def linebreak_end():
    print("-----------------------------------------------------------------------------")
    print("")

def path_gen(directory, filename):
    """
    :param directory: String. Directory name of directory where file should exist
    :param filename: String. Filename of file.
    :return: Path to file. If no matching directory is found, one will be created.
    """

    # if directory doesn't exist, creates directory
    if not os.path.exists(directory):
        os.makedirs(directory)
    # returns path
    return os.path.join(directory,filename)

def get_list_of_files_in_folder(directory, *, file_extension=False):

    """
    :param directory: String. Directory name of directory you want to search
    :param file_extension: String. Optional. Filter list by file extension.
    :return: list of all files in directory that meet conditions
    """

    if file_extension:
        print("Checking how many {} files in {}...".format(file_extension, directory))
        list_of_files = [name for name in os.listdir(directory) if name.endswith(file_extension)]
    else:
        print("Checking how many files in {}...".format(directory))
        list_of_files = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]

    # sort files, a to z
    list_of_files.sort()

    print("{} files:".format(len(list_of_files)))
    for file in list_of_files:
        print(file)
    return list_of_files
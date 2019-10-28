"""
MODULE: DELETE

Deletes folders and files from earlier program runs.

"""

import os
from shutil import rmtree


def delete_old_files(folders_to_delete):
    print("Checking that temp files have been deleted from previous program runs")
    for folder in folders_to_delete:
        path_of_folder = os.path.abspath(folder)
        if os.path.exists(path_of_folder):
            print("Deleting {}...".format(folder))
            try:
                rmtree(path_of_folder)
                print("Successfully deleted the directory and all files inside")
            except OSError:
                print("Deletion of the directory %s failed for some reason" % path_of_folder)
        else:
            print("No folder named {} detected".format(folder))

"""
MODULE: PROCESS TEXT

Handles processing of output text files.

"""

# My imports
from modules.misc import path_gen, get_list_of_files_in_folder


def merge_text(output_text_directory, final_directory, pdf_filename):

    print("Merging text files into one text file...")

    list_of_text_files = get_list_of_files_in_folder(output_text_directory)
    output_filename = pdf_filename.replace('.pdf','.txt')
    output_path = path_gen(final_directory, output_filename)

    with open(output_path, 'w') as outfile:
        for fname in list_of_text_files:
            fname_path = path_gen(output_text_directory, fname)
            with open(fname_path) as infile:
                for line in infile:
                    outfile.write(line)

    print("Text files merged into file: {}".format(output_filename))

"""
IMAGE-BASED PDF CONVERTER
Author: Daniel Simmons-Ritchie

This program converts image-based PDFs into text files. It first converts a PDF entirely into images and then uses OCR
to read text in those images.

Credit to geeksforgeeks.org, which heavily inspired the code for handling PDF parsing: https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

"""


# Third party imports
from datetime import datetime
from pathlib import Path

# My imports
from modules.misc import program_intro, linebreak_start, linebreak_end, get_list_of_files_in_folder
from modules.process_pdf import split_pdf, convert_pdf_to_image
from modules.process_img import convert_image_to_text
from modules.process_txt import merge_text
from modules.delete import delete_old_files

def main():

    ############ PROGRAM START ############

    start = datetime.now() # get current time, so we can see program runtime at end
    program_intro() # simple header for console display

    ############ SET UP ############

    # dirs
    output_parent_dir = Path("output_files/")
    input_pdf_directory = "input_pdfs"
    pdf_chunk_directory = output_parent_dir / "processed_pdf_chunks/"
    image_directory = output_parent_dir / "processed_images/"
    output_text_directory = output_parent_dir / "processed_text/"
    final_directory = output_parent_dir / "final_text/"

    # other vars
    delete_list_start_program = [pdf_chunk_directory, image_directory, output_text_directory] # temp folders that must be deleted when program starts
    delete_list_main_process_loop = [pdf_chunk_directory, image_directory] # temp folders that must be deleted each time it processes a PDF
    delete_list_pdf_chunk_loop = [image_directory] # temp folders that must be deleted each time it processes a PDF
    page_split_threshold = 10 # splits pdfs into chunks based on this value (good for large pdfs)
    image_quality = 300 # DPI for images, use 500 if you want higher quality images

    ############ DELETE ALL OLD TEMP FILES ############

    delete_old_files(delete_list_start_program) # we delete old files so that it doesn't impact current program run

    ############ PDF PROCESS LOOP ############

    list_of_pdfs = get_list_of_files_in_folder(input_pdf_directory, file_extension='.pdf') # get all pdf filenames

    for count, pdf_filename in enumerate(list_of_pdfs):

        linebreak_start()
        print("Processing PDF {}: {}".format(count + 1, pdf_filename))

        ############ DELETE TEMP PROCESS FILES ############

        delete_old_files(delete_list_main_process_loop)

        ############ SPLIT PDF ############

        split_pdf(input_pdf_directory, pdf_filename, page_split_threshold, pdf_chunk_directory)

        ############ PDF CHUNK PROCESS LOOP ############

        list_of_pdf_chunks = get_list_of_files_in_folder(pdf_chunk_directory)

        for chunk_count, pdf_chunk_filename in enumerate(list_of_pdf_chunks):

            print("Processing PDF chunk {}: {}".format(chunk_count + 1, pdf_chunk_filename))

            ############ DELETE TEMP PROCESS FILES ############

            delete_old_files(delete_list_pdf_chunk_loop)

            ############ CONVERT PDF TO IMAGE ############

            convert_pdf_to_image(pdf_chunk_directory, pdf_chunk_filename, image_directory, image_quality)

            ############ CONVERT IMAGES TO TEXT ############

            convert_image_to_text(image_directory, output_text_directory, pdf_chunk_filename)

        ############ MERGE TEXT FILES ############

        merge_text(output_text_directory, final_directory, pdf_filename) # merges all the text files from our pdf chunks into one file
        linebreak_end()

    ############ PROGRAM END ############

    final_time = datetime.now() - start
    print("Program runtime: {}".format(final_time))


# Start main loop if running from program.py
if __name__ == '__main__':
    main()

"""
MODULE: PROCESS PDF

Handles processing of PDF.

Hat tip: Credit to Geeksforgeeks.org. The convert_pdf_to_image function in this module is
inspired heavily by their example code: https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

"""
# Third party imports
import PIL
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

# My imports
from modules.misc import path_gen, get_list_of_files_in_folder



def split_pdf(input_pdf_directory, pdf_filename, page_split_threshold, pdf_chunk_directory):
    print("Checking whether PDF should be split into smaller PDFs...")

    # get path to pdf
    path_to_pdf = os.path.join(input_pdf_directory, pdf_filename)

    # creating a pdf file object
    pdfFileObj = open(path_to_pdf, 'rb')

    # creating a pdf reader object
    pdfReader = PdfFileReader(pdfFileObj, strict=False) # added strict arg to ignore 'Stream has ended unexpectedly error' in certain pdfs

    # get num of pages
    pages = pdfReader.getNumPages()
    print("{} pages detected in PDF".format(pages))

    # init pdf writing object
    pdf_writer = PdfFileWriter()

    # determining whether page_split_threshold is valid number
    if page_split_threshold < 1 or not isinstance(page_split_threshold, int):
        page_split_threshold_default = 10
        print("You have selected {} as page_split_threshold - this is an invalid input".format(page_split_threshold))
        print("Please provide a positive integer")
        print("Program will default to page_split_threshold of {}".format(page_split_threshold_default))
        page_split_threshold = page_split_threshold_default

    # count chunks
    chunk_count = 0

    print("Splitting pdf into chunks every {} pages...".format(page_split_threshold))

    for page in range(pages):



        # add current pdf page to pdf_writer object
        pdf_writer.addPage(pdfReader.getPage(page))

        # if page is page_split_threshold or it's the last page, then write to file
        if (page + 1) % page_split_threshold == 0 or page == (pages - 1):

            # add to chunk count
            chunk_count += 1

            # create filename based on page range
            pdf_filename = pdf_filename.replace('.pdf','')
            chunk_count_formatted = str(chunk_count).zfill(3)
            output_filename = '{}_chunk_{}.pdf'.format(pdf_filename, chunk_count_formatted)

            # create output path
            output_path = path_gen(pdf_chunk_directory, output_filename)

            # write page chunk
            with open(output_path, 'wb') as out:
                pdf_writer.write(out)

            # clear pdf_writer
            pdf_writer = PdfFileWriter()

            print('Created: {}'.format(output_filename))

    print("{} has been split into {} chunks".format(pdf_filename, chunk_count)) # we remove one from chunk



def convert_pdf_to_image(input_pdf_directory, pdf_filename, image_directory, image_quality=300):
    print("Converting PDF to images...")

    # Store all the pages of the PDF in a variable
    path_to_pdf = os.path.join(input_pdf_directory, pdf_filename)
    PIL.Image.MAX_IMAGE_PIXELS = 933120000 # set this to avoid PIL.Image.DecompressionBombError with certain pdf pages
    pages = convert_from_path(path_to_pdf, image_quality)

    # Counter to store images of each page of PDF to image
    image_counter = 1

    # Iterate through all the pages stored above
    for page in pages:

        print("Converting page: {}".format(image_counter))

        image_counter_formatted = str(image_counter).zfill(3)
        filename = pdf_filename.replace('.pdf','') + "__image_" + image_counter_formatted + ".jpg" # adding corresponding page number to image filename
        image_path = path_gen(image_directory, filename)

        # Save the image of the page in system
        # page.save(image_path, 'JPEG')
        page.save(image_path, 'JPEG')

        # Increment the counter to update filename
        image_counter = image_counter + 1



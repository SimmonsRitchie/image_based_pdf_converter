"""
MODULE: PROCESS IMG

Handles processing of images.

Hat tip: convert_image_to_text function is heavily based on
a Geeksforgeeks.org tutorial: https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/

"""

# Third party imports
import pytesseract
from PIL import Image

# my imports
from modules.misc import path_gen, get_list_of_files_in_folder


def convert_image_to_text(image_directory, output_text_directory, pdf_filename):

    print("Recognizing text from images using OCR...")

    # Get list of files in folder (ignore subdirectories)
    list_of_images = get_list_of_files_in_folder(image_directory)

    # Creating a text file to write the output
    output_text_filename = pdf_filename.replace('.pdf','.txt')
    outfile_path = path_gen(output_text_directory, output_text_filename)

    # Open the file in append mode so that
    # All contents of all images are added to the same file
    f = open(outfile_path, "a")

    # Iterate through all images
    for filename in list_of_images:
        print("Converting image: {}".format(filename))

        image_path = path_gen(image_directory, filename)

        # Recognize the text as string in image using pytesserct
        text = str(((pytesseract.image_to_string(Image.open(image_path)))))

        # The recognized text is stored in variable text
        # Any string processing may be applied on text
        # Here, basic formatting has been done:
        # In many PDFs, at line ending, if a word can't
        # be written fully, a 'hyphen' is added.
        # The rest of the word is written in the next line
        # Eg: This is a sample text this word here GeeksF-
        # orGeeks is half on first line, remaining on next.
        # To remove this, we replace every '-\n' to ''.
        text = text.replace('-\n', '')

        # Finally, write the processed text to the file.
        f.write(text)

    # Close the file after writing all the text.
    f.close()
    print("Finished converting text from image.")
#### Image-based PDF converter

A python program to convert scanned/image-based PDFs into text using OCR.

It first converts each page in a PDF into an image and then uses pytesseract to convert any text into a .txt file. 
Large files are broken into chunks.

Credit to geeksforgeeks.org, which heavily inspired the code for handling [PDF parsing](https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/)


##### Requirements

- Python 3.6.
- Tesseract. If you have homebrew installed, run the following command from your terminal:

```
brew install tesseract
```

##### Install and run

1. Copy the PDFs you wish to convert into text files into the 'input_pdfs' directory.

2. CD into project folder, then run:

```
pip3 install -r requirements.txt
```

3. Run the program:

```
python main.py
```

Text versions of each PDF will be generated in 'final_text' folder NOTE: PDFs of 100+ pages may take 10 minutes or 
more to process.

##### Author

Daniel Simmons-Ritchie

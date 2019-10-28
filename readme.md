#### Image-based PDF converter

This program was written to convert scanned/image-based PDFs into text using OCR.

The program first converts each page in a PDF into an image and then uses pytesseract to convert any text into a .txt file.

##### Requirements

- Python 3.6.
- You'll need tesseract installed on your computer. If you have homebrew installed, use:

    brew install tesseract

##### Install and run

1. Copy the PDFs you wish to convert to text into the 'input_pdfs' directory.

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

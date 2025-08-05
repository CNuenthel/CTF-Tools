# Requires tesseract engine and poppler install for method 2
# poppler -- https://github.com/oschwartz10612/poppler-windows/releases
# tesseract -- https://github.com/UB-Mannheim/tesseract/wiki
# poppler bin file directory needs to be added to path

import fitz
from pdf2image import convert_from_path
import pytesseract


def read_through_ocr(filename: str):
    images = convert_from_path(filename)

    for i, img in enumerate(images):
        text = pytesseract.image_to_string(img)
        print(f"--- OCR Page {i + 1} ---")
        print(text)

def read_raw_text(filename: str):
    doc = fitz.open(filename)
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")  # raw text, regardless of visuals
        print(f"--- Page {page_num} ---")
        print(text)

def get_input():
    inpt = input("1. Read raw text\nor\n2. Read through OCR\n")
    if inpt.strip() not in ("1", "2"):
        print("Invalid input\n")
        get_input()
    return inpt.strip()

if __name__ == "__main__":
    print("--- PDF Text Extraction ---")

    while True:
        fn = input("PDF Filepath: ")
        method = get_input()

        match method:
            case "1":
                read_raw_text(fn)
            case "2":
                read_through_ocr(fn)

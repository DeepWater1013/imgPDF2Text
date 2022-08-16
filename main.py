# Module Imports
import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Define Paths
poppler_path = r'C:\Program Files (x86)\poppler-0.68.0\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

pdf_path = "sample.pdf"

# Save PDF pages to images
images = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)
for count, img in enumerate(images):
    img_name = f"page_{count}.png"  
    img.save(img_name, "png")

# Extract Text
png_files = [f for f in os.listdir(".") if f.endswith(".png")]

for png_file in png_files:
    extracted_text = pytesseract.image_to_string(Image.open(png_file), lang='eng')
    print(extracted_text)
    
    with open(png_file + '_out.txt', 'w') as f:
        f.write(extracted_text)


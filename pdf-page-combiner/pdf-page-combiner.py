# Script to horizontal slides into A4 with 2-up slides

import pymupdf # pymupdf
import sys
from os import path

if len(sys.argv) < 2:
    print("Usage: python3 slide-aggregator.py <srcPath>")
    sys.exit()

srcPath = sys.argv[1]

if not path.exists(srcPath):
    print("Could not find a file at the provided path")
    sys.exit()

# open 
srcDoc = pymupdf.open(srcPath)
resDoc = pymupdf.open() # empty output

# A4, 300dpi
width, height = 2480, 3508

# 2 rectangles per page
topRect = pymupdf.Rect(0, 0, width, height / 2)
bottomRect = pymupdf.Rect(0, height / 2, width, height)

rects = [topRect, bottomRect]

for srcPage in srcDoc.pages():

    if srcPage.number % 2 == 0:
        resPage = resDoc.new_page(-1, width=width, height=height)

    resPage.show_pdf_page(
        rects[srcPage.number % 2],
        srcDoc,
        srcPage.number
    )

# save the result
resDoc.save("output.pdf", garbage=4, deflate=True)

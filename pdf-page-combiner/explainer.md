## PDF Page Combiner

### Explanation
Small util script that takes an input PDF, and converts it into 2-up form.
Creates A4-Format pages in the output, fitting the pages from the input in the top/bottom halves of the page.
Works best on PDF files with horizontally oriented A4-format pages (like slides)

The resulting quality can be adjusted within the script by adjusting the width and height params.

### Usage
```bash
python3 pdf-page-combiner.py /this/example/path
```

### Setup
```bash
python3 -m venv .venv # Optional
pip install -r requirements.txt
```

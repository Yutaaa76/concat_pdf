# PDF Concatenation Tool

This is a command-line tool for merging and manipulating PDF files. It is implemented in Python with the help of GitHub Copilot.

## Features
- Concatenate two or more PDF files into one.
- Split a PDF into single-page PDFs.
- Extract specific pages from a PDF.
- Handles missing or unreadable files gracefully.
- Includes unit tests (pytest) and BDD tests (Behave).
- Code linting with Ruff and type checking with mypy.

## Requirements
- Python 3.7+
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [ruff](https://pypi.org/project/ruff/) (for linting)
- (For testing) [pytest](https://docs.pytest.org/), [behave](https://behave.readthedocs.io/), [mypy](http://mypy-lang.org/)

## Installation
1. Clone this repository.
2. Install dependencies (with pinned versions):
   ```sh
   pip install -r requirements.txt
   # or for development (includes linting and testing tools):
   pip install -r requirements-dev.txt
   ```

> **Note:** All dependencies are pinned to specific versions in the requirements files for reproducibility and to lock versions.
> To update the lock, run `pip freeze > requirements.txt` after installing or upgrading packages.

## Usage
To concatenate PDF files:
```sh
python main.py file1.pdf file2.pdf -o merged.pdf
```

To split a PDF into single-page PDFs:
```python
from concat_pdf.concat_pdf import split_pdf
split_pdf('input.pdf', 'output_dir')
```

To extract specific pages from a PDF:
```python
from concat_pdf.concat_pdf import extract_pages
extract_pages('input.pdf', [1, 3, 5], 'output.pdf')
```

For help:
```sh
python main.py --help
```

## Testing
Run unit tests with:
```sh
pytest tests/
```

Run BDD (Behave) tests with:
```sh
behave tests/features
```

## Code Quality
Run Ruff linter:
```sh
ruff check .
```

Run mypy type checker:
```sh
mypy .
```

## Project Structure
- `main.py` — CLI entry point
- `concat_pdf/concat_pdf.py` — Core PDF manipulation logic
- `tests/` — Unit and BDD tests
- `requirements.txt` — Runtime dependencies (pinned)
- `requirements-dev.txt` — Development dependencies (pinned)

---

This project was coded with the help of GitHub Copilot.

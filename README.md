# PDF Concatenation Tool

This is a command-line tool for merging multiple PDF files into a single PDF. It is implemented in Python with the help of GitHub Copilot.

## Features
- Concatenate two or more PDF files into one.
- Handles missing or unreadable files gracefully.
- Includes unit tests (pytest) and BDD tests (Behave).

## Requirements
- Python 3.7+
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- (For testing) [pytest](https://docs.pytest.org/) and [behave](https://behave.readthedocs.io/)

## Installation
1. Clone this repository.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   # or install manually:
   pip install PyPDF2 pytest behave
   ```

## Usage
To concatenate PDF files:
```sh
python main.py file1.pdf file2.pdf -o merged.pdf
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

## Project Structure
- `main.py` — CLI entry point
- `concat_pdf/concat_pdf.py` — Core PDF merging logic
- `tests/` — Unit and BDD tests
- `requirements.txt` — (optional) List of dependencies

---

This project was coded with the help of GitHub Copilot.

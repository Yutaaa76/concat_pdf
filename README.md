# PDF Concatenation Tool

This is a command-line tool for merging multiple PDF files into a single PDF. It is implemented in Python with the help of GitHub Copilot.

## Features
- Concatenate two or more PDF files into one.
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
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   # or for development (includes linting and testing tools):
   pip install -r requirements-dev.txt
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

## Code Quality
Run Ruff linter:
```sh
ruff check .
```


## Project Structure
- `main.py` — CLI entry point
- `concat_pdf/concat_pdf.py` — Core PDF merging logic
- `tests/` — Unit and BDD tests
- `requirements.txt` — Runtime dependencies
- `requirements-dev.txt` — Development dependencies

---

This project was coded with the help of GitHub Copilot.

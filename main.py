import argparse
from concat_pdf.concat_pdf import concat_pdfs

def main():
    """
    Command-line interface for concatenating multiple PDF files into a single output PDF.

    Example:
        python main.py file1.pdf file2.pdf -o merged.pdf

    Raises:
        SystemExit: If fewer than two input PDF files are provided.
    """
    parser = argparse.ArgumentParser(
        description="Concatenate multiple PDF files into a single output PDF.",
        epilog="Example: python main.py file1.pdf file2.pdf -o merged.pdf"
    )
    parser.add_argument(
        'input_pdfs', nargs='+', metavar='PDF',
        help='Input PDF file paths (2 or more)'
    )
    parser.add_argument(
        '-o', '--output', required=True, metavar='OUTPUT',
        help='Output PDF file path'
    )
    args = parser.parse_args()
    if len(args.input_pdfs) < 2:
        parser.error("Please provide at least two input PDF files.")
    concat_pdfs(args.input_pdfs, args.output)

if __name__ == "__main__":
    main()

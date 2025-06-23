import sys
import argparse
from concat_pdf.concat_pdf import concat_pdfs

def main():
    parser = argparse.ArgumentParser(description="Concatenate multiple PDF files.")
    parser.add_argument('input_pdfs', nargs='+', help='Input PDF file paths (2 or more)')
    parser.add_argument('-o', '--output', required=True, help='Output PDF file path')
    args = parser.parse_args()
    if len(args.input_pdfs) < 2:
        print("Please provide at least two input PDF files.")
        sys.exit(1)
    concat_pdfs(args.input_pdfs, args.output)

if __name__ == "__main__":
    main()

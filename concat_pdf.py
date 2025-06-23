import sys
import argparse
import PyPDF2


def concat_pdfs(input_pdfs, output_pdf):
    print("DEBUG: concat_pdfs called with:", input_pdfs, output_pdf)
    pdf_merger = PyPDF2.PdfMerger()
    errors = []
    appended = 0
    for pdf_path in input_pdfs:
        try:
            with open(pdf_path, "rb") as f:
                pdf_merger.append(f)
                appended += 1
        except Exception as e:
            print(f"Error reading {pdf_path}: {e}")
            errors.append(pdf_path)
    if appended == 0:
        print("No valid PDF files to merge.")
        return False
    try:
        with open(output_pdf, "wb") as output_file:
            pdf_merger.write(output_file)
        print(f"Merged PDF saved as: {output_pdf}")
        if errors:
            print(f"Some files could not be read: {errors}")
    except Exception as e:
        print(f"Failed to write merged PDF: {e}")
        return False
    print("DEBUG: concat_pdfs returning True")
    return True


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

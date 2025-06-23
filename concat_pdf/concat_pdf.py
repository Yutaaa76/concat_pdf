import PyPDF2
from typing import List, Optional

def concat_pdfs(input_pdfs: List[str], output_pdf: str) -> bool:
    """
    Concatenates multiple PDF files into a single output PDF.

    Args:
        input_pdfs: List of paths to input PDF files.
        output_pdf: Path to save the concatenated PDF file.

    Returns:
        True if at least one file was merged, False otherwise.
    """
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

def split_pdf(input_pdf: str, output_dir: str) -> Optional[List[str]]:
    """
    Splits a PDF into single-page PDFs in the specified output directory.

    Args:
        input_pdf: Path to the input PDF file.
        output_dir: Directory to save the split PDF files.

    Returns:
        List of output file paths, or None if error.
    """
    try:
        with open(input_pdf, "rb") as infile:
            reader = PyPDF2.PdfReader(infile)
            output_files = []
            for i, page in enumerate(reader.pages):
                writer = PyPDF2.PdfWriter()
                writer.add_page(page)
                out_path = f"{output_dir}/page_{i+1}.pdf"
                with open(out_path, "wb") as out:
                    writer.write(out)
                output_files.append(out_path)
        print(f"Split {input_pdf} into {len(output_files)} pages.")
        return output_files
    except Exception as e:
        print(f"Failed to split PDF: {e}")
        return None

def extract_pages(input_pdf: str, page_numbers: List[int], output_pdf: str) -> bool:
    """
    Extracts specific pages from a PDF and saves them to a new PDF.

    Args:
        input_pdf: Path to the input PDF file.
        page_numbers: List of 1-based page numbers to extract.
        output_pdf: Path to save the extracted pages PDF.

    Returns:
        True if successful, False otherwise.
    """
    try:
        with open(input_pdf, "rb") as infile:
            reader = PyPDF2.PdfReader(infile)
            writer = PyPDF2.PdfWriter()
            for num in page_numbers:
                if 1 <= num <= len(reader.pages):
                    writer.add_page(reader.pages[num - 1])
                else:
                    print(f"Page number {num} is out of range.")
            with open(output_pdf, "wb") as out:
                writer.write(out)
        print(f"Extracted pages {page_numbers} from {input_pdf} to {output_pdf}.")
        return True
    except Exception as e:
        print(f"Failed to extract pages: {e}")
        return False

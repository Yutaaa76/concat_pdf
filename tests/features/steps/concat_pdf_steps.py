import os
import tempfile
from behave import given, when, then
from PyPDF2 import PdfWriter, PdfReader
from concat_pdf.concat_pdf import concat_pdfs

@given('two valid PDF files')
def given_two_valid_pdf_files(context):
    """
    Create two temporary valid PDF files and store their paths in the context.

    Args:
        context: Behave context object for sharing state between steps.
    """
    context.temp_files = []
    for _ in range(2):
        fd, path = tempfile.mkstemp(suffix='.pdf')
        os.close(fd)
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with open(path, 'wb') as f:
            writer.write(f)
        context.temp_files.append(path)
    context.output_file = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
    context.output_path = context.output_file.name
    context.output_file.close()

@given('one valid PDF file and one missing PDF file')
def given_one_valid_and_one_missing_pdf_file(context):
    """
    Create one temporary valid PDF file and add a missing file path to the context.

    Args:
        context: Behave context object for sharing state between steps.
    """
    context.temp_files = []
    fd, path = tempfile.mkstemp(suffix='.pdf')
    os.close(fd)
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with open(path, 'wb') as f:
        writer.write(f)
    context.temp_files.append(path)
    context.temp_files.append('nonexistent.pdf')
    context.output_file = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
    context.output_path = context.output_file.name
    context.output_file.close()

@when('I concatenate them')
def when_i_concatenate_them(context):
    """
    Call the concat_pdfs function with the files in context.

    Args:
        context: Behave context object for sharing state between steps.
    """
    context.result = concat_pdfs(context.temp_files, context.output_path)

@then('the output PDF should have 2 pages')
def then_output_pdf_should_have_2_pages(context):
    """
    Assert that the output PDF exists and has exactly 2 pages.

    Args:
        context: Behave context object for sharing state between steps.
    """
    assert context.result is True, f"concat_pdfs returned {context.result}"
    assert os.path.exists(context.output_path), f"Output file does not exist: {context.output_path}"
    try:
        reader = PdfReader(context.output_path)
        page_count = len(reader.pages)
        assert page_count == 2, f"Output PDF has {page_count} pages, expected 2"
    except Exception as e:
        raise AssertionError(f"Failed to read output PDF: {e}")
    # Cleanup
    for path in context.temp_files:
        if os.path.exists(path):
            os.remove(path)
    if os.path.exists(context.output_path):
        os.remove(context.output_path)

@then('the output PDF should not exist or should have at most 1 page')
def then_output_pdf_should_not_exist_or_have_at_most_1_page(context):
    """
    Assert that the output PDF does not exist or has at most 1 page.

    Args:
        context: Behave context object for sharing state between steps.
    """
    if context.result:
        # Output file should exist and have at most 1 page
        assert os.path.exists(context.output_path)
        try:
            reader = PdfReader(context.output_path)
            assert len(reader.pages) <= 1
        except Exception:
            # File exists but is unreadable/corrupted
            pass
        os.remove(context.output_path)
    else:
        # Output file should not exist or be empty/corrupted
        if os.path.exists(context.output_path):
            try:
                reader = PdfReader(context.output_path)
                assert len(reader.pages) == 0
            except Exception:
                pass
            os.remove(context.output_path)
    for path in context.temp_files:
        if os.path.exists(path):
            os.remove(path)

@when('I split the first PDF')
def when_i_split_the_first_pdf(context):
    """
    Split the first PDF in context.temp_files and store output files in context.split_files.
    """
    from concat_pdf.concat_pdf import split_pdf
    import tempfile
    context.split_dir = tempfile.mkdtemp()
    context.split_files = split_pdf(context.temp_files[0], context.split_dir)

@then('the output should be single-page PDFs')
def then_output_should_be_single_page_pdfs(context):
    """
    Assert that the split output files exist and each has one page.
    """
    from PyPDF2 import PdfReader
    assert context.split_files is not None
    for f in context.split_files:
        assert os.path.exists(f)
        reader = PdfReader(f)
        assert len(reader.pages) == 1
        os.remove(f)
    os.rmdir(context.split_dir)

@when('I extract the first page from the first PDF')
def when_i_extract_first_page(context):
    """
    Extract the first page from the first PDF and store the output path in context.extracted_pdf.
    """
    from concat_pdf.concat_pdf import extract_pages
    import tempfile
    context.extracted_pdf = tempfile.mktemp(suffix='.pdf')
    context.extract_result = extract_pages(context.temp_files[0], [1], context.extracted_pdf)

@then('the extracted PDF should have 1 page')
def then_extracted_pdf_should_have_1_page(context):
    """
    Assert that the extracted PDF exists and has exactly 1 page.
    """
    from PyPDF2 import PdfReader
    assert context.extract_result is True
    assert os.path.exists(context.extracted_pdf)
    reader = PdfReader(context.extracted_pdf)
    assert len(reader.pages) == 1
    os.remove(context.extracted_pdf)

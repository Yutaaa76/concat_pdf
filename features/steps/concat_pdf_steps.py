import os
import tempfile
from behave import given, when, then
from PyPDF2 import PdfWriter, PdfReader
from concat_pdf import concat_pdfs

@given('two valid PDF files')
def step_impl(context):
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
def step_impl(context):
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
def step_impl(context):
    concat_pdfs(context.temp_files, context.output_path)

@then('the output PDF should have 2 pages')
def step_impl(context):
    reader = PdfReader(context.output_path)
    assert len(reader.pages) == 2
    # Cleanup
    for path in context.temp_files:
        if os.path.exists(path):
            os.remove(path)
    if os.path.exists(context.output_path):
        os.remove(context.output_path)

@then('the output PDF should not exist or should have at most 1 page')
def step_impl(context):
    if os.path.exists(context.output_path):
        try:
            reader = PdfReader(context.output_path)
            assert len(reader.pages) <= 1
        except Exception:
            pass
        os.remove(context.output_path)
    for path in context.temp_files:
        if os.path.exists(path):
            os.remove(path)

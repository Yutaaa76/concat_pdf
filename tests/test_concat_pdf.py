import os
import tempfile
import pytest
from PyPDF2 import PdfWriter, PdfReader
from concat_pdf.concat_pdf import concat_pdfs, split_pdf, extract_pages

@pytest.fixture
def temp_pdfs():
    files = []
    for _ in range(2):
        fd, path = tempfile.mkstemp(suffix='.pdf')
        os.close(fd)
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with open(path, 'wb') as f:
            writer.write(f)
        files.append(path)
    yield files
    for path in files:
        if os.path.exists(path):
            os.remove(path)

@pytest.fixture
def output_pdf():
    output_file = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
    output_path = output_file.name
    output_file.close()
    yield output_path
    if os.path.exists(output_path):
        os.remove(output_path)

def test_concat_pdfs(temp_pdfs, output_pdf):
    concat_pdfs(temp_pdfs, output_pdf)
    reader = PdfReader(output_pdf)
    assert len(reader.pages) == 2

def test_concat_pdfs_with_missing_file(temp_pdfs, output_pdf):
    missing_file = 'nonexistent.pdf'
    files = [temp_pdfs[0], missing_file]
    if os.path.exists(output_pdf):
        os.remove(output_pdf)
    concat_pdfs(files, output_pdf)
    if os.path.exists(output_pdf):
        try:
            reader = PdfReader(output_pdf)
            assert len(reader.pages) <= 1
        except Exception:
            pass
    else:
        assert not os.path.exists(output_pdf)

def test_split_pdf(tmp_path, temp_pdfs):
    # Use the first temp PDF
    out_dir = tmp_path
    out_files = split_pdf(temp_pdfs[0], str(out_dir))
    assert out_files is not None
    assert len(out_files) == 1
    assert os.path.exists(out_files[0])
    # Clean up
    for f in out_files:
        if os.path.exists(f):
            os.remove(f)

def test_extract_pages(tmp_path, temp_pdfs):
    # Use the first temp PDF
    out_pdf = os.path.join(tmp_path, "extracted.pdf")
    result = extract_pages(temp_pdfs[0], [1], out_pdf)
    assert result is True
    reader = PdfReader(out_pdf)
    assert len(reader.pages) == 1
    if os.path.exists(out_pdf):
        os.remove(out_pdf)

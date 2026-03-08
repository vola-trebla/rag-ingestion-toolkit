import pdfplumber


def parse_pdf(filepath: str) -> str:
    with pdfplumber.open(filepath) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
        return " ".join(filter(None, pages))


def process_pdf_file(filepath: str) -> str:
    return parse_pdf(filepath)

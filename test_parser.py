from parsers.html_parser import process_html_file
from parsers.md_parser import process_markdown_file
from parsers.pdf_parser import process_pdf_file

result = process_html_file("input/test.html")
print(result)

result_md = process_markdown_file("input/test.md")
print(result_md)

result_pdf = process_pdf_file("input/test.pdf")
print(result_pdf)

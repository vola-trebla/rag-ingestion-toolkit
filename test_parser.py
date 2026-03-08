from parsers.html_parser import process_html_file
from parsers.md_parser import process_markdown_file

result = process_html_file("input/test.html")
print(result)

result_md = process_markdown_file("input/test.md")
print(result_md)
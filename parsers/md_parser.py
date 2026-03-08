import markdown
from parsers.html_parser import parse_html


def parse_markdown(md_content: str) -> str:
    html_content = markdown.markdown(md_content)
    return parse_html(html_content)


def load_markdown_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def process_markdown_file(filepath: str) -> str:
    md_content = load_markdown_file(filepath)
    return parse_markdown(md_content)

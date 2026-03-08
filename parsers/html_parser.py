from bs4 import BeautifulSoup


def parse_html(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "lxml")

    # remove noise
    for tag in soup(["nav", "footer", "header", "script", "style", "title"]):
        tag.decompose()

    return soup.get_text(separator=" ", strip=True)


def load_html_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def process_html_file(filepath: str) -> str:
    html_content = load_html_file(filepath)
    return parse_html(html_content)

import os
from parsers.html_parser import process_html_file
from parsers.md_parser import process_markdown_file
from parsers.pdf_parser import process_pdf_file
from chunkers.chunker import chunk_by_sentences
from extractors.metadata_extractor import extract_simple_metadata, extract_llm_metadata


def run_pipeline(filepath: str, mode: str = "simple") -> list[dict]:
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".html":
        text = process_html_file(filepath)
    elif ext == ".md":
        text = process_markdown_file(filepath)
    elif ext == ".pdf":
        text = process_pdf_file(filepath)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    chunks = chunk_by_sentences(text, sentences_per_chunk=3)

    results = []
    for chunk in chunks:
        if mode == "llm":
            metadata = extract_llm_metadata(chunk)
        else:
            metadata = extract_simple_metadata(chunk)
        results.append({"text": chunk, "metadata": metadata})

    return results

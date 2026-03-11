# rag-ingestion-toolkit

Clean data pipeline for RAG systems. Converts raw HTML, PDF, and Markdown into chunked, embedding-ready output with metadata extraction.

## Problem

90% of RAG systems have poor retrieval quality because raw documents are fed directly into embedding models. This toolkit solves the data preparation step that most developers skip.

## How it works

```
Input File (HTML / PDF / Markdown)
        ↓
   Parser (format-specific noise removal)
        ↓
   Raw Clean Text
        ↓
   Chunker (fixed-size or sentence-based)
        ↓
   Text Chunks
        ↓
   Metadata Extractor (simple stats or LLM-powered)
        ↓
   List of { text, metadata } dicts → ready for embedding
```

## Modules

### Parsers (`parsers/`)

| Parser | File | What it does |
|--------|------|-------------|
| HTML | `html_parser.py` | Strips noise tags (`nav`, `footer`, `header`, `script`, `style`, `title`), extracts clean text via BeautifulSoup + lxml |
| Markdown | `md_parser.py` | Converts Markdown → HTML, then reuses the HTML parser for noise removal |
| PDF | `pdf_parser.py` | Extracts text from all pages using pdfplumber |

Each parser exposes a `process_*_file(filepath)` function that takes a file path and returns clean text.

### Chunkers (`chunkers/`)

| Strategy | Function | Description |
|----------|----------|-------------|
| Fixed-size | `chunk_by_size(text, chunk_size, overlap)` | Splits text into character-level chunks with configurable overlap (sliding window) |
| Sentence-based | `chunk_by_sentences(text, sentences_per_chunk)` | Groups sentences into chunks by count, splitting on `. ` |

### Metadata Extractors (`extractors/`)

| Mode | Function | Description |
|------|----------|-------------|
| Simple | `extract_simple_metadata(text)` | Returns `char_count`, `word_count`, `sentence_count` — no API calls |
| LLM | `extract_llm_metadata(text)` | Uses Claude Haiku to extract `topic`, `key_entities`, `sentiment` as JSON |

### Pipeline (`pipeline.py`)

`run_pipeline(filepath, mode="simple")` — main entry point that ties everything together:

1. Detects file type by extension (`.html`, `.pdf`, `.md`)
2. Parses the file with the appropriate parser
3. Chunks text into sentences (3 sentences per chunk)
4. Extracts metadata for each chunk (simple or LLM mode)
5. Returns a list of dicts:

```python
[
    {
        "text": "Chunk text here...",
        "metadata": {"char_count": 42, "word_count": 8, "sentence_count": 2}
    },
    ...
]
```

## Quick start

```bash
# clone and setup
git clone https://github.com/vola-trebla/rag-ingestion-toolkit.git
cd rag-ingestion-toolkit
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# for LLM mode: add your API key
echo "ANTHROPIC_API_KEY=your-key-here" > .env
```

### Usage

```python
from pipeline import run_pipeline

# simple mode (no API calls)
results = run_pipeline("input/test.html")

# LLM mode (requires ANTHROPIC_API_KEY)
results = run_pipeline("input/test.html", mode="llm")

for r in results:
    print(r["text"])
    print(r["metadata"])
```

### Using individual components

```python
from parsers.html_parser import process_html_file
from chunkers.chunker import chunk_by_size, chunk_by_sentences
from extractors.metadata_extractor import extract_simple_metadata

# parse
text = process_html_file("input/test.html")

# chunk
chunks = chunk_by_sentences(text, sentences_per_chunk=3)
# or: chunks = chunk_by_size(text, chunk_size=500, overlap=50)

# extract metadata
for chunk in chunks:
    meta = extract_simple_metadata(chunk)
    print(meta)
```

## Requirements

- Python 3.13+
- beautifulsoup4, lxml — HTML parsing
- pdfplumber — PDF extraction
- markdown — Markdown conversion
- anthropic, python-dotenv — LLM metadata extraction

## Development

```bash
# lint & format
ruff check --fix .
ruff format .
```

Pre-commit hooks run `ruff format` automatically on each commit.

## Project structure

```
rag-ingestion-toolkit/
├── parsers/
│   ├── html_parser.py
│   ├── md_parser.py
│   └── pdf_parser.py
├── chunkers/
│   └── chunker.py
├── extractors/
│   └── metadata_extractor.py
├── pipeline.py
├── test_parser.py
├── requirements.txt
├── .pre-commit-config.yaml
└── .github/workflows/
    └── lint.yml          # ruff CI on PRs
```

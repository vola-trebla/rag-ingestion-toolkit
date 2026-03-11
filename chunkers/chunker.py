def chunk_by_size(text: str, chunk_size: int, overlap: int) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start : start + chunk_size]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def chunk_by_sentences(text: str, sentences_per_chunk: int) -> list[str]:
    sentences = text.split(". ")
    chunks = []
    start = 0
    while start < len(sentences):
        chunks.append(". ".join(sentences[start : start + sentences_per_chunk]))
        start += sentences_per_chunk
    return chunks

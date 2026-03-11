from chunkers.chunker import chunk_by_sentences


# chunks = chunk_by_size("ABCDEFGHIJKLMNO", 5, 2)
# for i, chunk in enumerate(chunks):
#     print(f"chunk {i}: {chunk}")

chunks = chunk_by_sentences(
    "Milk costs 89 rub. Kefir costs 75 rub. Yogurt costs 120 rub.", 2
)
for i, chunk in enumerate(chunks):
    print(f"chunk {i}: {chunk}")

# result = process_html_file("input/test.html")
# print(result)

# result_md = process_markdown_file("input/test.md")
# print(result_md)

# result_pdf = process_pdf_file("input/test.pdf")
# print(result_pdf)

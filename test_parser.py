from extractors.metadata_extractor import extract_llm_metadata, extract_simple_metadata


# result = process_html_file("input/test.html")
# print(result)

# result_md = process_markdown_file("input/test.md")
# print(result_md)

# result_pdf = process_pdf_file("input/test.pdf")
# print(result_pdf)


text = "Milk costs 89 rub per liter. Kefir costs 75 rub. Yogurt costs 120 rub."

print(extract_simple_metadata(text))
print(extract_llm_metadata(text))

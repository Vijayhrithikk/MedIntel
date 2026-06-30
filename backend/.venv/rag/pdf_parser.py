import fitz

def extract_text(pdf_path: str):
    with fitz.open(pdf_path) as document:
        print("Pages:", len(document))

        pages_text = []

        for i, page in enumerate(document):
            text = page.get_text()

            print(f"Page {i + 1} characters:", len(text))

            pages_text.append(text)

        full_text = "".join(pages_text)

        print("Total characters:", len(full_text))

        return {
            "pages": len(document),
            "characters": len(full_text),
            "text": full_text,
        }
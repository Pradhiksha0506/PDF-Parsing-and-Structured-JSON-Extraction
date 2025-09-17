import pdfplumber
import camelot
import json
import argparse


def extract_paragraphs(pdf_path):
    paragraphs = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:
                for para in text.split("\n"):
                    if para.strip():
                        paragraphs.append({
                            "page_number": page_num,
                            "type": "paragraph",
                            "section": None,      
                            "sub_section": None,
                            "text": para.strip()
                        })
    return paragraphs

def extract_tables(pdf_path):
    tables = []
    try:
        all_tables = camelot.read_pdf(pdf_path, pages="all")
        for i, table in enumerate(all_tables):
            tables.append({
                "page_number": int(table.parsing_report["page"]),
                "type": "table",
                "section": None,
                "description": None,
                "table_data": table.df.values.tolist()
            })
    except Exception as e:
        print("⚠️ No tables found or error:", e)
    return tables


def parse_pdf_to_json(pdf_path, output_json="output.json"):
    json_data = {"pages": []}

    paragraphs = extract_paragraphs(pdf_path)
    tables = extract_tables(pdf_path)

    pages = {}
    for item in paragraphs + tables:
        page_num = item["page_number"]
        if page_num not in pages:
            pages[page_num] = {"page_number": page_num, "content": []}
        pages[page_num]["content"].append(item)

    
    json_data["pages"] = [pages[p] for p in sorted(pages.keys())]

    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)

    print(f" JSON saved as {output_json}")
    return json_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse PDF into structured JSON")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("output_json", help="Path to save JSON output")

    args = parser.parse_args()
    parse_pdf_to_json(args.pdf_path, args.output_json)

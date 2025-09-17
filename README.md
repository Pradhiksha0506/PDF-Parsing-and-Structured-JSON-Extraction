PDF Parsing and Structured JSON Extraction

Table of Contents

Introduction
Project Objective
Methodology
Technologies Used
Program Flow
Results

1. Introduction

Extracting information from PDF files is often challenging due to the unstructured nature of the content. This project provides a solution by parsing PDF documents and converting them into a structured JSON format. The extracted JSON maintains a page-level hierarchy while categorizing content into paragraphs, tables, and charts, making the data easier to analyze and process programmatically.

2. Project Objective

The objective of this project is to build a Python-based program that: Accepts a PDF file as input.

Accepts a PDF file as input.
Extracts content such as paragraphs, tables, and charts.
Preserves the hierarchical structure of the document.
Saves the output into a clean and readable JSON format.
3. Methodology

The program follows a pipeline that includes:

Text Extraction: Using pdfplumber, text is extracted from each page and stored as paragraphs.
Table Extraction: Using camelot, tables are identified and extracted as structured data.
JSON Structuring: Content is organized at a page level, including type (paragraph, table, chart), section names, and sub-sections if available.
Output Generation: The structured data is exported into a JSON file.
4. Technologies Used

Python 3.9+
pdfplumber – for paragraph and text extraction.
Camelot – for table extraction from PDFs.
json – for generating structured JSON files.
Ghostscript – required dependency for Camelot (to handle PDF processing).
5. Program Flow

Install dependencies: pip install pdfplumber camelot-py[cv]

Run the program from terminal or VS Code: python pdf_parser.py input.pdf output.json

The script extracts paragraphs and tables, preserves page hierarchy, and saves the results in the specified JSON file.

6. Results

The program successfully extracts and organizes PDF content into a well-structured JSON format.

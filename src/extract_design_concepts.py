import fitz  # PyMuPDF
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()


# Set up OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a PDF file."""
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

def get_design_concepts(text):
    """Uses OpenAI API to extract design concepts from text."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in design concepts."},
            {"role": "user", "content": f"Extract all relevant design concepts from the following text: {text}"}
        ]
    )
    print(response)
    concepts = response.choices[0].message.content
    return concepts

def main(pdf_paths, output_file):
    """Main function to process PDFs and save extracted design concepts to a .txt file."""
    all_concepts = ""
    for pdf_path in pdf_paths:
        print(f"Processing {pdf_path}...")
        text = extract_text_from_pdf(pdf_path)
        concepts = get_design_concepts(text)
        all_concepts += concepts + "\n\n"
    
    with open(output_file, 'w') as file:
        file.write(all_concepts)

if __name__ == "__main__":
    pdf_paths = ['data/design_concepts/1.pdf', 'data/design_concepts/2.pdf', 'data/design_concepts/3.pdf', 'data/design_concepts/4.pdf']  # Add your PDF paths here
    output_file = 'data/design_concepts.txt'
    main(pdf_paths, output_file)
    print(f"Design concepts have been saved to {output_file}")

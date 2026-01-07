
import PyPDF2

def extract_text_from_pdf(pdf_path):
    extracted_text = ""

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text

    return extracted_text
pdf_path = "CV.pdf"
extract_text_from_pdf(pdf_path)
from google import genai
client = genai.Client(api_key = "AIzaSyDBf0DR_wQLiUohkV0lHE-LHFR53AbhV2w")
response = client.models.generate_content(model = "gemini-2.5-flash",contents = text + "assume yourself as a resume evaluator and give score to it for 100 percent and also give advantages and disadvantages and give it in line by line")
response.text
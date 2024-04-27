import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import GetRelativePath as gr


def scrape_text(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p', class_='paragraph inline-placeholder')
        
        combined_text = '\n'.join(paragraph.get_text(strip=True) for paragraph in paragraphs)

        save_text_as_pdf(combined_text, gr.resource_path("db\\pdf\\news.pdf"))

def save_text_as_pdf(text, filename):
    # Create a canvas object with specified filename
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Set font and font size
    c.setFont("Helvetica", 12)
    
    # Split text into lines to fit within the page width
    lines = text.split('\n')
    
    # Define starting position for text
    y = 720
    
    # Write each line of text on the PDF
    for line in lines:
        c.drawString(72, y, line)
        y -= 15  # Move to the next line (adjust spacing as needed)
    
    # Save the canvas (i.e., generate the PDF file)
    c.save()

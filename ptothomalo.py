from bs4 import BeautifulSoup
import requests

# Replace 'your_url_here' with the URL where your HTML content is located
url = 'https://www.prothomalo.com/bangladesh/sgdvna4je1'

# Send a GET request to fetch the HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the div containing the text (adjust the CSS selector based on your HTML structure)
text_div = soup.find('div', class_='story-element-text')

# Initialize an empty string to accumulate the extracted text
extracted_text = ''

# If the text_div is found, extract the text inside all <p> tags within the div
if text_div:
    paragraphs = text_div.find_all('p')
    for paragraph in paragraphs:
        extracted_text += paragraph.get_text() + '\n'  # Add each paragraph's text to the result

# Specify the output file path where the extracted text will be saved
output_file_path = 'extracted_text.txt'

# Write the extracted text to a .txt file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print(f"Extracted text saved to: {output_file_path}")

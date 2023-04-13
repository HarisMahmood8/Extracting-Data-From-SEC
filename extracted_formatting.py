import csv
from sec_api import ExtractorApi
from bs4 import BeautifulSoup

extractorApi = ExtractorApi("ENTER SEC API HERE")

filing_url = "https://www.sec.gov/Archives/edgar/data/1318605/000156459021004599/tsla-10k_20201231.htm"

section_text = extractorApi.get_section(filing_url, "1A", "text")

section_html = extractorApi.get_section(filing_url, "7", "html")

soup = BeautifulSoup(section_html, 'html.parser')
section_text_html_stripped = soup.get_text()

with open('sec_data.csv', mode='w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Section', 'Content'])
    writer.writerow(['1A', section_text])
    writer.writerow(['7', section_text_html_stripped])
    
print("Data extracted ti sec_data.csv")









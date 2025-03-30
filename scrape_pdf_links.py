#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import time
from random import randint
from urllib.parse import urljoin

def extract_pdf_links(url):
    try:

        # Add delay to be nice to the server
        time.sleep(randint(1,5))
        
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links
        pdf_links = []
        for link in soup.find_all('a'):
            href = link.get('href').lower()
            # only include links that contain .pdf and are from the specified domains
            if '.pdf' in href and ('bsi.bund.de' in href or 'etsi.org' in href):
                # Convert relative URLs to absolute
                full_url = urljoin(url, href)
                pdf_links.append(full_url)
                
        return pdf_links
        
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return []

def main():
    list_of_all_trs = 'data/tr-list.txt'
    list_of_all_pdfs = 'data/pdf_links.txt'

    # Get all TR URLs
    with open(list_of_all_trs, 'r') as f:
        urls = f.readlines()
    
    # Clean URLs
    urls = [url.strip() for url in urls]
    
    # Store results
    with open(list_of_all_pdfs, 'w') as f:
        for url in urls:
            print(f"Processing: {url}")
            pdf_links = extract_pdf_links(url)
            
            if pdf_links:
                for pdf in pdf_links:
                    f.write(f"{pdf}\n")
                f.flush()  # Ensure writing to disk

if __name__ == "__main__":
    main()

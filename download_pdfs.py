#!/usr/bin/env python3

import os
import requests
from tqdm import tqdm
from urllib.parse import unquote
import re

def clean_filename(url):
    filename = os.path.basename(unquote(url))
    filename = re.sub(r'[^\w\-_\. ]', '_', filename)
    filename = filename.split('.pdf')[0]
    return filename + '.pdf'

def download_file(url, dest_folder):
    try:
        
        # Send a HEAD request first to get the file size
        response = requests.head(url, allow_redirects=True)
        total_size = int(response.headers.get('content-length', 0))
        
        # Get the filename from the URL
        filename = clean_filename(url)
        filepath = os.path.join(dest_folder, filename)
        
        # Start the download with progress bar
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f, tqdm(
            desc=filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as progressbar:
            for data in response.iter_content(chunk_size=1024):
                size = f.write(data)
                progressbar.update(size)

    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")


def main():
    list_of_pdf_urls = 'data/pdf_links.txt'

    # Create downloads directory
    download_dir = os.path.join(os.path.dirname(__file__), 'pdf')
    os.makedirs(download_dir, exist_ok=True)
    
    # Read and parse pdf_links.txt
    pdf_urls = []
    with open(list_of_pdf_urls, 'r') as f:
        for line in f:
            if '.pdf' in line.strip():
                pdf_urls.append(line.strip())
    
    print(f"Found {len(pdf_urls)} PDFs to download")
    
    # Download files with progress bar
    with tqdm(total=len(pdf_urls), desc="Overall Progress", unit="file") as progressbar:
        for url in pdf_urls:
            download_file(url, download_dir)
            progressbar.update(1)

if __name__ == "__main__":
    main()

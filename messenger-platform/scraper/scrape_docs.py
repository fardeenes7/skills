import os
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from lxml import html

# Configuration
URLS_FILE = "../references/urls.txt"
OUTPUT_DIR = "scraped_content"
TARGET_DIV_ID = "documentation_body_pagelet"
FALLBACK_XPATH = "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div[2]"

def clean_filename(title):
    # Remove characters that are not alphanumeric, spaces, or hyphens
    title = re.sub(r'[^\w\s-]', '', title)
    # Replace spaces with underscores
    title = re.sub(r'\s+', '_', title).strip()
    return title

def scrape_page(url):
    print(f"Scraping: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse with BeautifulSoup for title and primary div
        soup = BeautifulSoup(response.content, 'lxml')
        
        # Get Title
        title_tag = soup.find('title')
        title = title_tag.get_text() if title_tag else "untitled"
        filename = clean_filename(title) + ".md"
        
        # Find the target div
        content_div = soup.find('div', id=TARGET_DIV_ID)
        
        markdown_content = None
        
        if content_div:
            # Convert to markdown
            markdown_content = md(str(content_div), heading_style="ATX")
        else:
            print(f"Primary div#{TARGET_DIV_ID} not found. Retrying with fallback XPath...")
            # Use lxml for XPath
            tree = html.fromstring(response.content)
            elements = tree.xpath(FALLBACK_XPATH)
            if elements:
                # Convert the lxml element back to HTML string for markdownify
                element_html = html.tostring(elements[0], encoding='unicode')
                markdown_content = md(element_html, heading_style="ATX")
            else:
                print(f"Warning: Fallback XPath also failed for {url}")

        if markdown_content:
            # Save to file
            os.makedirs(OUTPUT_DIR, exist_ok=True)
            filepath = os.path.join(OUTPUT_DIR, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"Source: {url}\n\n")
                f.write(markdown_content)
            
            print(f"Saved to: {filepath}")
            
    except Exception as e:
        print(f"Error scraping {url}: {e}")

def main():
    if not os.path.exists(URLS_FILE):
        print(f"Error: {URLS_FILE} not found.")
        return

    with open(URLS_FILE, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('Created At:') and not line.startswith('Completed At:') and not line.startswith('File Path:')]

    for url in urls:
        scrape_page(url)

if __name__ == "__main__":
    main()

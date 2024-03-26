import requests
from bs4 import BeautifulSoup


def crawl_and_save(url, filename):
    # Retrieve HTML content from URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parsing HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Save the HTML content into a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"Successfully save the crawling result from {url} to {filename}")
    else:
        print(f"Failed crawling of {url}")


# The website to be crawled and the file name to save the result
websites = [
    {"url": "https://cmlabs.co", "filename": "cmlabs_crawled.html"},
    {"url": "https://sequence.day", "filename": "sequence_day_crawled.html"}
]

# Perform crawling for each website
for website in websites:
    crawl_and_save(website["url"], website["filename"])

# CMLabs Backend Crawler Freelance Test

This project is a simple web crawler implemented in Python. It crawls the specified websites and saves the HTML content into separate files.

## Description

This Python script retrieves the HTML content from the specified URLs using the `requests` library and then parses the HTML content using `BeautifulSoup`. It saves the HTML content into separate files using the provided filenames.

## How to use

Steps to use or run this project. These include:

1. Ensure you have Python installed on your system.

2. Install dependencies by running the command:
   ```bash
   pip install -r requirements.txt

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

4. Run the Python script:
   ```bash
   python main.py
   ```
   
5. The crawling results will be saved into HTML files (cmlabs_crawled.html, sequence_day_crawled.html, and python_org_crawled.html).

6. To view the crawling results in a web browser:
   ```
   - Open the HTML file using a web browser of your choice. 
   - You can do this by double-clicking on the HTML file, 
   - or by right-clicking and selecting "Open with" 
     and choosing your preferred web browser.
   - or "Open in" -> "Browser" on your code editor (PyCharm)
     and choosing your preferred web browser.
   ```

## Directory Structure

A description of the directory structure of this project. This includes:

```
.
├── venv/
├── .gitignore
├── cmlabs_crawled.html
├── main.py
├── python_org_crawled.html
├── README.md
├── requirements.txt
└── sequence_day_crawled.html
```

## Contribution

If you would like to contribute to this project, please open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

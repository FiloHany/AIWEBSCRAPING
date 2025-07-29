import os
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

# Use environment variable for Bright Data credentials if set
AUTH = os.getenv('BRIGHTDATA_AUTH', 'brd-customer-hl_81a2698a-zone-scraping_browser1:qgfb8bhxerh5')
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

def scrape_website(website: str) -> str:
    """Scrape the given website using Selenium and Bright Data proxy."""
    print("Launching Chrome browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting for captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html

def extract_body_content(html_content: str) -> str:
    """Extract the <body> content from HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body_content: str) -> str:
    """Remove scripts/styles and clean up the body content."""
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_dom_content(dom_content: str, max_length: int = 6000) -> list:
    """Split DOM content into chunks for LLM processing."""
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]





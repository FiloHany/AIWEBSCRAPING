# AI Web Scrapping

A modern, AI-powered web scraping tool that extracts web page content and uses LLMs to parse and extract meaningful information. Built with Streamlit for a simple UI, Selenium for robust scraping, and LangChain+Ollama for advanced parsing.

## Features
- **Streamlit UI**: Simple, interactive web interface
- **Selenium Scraping**: Automates browser to bypass captchas and blocks
- **Bright Data Proxy**: Large-scale, reliable scraping
- **BeautifulSoup Cleaning**: Extracts and cleans page content
- **LLM Parsing**: Uses LangChain+Ollama to extract custom information

## Requirements
- Python 3.8+
- Chrome browser
- ChromeDriver (included)
- See `requirements.txt` for Python dependencies

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AIWebScrapping.git
   cd AIWebScrapping/AIWEBSCRAPPING
   ```
2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Start the Streamlit app**
   ```bash
   streamlit run code/main.py
   ```
2. **Enter a website URL** and click "Scrape Site".
3. **View and parse content** using the provided UI.

## Environment Variables
- If you use your own Bright Data credentials, set them in the code or via environment variables (see `scrape.py`).
- You may use a `.env` file for sensitive data (e.g., API keys, proxy credentials). Example:
  ```env
  BRIGHTDATA_AUTH=your_auth_here
  ```

## File Structure
- `code/main.py` - Streamlit UI and app logic
- `code/scrape.py` - Web scraping and cleaning functions
- `code/parse.py` - LLM-based parsing logic
- `code/chromedriver.exe` - ChromeDriver binary
- `requirements.txt` - Python dependencies

## Notes
- **Do not commit sensitive data** (API keys, credentials) to the repository.
- The included `chromedriver.exe` is for Windows. Download the correct version for your OS if needed.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE) (add a LICENSE file if needed)

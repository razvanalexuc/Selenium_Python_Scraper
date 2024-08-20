# Selenium Python Scraper

This project is a web scraper built using Python and Selenium. The scraper extracts book information from Audible's search results, including the book title, author, length, and release date. The extracted data is saved into a CSV file for further analysis.

## Prerequisites

- Python 3.8+
- Google Chrome browser installed

## Setup

1. **Clone the repository:**
   git clone https://github.com/razvanalexuc/Selenium_Python_Scraper.git
   cd Selenium_Python_Scraper
2. **Create and activate a virtual environment (optional but recommended):**
  python -m venv .venv
  source .venv/bin/activate    # On Windows: .venv\Scripts\activate
3. **Install the required Python packages:**
   pip install -r requirements.txt
4. **Run the scraper:**
  python src/main.py

## How It Works
- Selenium WebDriver: Used to automate the browser interactions.
- Pagination Handling: The scraper navigates through all pages of the search results to ensure complete data extraction.
- Error Handling: The scraper is designed to handle exceptions gracefully, ensuring that partial data is not lost.
## Troubleshooting
- NoSuchWindowException: This error may occur if the browser window closes unexpectedly. Make sure the browser window remains open throughout the scraping process.
- Data Not Saving: Ensure that the data/ directory exists and that you have the necessary permissions to write to this directory.
## Contributing
- Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
- This project is licensed under the MIT License. See the LICENSE file for more details.

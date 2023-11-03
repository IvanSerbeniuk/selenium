# Audible Web Scraping Project

This Python project is designed to scrape data from the Audible website, specifically audiobook details, and save the information to a CSV file.

## Getting Started

### Prerequisites

Before running this project, ensure that you have the following requirements:

- Python (3.x recommended)
- Selenium Python library
- Chrome WebDriver
- Pandas Python library

You can install Python packages using pip:
```shell
pip install selenium pandas
```
### Running the Project
1. Clone this repository or download the Python script and README.md file.

2. Install the required Python libraries.

3. Run the Python script:
```shell
python audible_scraper.py
```
4. The script will scrape audiobook details from Audible and save the data to a CSV file named amazon_books.csv.
   
## Project Details

The script navigates to the Audible website and scrapes audiobook information.

It automatically determines the number of pages and iterates through them to collect data.

Collected data includes audiobook title, author, and length.

Data is saved to a CSV file for further analysis or use.

## License
This project is licensed under the MIT [License](https://opensource.org/license/mit/) - see the LICENSE file for details.
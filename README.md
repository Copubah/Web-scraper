# Web Scraper 
- This is a Python script to scrape job listings from [www.myjobmag.co.ke](https://www.myjobmag.co.ke). The script extracts job details such as title, company, location, date posted, and job link, and saves the data into a CSV file.

## Features
- Scrapes job listings from multiple pages.
- Saves the scraped data into a CSV file (`jobs.csv`).
- Includes respectful delays between requests to avoid overloading the server.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Required Python libraries: `requests` and `beautifulsoup4`

## Installation
1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/your-username/myjobmage-scraper.git
   cd myjobmage-scraper
import requests
from bs4 import BeautifulSoup
import time
import csv

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_job_page(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Update these selectors based on actual website structure
        jobs = soup.find_all('div', class_='job-listing')  # Replace with actual class
        
        job_data = []
        for job in jobs:
            title = job.find('h2').text.strip()  # Update selector
            company = job.find('div', class_='company').text.strip()  # Update selector
            location = job.find('span', class_='location').text.strip()  # Update selector
            date_posted = job.find('span', class_='date').text.strip()  # Update selector
            link = job.find('a')['href']  # Update selector
            
            job_data.append({
                'title': title,
                'company': company,
                'location': location,
                'date_posted': date_posted,
                'link': link
            })
        
        return job_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return []

def scrape_multiple_pages(base_url, pages=1):
    all_jobs = []
    for page in range(1, pages + 1):
        print(f"Scraping page {page}")
        url = f"{base_url}?page={page}"  # Update pagination pattern if different
        page_jobs = scrape_job_page(url)
        all_jobs.extend(page_jobs)
        time.sleep(2)  # Respectful delay between requests
    
    return all_jobs

def save_to_csv(jobs, filename='jobs.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=jobs[0].keys())
        writer.writeheader()
        writer.writerows(jobs)

if __name__ == '__main__':
    # Replace with actual job listings URL
    BASE_URL = 'https://www.myjobmag.co.ke/jobs'
    
    # Scrape first 3 pages
    jobs = scrape_multiple_pages(BASE_URL, pages=3)
    
    if jobs:
        save_to_csv(jobs)
        print(f"Successfully scraped {len(jobs)} jobs")
    else:
        print("No jobs found")
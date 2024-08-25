import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_webdriver(chrome_driver_path):
    """Set up and return a Selenium WebDriver instance."""
    service = Service(executable_path=chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def extract_company_names(driver):
    """Extract and return a list of company names from the current page."""
    company_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p.typography_heading-xs__jSwUz'))
    )
    return [element.text for element in company_elements]


def extract_jobs(driver):
    """Extract and return a list of jobs from the current page."""
    job_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.typography_body-xs__9Yq3q'))
    )
    return [element.text for element in job_elements]


def scrape_data(url, chrome_driver_path, output_file='output.csv'):
    """Main function to scrape company names and job titles and save them to a CSV file."""
    driver = setup_webdriver(chrome_driver_path)
    driver.get(url)

    company_names = extract_company_names(driver)
    job_titles = extract_jobs(driver)

    driver.quit()

    data = pd.DataFrame({
        'Company Name': company_names,
        'Job Title': job_titles
    })

    data.to_csv(output_file, index=False)
    print(f"Data successfully saved to {output_file}")


if __name__ == "__main__":
    CHROME_DRIVER_PATH = '/path/to/chromedriver'
    URL = 'https://example.com/jobs'
    OUTPUT_FILE = 'scraped_jobs.csv'

    scrape_data(URL, CHROME_DRIVER_PATH, OUTPUT_FILE)

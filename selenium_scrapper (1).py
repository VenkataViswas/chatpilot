import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

def selenium_scrape_and_save_to_csv(url):
    """Scrapes a website using Selenium and extracts its content.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        str: The extracted content of the website.
    """

    try:
        # Initialize a WebDriver (e.g., Chrome)
        driver = webdriver.Chrome()
        # Navigate to the URL
        driver.get(url)
        # Allow JavaScript to execute
        driver.implicitly_wait(10)  # Wait for up to 10 seconds


        # Extract content using BeautifulSoup or other methods
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content = soup.get_text()  # Example: extract all text
        
        # total_content
        content = content.replace('\u200e', '')
        content = content.replace('\u200e', '')
        content = content.replace('\n', '')
        with open("selenium_output.txt", "w", encoding="utf-8") as file:
            file.write(content) 

        # links
        links = soup.find_all('a')
        with open("selenium_output[routes].csv", mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Link Text', 'URL'])

            for link in links:
                text = link.get_text(strip=True)
                href = link.get('href')
                csv_writer.writerow([text, href])

        #images
        images = soup.find_all('img')
        with open("selenium_output[images].csv", mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Alt text','Image URLs'])
            
            for image in images:
                alt_text = image.get('alt')
                src = image.get('src')
                csv_writer.writerow([alt_text, src])

        # Close the WebDriver
        driver.quit()

        return content
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Example usage:
url = "https://www.apple.com/"
content = selenium_scrape_and_save_to_csv(url)
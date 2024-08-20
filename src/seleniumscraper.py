from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import time
import os

def get_products():
    website = "https://www.audible.com/search"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(website)
    driver.maximize_window()

    book_title = []
    book_author = []
    book_length = []
    book_date = []

    #handling pagination
    pagination = driver.find_element(By.XPATH, './/ul[contains(@class, "pagingElements")]')
    pages = pagination.find_elements(By.TAG_NAME, 'li')
    last_page = int(pages[-2].text)
    current_page = 1

    while(current_page <= last_page):
        time.sleep(2) # making sure the page renders correctly
        audible_container = driver.find_element(By.CLASS_NAME, "adbl-impression-container")
        audibles = audible_container.find_elements(By.XPATH, '//li[contains(@class, "productListItem")]')

        for audible in audibles:
            try:
                title = audible.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]/a').text
                book_title.append(title)
            except:
                book_title.append(None)
            try:
                author = audible.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text
                book_author.append(author)
            except:
                book_author.append(None)
            try:
                length = audible.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text
                book_length.append(length)
            except:
                book_length.append(None)
            try:
                release_date = audible.find_element(By.XPATH, './/li[contains(@class, "releaseDateLabel")]').text
                book_date.append(release_date)
            except:
                book_length.append(None)
        
        current_page += 1 # surfing through each page until it reaches the last_page

        try:
            next_page = pagination.find_element(By.XPATH, './/span[contains(@class, "nextButton")]')
            next_page.click()
        except:
            pass

    driver.quit()

    df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length, 'release_date' : book_date})
    data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    csv_path = os.path.join(data_folder, 'books.csv')
    df_books.to_csv(csv_path, index=False)




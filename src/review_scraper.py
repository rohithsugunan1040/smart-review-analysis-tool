from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

from selenium.common.exceptions import NoSuchElementException

import sys
import os
import streamlit as st

driver_path = ChromeDriverManager().install()
if os.path.exists(driver_path):
    print("ChromeDriver already installed at:", driver_path)
else:
    print("Installing ChromeDriver...")


#FOR OPTIONS
op = Options()
op.add_argument('headless')


# Setup ChromeDriver using WebDriver Manager
service = Service(driver_path)

def fetch_reviews(link):
    driver = webdriver.Chrome(service=service)
    driver.get(link)

    while driver.execute_script("return document.readyState") != "complete":
        pass

    print('\nPAGE FULLY LOADED!!\n')
    try:
        all_review_button = driver.find_element(By.CSS_SELECTOR,"._23J90q.RcXBOT")
    except NoSuchElementException:
        try:
            all_review_button = driver.find_element(By.CSS_SELECTOR,"._23J90q.iIbIvC")
        except NoSuchElementException:
            st.error("Review not found")
            return 0
    anchor = all_review_button.find_element(By.XPATH,'..')
    anchor_link = anchor.get_attribute("href")

    reviews = []
    page_count = 1
    driver.get(anchor_link+"&page="+str(page_count))
    try:
        while(driver.find_element(By.CLASS_NAME,"_9QVEpD")):
            while driver.execute_script("return document.readyState") != "complete":
                pass

            sys.stdout.write(f"\rPAGE {page_count} LOADED")
            sys.stdout.flush()

            review_divs = driver.find_elements(By.CLASS_NAME,"ZmyHeo")

            for div in review_divs:
                read_more = div.find_element(By.TAG_NAME,"span")
                if read_more.is_displayed():
                    read_more.click()
                review = div.find_element(By.XPATH,'.//div').text
                reviews.append(review)
            page_count += 1
            driver.get(anchor_link+"&page="+str(page_count))
    except NoSuchElementException:
        print("\nEND OF PAGINATION")
    driver.quit()
    return reviews
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

from selenium.common.exceptions import NoSuchElementException

import time


#FOR OPTIONS
op = Options()
op.add_argument('headless')


# Setup ChromeDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=op)


def fetch_reviews(link):
    driver.get(link)

    while driver.execute_script("return document.readyState") != "complete":
        pass

    print('\nPAGE FULLY LOADED!!\n')

    all_review_button = driver.find_element(By.CSS_SELECTOR,"._23J90q.RcXBOT")


    anchor = all_review_button.find_element(By.XPATH,'..')

    anchor_link = anchor.get_attribute("href")

    reviews = []
    page_count = 1
    driver.get(anchor_link+"&page="+str(page_count))
    try:
        while(driver.find_element(By.CLASS_NAME,"_9QVEpD")):
            while driver.execute_script("return document.readyState") != "complete":
                pass
            print(f'\nPAGE {page_count} LOADED\n')

            review_divs = driver.find_elements(By.CLASS_NAME,"ZmyHeo")

            for div in review_divs:
                read_more = div.find_element(By.TAG_NAME,"span")
                if read_more.is_displayed():
                    read_more.click()
                review = div.find_element(By.XPATH,'.//div').text
                # print(div.find_element(By.XPATH,'.//div').text)
                reviews.append(review)
            page_count += 1
            driver.get(anchor_link+"&page="+str(page_count))
    except NoSuchElementException:
        print("ELEMENT NOT FOUND")
    # reviews.append("This watch is very bad")
    # reviews.append("The competitor product is more good than this")
    # reviews.append("This watch is good but could be better in handling connections")
    # reviews.append("The watch is okay, not too bad but not too good either")  # Neutral review
    # reviews.append("The product is average, it meets expectations but doesn't exceed them")  # Neutral review
    # reviews.append("It's a decent product, nothing extraordinary")  # Neutral review
    # reviews.append("The performance is satisfactory, neither impressive nor disappointing")  # Neutral review
    return reviews
    








# anchor.click()

# while driver.execute_script("return document.readyState") != "complete":
#     pass
# print("\nALL REVIEW PAGE LOADED!!\n")
# time.sleep(3)
# print("CURRENT URL")
# print(driver.current_url)

# for i in range(1,4):
#     review_divs


# review_divs = driver.find_elements(By.CLASS_NAME,"ZmyHeo")


# for div in review_divs:
#     read_more = div.find_element(By.TAG_NAME,"span")
#     if read_more.is_displayed():
#         read_more.click()
#     print(div.find_element(By.XPATH,'.//div').text)
#     print("------------------------------------------")

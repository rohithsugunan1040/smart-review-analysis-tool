from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver import ActionChains

import time


#FOR OPTIONS
op = Options()
op.add_argument('headless')


# Setup ChromeDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=op)


def fetch_reviews(link):

    # url = "https://www.flipkart.com/noise-buds-vs102-50-hrs-playtime-11mm-driver-ipx5-unique-flybird-design-bluetooth/p/itm5b1444b835ede?pid=ACCGFFZJYBEF6HMY&lid=LSTACCGFFZJYBEF6HMYE93Y1Z&marketplace=FLIPKART&store=0pm%2Ffcn&srno=b_1_6&otracker=browse&fm=organic&iid=en_BBlPmuGUp2ePn8LhbJQIouu1iCgM8NIGkmkgK24wvFG0nHgC9UTvnaLOH9YeFGiWdRGujqZf4sDyHE3jDHy36UKsf8s6I2Oz2HOgbXTo_9U%3D&ppt=browse&ppn=browse&ssid=baqgxx2dvvvx9erk1737615304549"
    # url = "https://www.flipkart.com/boat-lunar-discovery-w-turn-navigation-3-53-cm-hd-display-bt-calling-smartwatch/p/itm49ddaa9294db0?pid=SMWH44GEEK2WDVHU&lid=LSTSMWH44GEEK2WDVHUYEJ6CE&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_4&otracker=browse&fm=organic&iid=fee2a1b8-53df-4bbe-ac6a-aaddc186ccfd.SMWH44GEEK2WDVHU.SEARCH&ppt=browse&ppn=browse&ssid=ohyjpqiewsq6jev41737637580654"

    # Open review page
    driver.get(link)

    while driver.execute_script("return document.readyState") != "complete":
        pass

    print('\nPAGE FULLY LOADED!!\n')
    # print(driver.title)

    all_review_button = driver.find_element(By.CSS_SELECTOR,"._23J90q.RcXBOT")


    anchor = all_review_button.find_element(By.XPATH,'..')

    anchor_link = anchor.get_attribute("href")

    reviews = []
    for i in range(1,10):
        driver.get(anchor_link+"&page="+str(i))

        while driver.execute_script("return document.readyState") != "complete":
            pass
        print(f'\nPAGE {i} LOADED\n')
        time.sleep(3)

        review_divs = driver.find_elements(By.CLASS_NAME,"ZmyHeo")

        for div in review_divs:
            read_more = div.find_element(By.TAG_NAME,"span")
            if read_more.is_displayed():
                read_more.click()
            review = div.find_element(By.XPATH,'.//div').text
            # print(div.find_element(By.XPATH,'.//div').text)
            reviews.append(review)
            print("------------------------------------------")
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
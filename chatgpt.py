from telnetlib import EC

import openai
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import read_csv
import time
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By



# openai.api_key = "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"
#
#
# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,
#     )
#     return response.choices[0].message["content"]
#
#
def get_description(id,name):
    chrome_options = webdriver.ChromeOptions()

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.ae/")
    time.sleep(1)

    # signing in
    driver.find_element(By.ID,"twotabsearchtextbox").send_keys(name)
    driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
    time.sleep(1)

    try:
        wait = WebDriverWait(driver, 10)
        first_result_title_element = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.s-main-slot div[data-asin][data-component-type='s-search-result'] h2 a")))

        # Click on the first result
        first_result_title_element.click()
        time.sleep(1)

        product_description_div = driver.find_element(By.ID, "productDescription")
        p_tag = product_description_div.find_element(By.TAG_NAME, "p")

        des = p_tag.text

    except:
        des = name
    return name



def get_category(id):
    url = f"https://www.upcitemdb.com/upc/{id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    active_li = soup.find("li", class_="active")

    # Extract the text content of the active category
    if active_li:
        active_category = active_li.get_text()
        # print(active_category)
    else:
        active_category = "Health care"

    return active_category




# barcodes = read_csv.get_barcodes()
# names = read_csv.get_names()
# for i,code in enumerate(barcodes):
#     get_description(code,names[i])
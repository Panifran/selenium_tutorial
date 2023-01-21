# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cp_36%3A1253503011%2Cp_72%3A1248879011%2Cp_89%3ASAMSUNG&dc&fs=true&qid=1674311265&rnid=2528832011&ref=sr_nr_p_89_3&ds=v1%3AZS4kft%2FpeDuYuv5TO0h5hN2u%2B5Uj7avyH8Ogu1wDEV0")
#
# # PAGINATION - Cada vez que haya un botón next se buscan los elementos
#
# isNextDisabled = False
#
# counter_page = 0
#
# while not isNextDisabled:
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#         (By.CSS_SELECTOR, '.action-inner')
#     ))
#     element_list = driver.find_elements(By.CSS_SELECTOR, '.s-card-container')
#
#
#     for elem in element_list:
#         title = elem.find_element(By.CSS_SELECTOR, '.a-size-base-plus')
#         print(title.text)
#
#
#     counter_page += 1
#
#     try:
#         driver.find_element(By.CSS_SELECTOR, '.s-pagination-separator').click()
#     except:
#         isNextDisabled = True
#
# print(counter_page)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from concurrent.futures import ThreadPoolExecutor
#
#
#
# options = Options()
# options.headless = False
# options.add_argument("window-size=1500,1500")
# options.add_argument("--disable-features=VizDisplayCompositor")
#
#
# PATH = "/usr/bin/chromedriver"
# driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
#
#
# driver.get("https://www.oddsportal.com/")
#
# WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#          (By.XPATH(".//div[contains(@class, 'loginModalBtn')]")
#      )))
#
#
#
# driver.find_element(By.XPATH(".//div[contains(@class, 'loginModalBtn')]")).click()
#
# if driver.find_element(By.NAME("login-submit")).is_enabled():
#     driver.find_element(By.XPATH("//input[@name=\"login-username\"]")).send_keys('Pani')
#     driver.find_element(By.XPATH("//input[@name=\"login-password\"]")).send_keys('c21bd681')
#     driver.find_element(By.XPATH("//input[@name=\"login-submit\"]")).click()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time as t

chrome_options = Options()
chrome_options.add_argument("window-size=1500,1500")
chrome_options.add_argument("--disable-features=VizDisplayCompositor")

webdriver_service = Service("chromedriver/chromedriver")  ## path to where you saved chromedriver binary
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)

url = 'https://www.oddsportal.com/'
browser.get(url)

WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'loginModalBtn')]")))

## sortout cookie button
try:
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, ".//div[contains(@class, 'loginModalBtn')]"))).click()
    print("accepted cookies")
except Exception as e:
    print('no cookie button')

if browser.find_element(By.NAME, "login-submit").is_enabled():
    browser.find_element(By.XPATH, "//input[@name=\"login-username\"]").send_keys('Pani')
    browser.find_element(By.XPATH, "//input[@name=\"login-password\"]").send_keys('c21bd681')
    browser.find_element(By.XPATH, "//input[@name=\"login-submit\"]").click()


url = 'https://www.oddsportal.com/matches/my-matches/20230121'
browser.get(url)
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.next-m\:pt-0')))
element_list = browser.find_elements(By.CSS_SELECTOR, '.next-m\:pt-0')
print(len(element_list))
#.next-m\:pt-0









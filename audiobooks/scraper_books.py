from selenium import webdriver
import pandas as pd
import time

web = "https://www.audible.com/search"
driver = webdriver.Chrome()
driver.get(web)
# driver.maximize_window()
# time.sleep(1)

container = driver.find_element('xpath', '//*[@id="center-3"]/div/div/div/span[2]/ul')
# product = driver.find_element("xpath", './li')
products = container.find_elements('xpath','.//li[contains(@class, "productListItem")]')
# print(products)

title = []
author = []
length = []

for product in products:
    title.append(product.find_element('xpath', './/h3[contains(@class, "bc-heading")]').text)
    author.append(product.find_element('xpath', './/li[contains(@class, "authorLabel")]').text)
    length.append(product.find_element('xpath', './/li[contains(@class, "runtimeLabel")]').text)

df = pd.DataFrame({'title':title, 'author':author, 'length':length})
df.to_csv('audiobooks/amazon_books.csv')
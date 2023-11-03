from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless=new')

web = "https://www.audible.com/search"
driver = webdriver.Chrome(options=options)
driver.get(web)

pagination = driver.find_element('xpath','//ul[contains(@class, "pagingElements")]')  
pages = pagination.find_elements('tag name','li')
last_page = int(pages[-2].text)

current_page = 1

title = []
author = []
length = []

while current_page <= last_page:
    container = driver.find_element('xpath', '//*[@id="center-3"]/div/div/div/span[2]/ul')
    products = container.find_elements('xpath','.//li[contains(@class, "productListItem")]')


    for product in products:
        title.append(product.find_element('xpath', './/h3[contains(@class, "bc-heading")]').text)
        author.append(product.find_element('xpath', './/li[contains(@class, "authorLabel")]').text)
        length.append(product.find_element('xpath', './/li[contains(@class, "runtimeLabel")]').text)
    
    next_page = driver.find_element('xpath','.//span[contains(@class , "nextButton")]')
    if next_page is not None:
        next_page.click()

    current_page += 1

    df = pd.DataFrame({'title':title, 'author':author, 'length':length})
    df.to_csv('audiobooks/amazon_books.csv')
from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select


website = 'https://www.adamchoi.co.uk/btts/detailed'

driver = webdriver.Chrome()

driver.get(website)
button = driver.find_element("xpath",'//label[@analytics-event="All matches"]')

date = []
hame_team = []
score = []
away_team = []

def scrape():

    button.click()
    dropdown = Select(driver.find_element('id','country'))
    dropdown.select_by_visible_text('Spain')    
    matches = driver.find_elements("tag name", 'tr')

    for match in matches:
        date.append(match.find_element('xpath','./td[1]').text)
        hame_team.append(match.find_element('xpath','./td[2]').text)
        score.append(match.find_element('xpath','./td[3]').text)
        away_team.append(match.find_element('xpath','./td[4]').text)

    df = pd.DataFrame({'date': date, 'hame_team':hame_team, 'score':score, 'away_team':away_team})
    df.to_csv('football/football_data.csv', index=True)

scrape()

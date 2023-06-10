import sys
import pandas
import csv
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
from bs4 import BeautifulSoup

scraped_datatime=datetime.datetime.utcnow().isoformat()


driver=webdriver.Chrome()
driver.maximize_window()

all_datas=[]

urll="https://www.google.com/travel/hotels/entity/CgsI1_7cptqQwZTAARAB?ei=3-EOZNPlM8-XxdwPsMGEsAo&sa=X&ved=2ahUKEwiT0cewwdj9AhXPS5EFHbAgAaYQrsMEegQIBBAq"
driver.get(urll)

#print(title)

time.sleep(500)
pri=driver.find_element(By.ID, "prices").click()

soup1 = BeautifulSoup(driver.page_source, 'html.parser')
title=soup1.find("h1", class_="QORQHb fZscne").text
time.sleep(6)
soup = BeautifulSoup(driver.page_source, 'html.parser')

alll=soup.find("div", class_="R09YGb ilovz").find_all("div", class_="CcERhd msQyLb hGTXTe qbgwxe MPcYpd")
for x in alll:
    print(x)
    print("\n")

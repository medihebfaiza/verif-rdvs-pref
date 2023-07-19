import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from notify_run import Notify


pref_url = 'https://www.herault.gouv.fr/booking/create/15253/0'
chrome_driver = open("chrome_driver.txt","r").read()
notify_endpoint = open("notify_endpoint.txt","r").read()

print(chrome_driver)
print(notify_endpoint)

check_every = 10

def bypass502(driver): 
  if driver.find_elements_by_xpath("//*[text()='502 Bad Gateway']"):
    while driver.find_elements_by_xpath("//*[text()='502 Bad Gateway']"):
      driver.refresh()
      sleep(5)

requests.post(notify_endpoint, {'message': 'La vérification des RDVs est lancée', 'action': None})

driver = webdriver.Chrome(chrome_driver)
driver.get(pref_url)
bypass502(driver)
while True:
  bypass502(driver)
  driver.find_element_by_name("condition").click()
  driver.find_element_by_name("nextButton").click()
  bypass502(driver)
  if driver.find_elements_by_name("finishButton") :
    driver.find_element_by_name("finishButton").click()
    sleep(check_every * 300)
  else:
    requests.post(notify_endpoint, {'message': 'Des RDVs sont disponibles sur le site de la préfecture', 'action': None})
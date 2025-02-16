from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from tkinter import Tk
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://online.seterra.com/en/vgp/3015")

## Variables

valid = False
current_country = ""
cclength = 0

## Automation

time.sleep(4)
driver.find_element(By.CLASS_NAME, "close-adhesive-icon").click()
time.sleep(3)
driver.find_element(By.ID, "cmdRestart").click()

win = driver.find_element(By.ID, "lblFinalScore2").text
print(win)
while win == "":
    try:
        current_country = driver.find_element(By.ID, "currQuestion").text
        print("Element exists!")
    except NoSuchElementException:
        print("Element does not exist")
    #time.sleep(2)
    cclength = len(current_country)
    current_country = current_country[11:cclength].upper()
    current_country = current_country.replace(" ", "")

    current_country = current_country.replace("CITY", "")#Fixes Vatican City
    current_country = current_country.replace("(CZECHIA)", "")#Fixes CZECHREPUBLIC
    current_country = current_country.replace("LUXEMBOURG", "LUXEMBURG")#Fixes CZECHREPUBLIC
    current_country = current_country.replace("NORTH", "")#Fixes NORTH MACEDONIA
    print(current_country)

    valid = False
    while not valid:
        try:
            current_country_button = driver.find_element(By.ID, "CITY_" + current_country).click()
            valid = True
            print(">CITY_")
        except:
            print("NOT CITY_")
            try:
                current_country_button = driver.find_element(By.ID, "AREA_" + current_country).click()
                valid = True
                print(">AREA_")
            except:
                print("NOT AREA_")
                try:
                    current_country_button = driver.find_element(By.ID, "CITY_THE" + current_country).click()
                    valid = True
                    print(">CITY_THE")
                except:
                    print("NOT CITY_THE")
                    try:
                        current_country_button = driver.find_element(By.ID, "AREA_THE" + current_country).click()
                        valid = True
                        print(">AREA_THE")
                    except:
                        print("NOT AREA_THE")
                        try:
                            current_country_button = driver.find_element(By.ID, current_country).click()
                            valid = True
                            print(">NO PREFIX")
                        except:
                            #driver.find_element(By.ID, "divSkip").click()
                            #valid = True
                            print("error")
                            #time.sleep(20)
    #current_country_button.click()
    win = driver.find_element(By.ID, "lblFinalScore2").text
    print("x")
    print(" ")
print("Complete!")
#driver.close()
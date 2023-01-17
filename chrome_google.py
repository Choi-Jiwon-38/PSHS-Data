# Selenium 실행 코드
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # Chrome Driver를 불러온 뒤, driver
driver.get('https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl')  # Move to 'google image'

elem = driver.find_element(By.CLASS_NAME, "gLFyf")                  # Find 'search bar' in 'google image' page
elem.clear()                # Clear all texts in search bar
elem.send_keys('can')       # Enter keywords you want to search
elem.send_keys(Keys.RETURN) # Press 'ENTER' key

SCROLL_PAUSE_TIME = 1       # Delay time for load new contents in google images
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")        
while (1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")    # Scroll page
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:   
        try:            
            driver.find_element(By.CLASS_NAME, 'mye4qd').send_keys(Keys.ENTER)
        except:                 # If end of page (No view more button)
            break   
    last_height = new_height    # Update last height for loop

images = driver.find_elements(By.CLASS_NAME, 'rg_i Q4LuWd')
count = 1
for image in images:
    try:
        image.send_keys(Keys.ENTER)
        time.sleep(2)
        imageURL = driver.find_element(By.XPATH, '')
        # ADD MORE CODE . . .
        count = count + 1
    except:
        pass

driver.quit()
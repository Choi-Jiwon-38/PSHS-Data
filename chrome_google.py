# Selenium 실행 코드
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

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
            driver.find_element(By.CLASS_NAME, 'mye4qd').click()
        except:                 # If end of page (No view more button)
            break   
    last_height = new_height    # Update last height for loop

images = driver.find_elements(By.CLASS_NAME, 'rg_i Q4LuWd')
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imageURL = driver.find_element(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        opener = urllib.request.build_opener()
        opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imageURL, str(count) + ".jpg")
        count = count + 1
    except:
        pass

driver.quit()
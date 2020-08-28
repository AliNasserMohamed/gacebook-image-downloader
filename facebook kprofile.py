from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=option, executable_path=path)
driver.get("https://facebook.com")
search = driver.find_element_by_name("email")
username = input("inter your number")
search.send_keys(username)
password = driver.find_element_by_name("pass")
passWord = input("inter your password")
password.send_keys(passWord)
submit = driver.find_element_by_name("login")
submit.click()
print("ali")
try:
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                           '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/a')))
    print(main.get_property("href"))
    time.sleep(10)
    main.click()
    print("main clicked")
    time.sleep(20)
    imgs = driver.find_elements_by_tag_name("img")

    print("reaching images")
    print(imgs)
    for img in imgs:
        img_source = img.get_property("src")
        img_name=img.get_property("alt")
        if img_name:
           r=requests.get(img_source)
           time.sleep(3)
           file=open("images\\"+img_name+".jpg","wb")
           file.write(r.content)

except:
    print("not here")

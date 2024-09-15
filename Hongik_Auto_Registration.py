import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #keep chrome opened
cService = webdriver.ChromeService(executable_path=r"chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = cService, options = chrome_options)

driver.get("https://www.hongik.ac.kr/my/login.do?Refer=https://cn.hongik.ac.kr/")


#Login
try:
    #id
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'USER_ID'))
    )
    user_id = driver.find_element(By.ID, 'USER_ID')
    user_id.send_keys("ID")  # replace with your Hongik ID

    #pw
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'PASSWD'))
    )
    user_pw = driver.find_element(By.ID, 'PASSWD')
    user_pw.send_keys("PASSWORD") # replace with your Hongik password

    #login button
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'btn-login'))
    )
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    #popup click (password change alert)
    if WebDriverWait(driver, 10).until(EC.alert_is_present()):
        try: # Wait for the alert to be present
            alert = Alert(driver)
            alert.accept() # Accept the alert
        except:
            None

    #전자출결 click
    driver.switch_to.new_window()
    driver.get("https://at.hongik.ac.kr/")

except Exception as e:

    print(e)


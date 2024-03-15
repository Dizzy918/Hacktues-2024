from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time
import threading

mail = 'aleks.i.gerasimov.2022@elsys-bg.org'
password = 'Sladoled'

running = True
driver = webdriver.Chrome()

def login(mail, password):
    global driver
    driver.get("https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&ifkv=ATuJsjx1Te0um30YO4g8V2XnqUi_0vgBhLBi4SMQAeVJ_FslFH6o8GZmokr0WRVo8YP31jWFrifMbg&passive=1209600&service=classroom&theme=glif")
    
    email_input = driver.find_element(By.XPATH, "//input[@type='email']")
    email_input.send_keys(mail)

    sleep(3)
    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
    next_button.click()

    sleep(3)
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys(password)

    sleep(3)
    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
    next_button.click()

def unlimited_sleep():
    global running
    sleep(5)
    logout(driver)

def logout():
    global running
    global driver

    sleep(3)

    driver.implicitly_wait(10)
    profile_button = driver.find_element(By.CLASS_NAME, "gb_Fa")
    profile_button.click()
    iframe = driver.find_element(By.XPATH, "//iframe[@name='account']")
    print(iframe)
    driver.switch_to.frame(iframe)

    container = driver.find_element(By.CLASS_NAME, "JWEMkf")
    links = container.find_elements(By.TAG_NAME,"a")
    print(links)
    signout_button = links[1]
    signout_button.click()
    sleep(7)

    driver.switch_to.default_content()

    container2 = driver.find_element(By.CLASS_NAME, "OVnw0d")
    options = container2.find_elements(By.TAG_NAME, "li")
    removeprofile_button = options[2]
    removeprofile_button.click()
    print("d")
    sleep(7)

    redminus_button = driver.find_element(By.CLASS_NAME, "stUf5b")
    redminus_button.click()
    sleep(7)

    logoutconfirmation_button = driver.find_element(By.CLASS_NAME, "RveJvd snByac")
    logoutconfirmation_button.click()
    sleep(3)

    running = False
    driver.quit()

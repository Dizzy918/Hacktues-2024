from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time
import threading

mail = input("Enter your mail: ")
password = input("Enter your password: ")

running = True

def login(mail, password):
    
    driver = webdriver.Chrome()
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

    return driver

def unlimited_sleep():
    global running
    #while True:
    sleep(5)
    logout(driver)

def logout(driver):

    #t.join()

    print("A")  
    global running

    sleep(5)

    profile_button = driver.find_element(By.CLASS_NAME, "gb_Fa")
    profile_button.click()
    print("b")
    sleep(5)

    signout_button = driver.find_element(By.CLASS_NAME, "JWEMkf")
    signout_button.click()
    print("c")
    sleep(2)

    removeprofile_button = driver.find_element(By.CLASS_NAME, "lCoei YZVTmd SmR8")
    removeprofile_button.click()
    sleep(2)

    redminus_button = driver.find_element(By.CLASS_NAME, "stUf5b")
    redminus_button.click()
    sleep(2)

    logoutconfirmation_button = driver.find_element(By.CLASS_NAME, "ZFr60d CeoRYc")
    logoutconfirmation_button.click()
    sleep(2)

    running = False
    driver.quit()

driver = login(mail, password)

t = threading.Thread(target = unlimited_sleep())
t.start()

logout(driver)

sleep(30)

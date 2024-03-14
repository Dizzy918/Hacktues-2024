from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

mail = input("Enter your mail: ")
password = input("Enter your password: ")

def fun(mail, password):
    
    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fclassroom.google.com%2F%3Femr%3D0&ifkv=ATuJsjx1Te0um30YO4g8V2XnqUi_0vgBhLBi4SMQAeVJ_FslFH6o8GZmokr0WRVo8YP31jWFrifMbg&passive=1209600&service=classroom&theme=glif")

    sleep(2)
    email_input = driver.find_element(By.XPATH, "//input[@type='email']")
    email_input.send_keys(mail)

    sleep(2)
    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
    next_button.click()

    sleep(2)
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    password_input.send_keys(password)

    sleep(2)
    next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
    next_button.click()

    sleep(5)
    error_div = driver.find_element(By.XPATH, "//div[@jsname='B34EJ']")
    
    print("Error message:", error_div.text)
    
    sleep(10)
    driver.quit()
    print("Finished succesfuly")

fun(mail, password)
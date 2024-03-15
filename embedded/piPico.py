import board
import time
import digitalio
import microcontroller
import random
import usb_cdc

email = "daniel.b.yordanov.2022@elsys-bg.org"
password = "dani08201214012119"

email1 = f"({email})"
password1 = f"({password})"

button_login = digitalio.DigitalInOut(board.GP0)
button_login.switch_to_input(pull = digitalio.Pull.UP)

button_logout = digitalio.DigitalInOut(board.GP1)
button_logout.switch_to_input(pull = digitalio.Pull.UP)



while True:
    # 2 events
    # Login -> "Login: (username, password)"
    # Logout -> "Logout"
    if button_login.value == False:
        print(email1)
        print(password1)
        time.sleep(1)
    elif button_logout.value == False:
        print("Logout")
        time.sleep(1)

        

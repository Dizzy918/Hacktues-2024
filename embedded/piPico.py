import board
import time
import digitalio
import microcontroller
import random
import usb_cdc

email = "gmail.vom"
password = "password"

email1 = f"({email})"
password1 = f"({password})"

button = digitalio.DigitalInOut(board.GP0)
button.switch_to_input(pull = digitalio.Pull.UP)



while True:
    if button.value == False:
        print(email1)
        print(password1)
        time.sleep(1)


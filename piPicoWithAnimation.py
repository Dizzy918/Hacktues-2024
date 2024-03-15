import board
import time
import digitalio
import microcontroller
import random
import usb_cdc
import busio
import displayio
import adafruit_displayio_ssd1306
import adafruit_imageload


email = "gmail"
password = "password"

email1 = f"({email})"
password1 = f"({password})"

button_login = digitalio.DigitalInOut(board.GP0)
button_login.switch_to_input(pull = digitalio.Pull.UP)

button_logout = digitalio.DigitalInOut(board.GP1)
button_logout.switch_to_input(pull = digitalio.Pull.UP)



IMAGE_FILE = "bee.bmp"
SPRITE_SIZE = (64, 64)
FRAMES = 28

def invert_colors(palette):
    palette[0], palette[1] = palette[1], palette[0]

displayio.release_displays()

i2c = busio.I2C(board.GP9, board.GP8)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

group = displayio.Group()

icon_bit, icon_pal = adafruit_imageload.load(IMAGE_FILE, bitmap=displayio.Bitmap, palette=displayio.Palette)
invert_colors(icon_pal)

icon_grid = displayio.TileGrid(icon_bit, pixel_shader=icon_pal, width=1, height=1, tile_height=SPRITE_SIZE[1], tile_width=SPRITE_SIZE[0], default_tile=0, x=32, y=0)
group.append(icon_grid)

display.show(group)

timer = 0
pointer = 0



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

    if (timer + 0.1) < time.monotonic():
        icon_grid[0] = pointer
        pointer = (pointer + 1) % FRAMES
        timer = time.monotonic()
from threading import Thread
from time import sleep

# Global flag to control the thread
running = True

def unlimited_sleep():
    global running
    while running:
        print("Thread is running...")
        sleep(1)

# Create and start the thread
t = Thread(target=unlimited_sleep)
t.start()

# Sleep for some time before stopping the thread
sleep(5)

# Signal the thread to stop
running = False

# Wait for the thread to finish
t.join()

print("Thread stopped.")
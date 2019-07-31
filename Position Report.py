from pynput.mouse import *
import time

if __name__ == "__main__":
    mouse = Controller()
    mousePos = mouse.position
    while True:
        mousePos = mouse.position
        print(mousePos)
        time.sleep(1)

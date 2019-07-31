from pynput.mouse import *
import numpy as np
from PIL import ImageGrab
import cv2

if __name__ == "__main__":
    mouse = Controller()
    game_cord = (250*1.25, 459*1.25, 558*1.25, 464*1.25)
    mousePos = mouse.position
    screen = np.array(ImageGrab.grab(bbox=game_cord))
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
    while True:
        screen = np.array(ImageGrab.grab(bbox=game_cord))
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
        line = list(screen[0])
        if 17 in line:
            if line.index(17) == 0:  # 1
                mouse.position = (282, 550)
                mouse.click(Button.left)
            elif line.index(17) == 96: # 2
                mouse.position = (366, 550)
                mouse.click(Button.left)
            elif line.index(17) == 196: # 3
                mouse.position = (445, 550)
                mouse.click(Button.left)
            elif line.index(17) == 296: # 4
                mouse.position = (523, 550)
                mouse.click(Button.left)
        else:
            mouse.position = (482, 622)
            mouse.click(Button.left)
            print("Restart\n")

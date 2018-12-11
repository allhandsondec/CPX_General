import time
import board
import neopixel


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK = (0, 0, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)

while True:
    i = 0
    pixels.fill(BLACK)
    for i in range(9):
        pixels[i]=YELLOW
        pixels[i-1]=YELLOW
        pixels.show()
        time.sleep(.1)
        pixels[i]=BLACK
        pixels[i-1]=BLACK
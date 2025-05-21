from microbit import *
import random

while True:
    gameStarted = False
    if pin0.is_touched():
        display.show(3)
        sleep(1000)
        display.show(2)
        sleep(1000)
        display.show(1)
        sleep(1000)
        display.show(Image.YES)
        sleep(1000)
        sleep(random.randint(1000, 5000))
        gameStarted = True
        display.show(Image.HEART)
        start = running_time()
        while gameStarted:
            if pin1.is_touched():
                display.show('A')
                sleep(1000)
                display.scroll(running_time() - start)
                gameStarted = False
            elif pin2.is_touched():
                display.show('B')
                sleep(1000)
                display.scroll(running_time()- start)
                gameStarted = False
        sleep(3000)
        display.clear()

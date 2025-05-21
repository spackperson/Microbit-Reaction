from microbit import *
import random

#variables
score_A = 0
score_B = 0
gameOn = True

#start image
display.show(Image.PACMAN)

while gameOn:
    roundStarted = False
    if pin0.is_touched():
        #countdown and display start image
        display.show(3)
        sleep(1000)
        display.show(2)
        sleep(1000)
        display.show(1)
        sleep(1000)
        display.show(Image.YES)
        sleep(1000)

        #de
        sleep(random.randint(1000, 5000))
        roundStarted = True
        display.show(Image.HEART)
        start = running_time()
        while roundStarted:
            if pin1.is_touched():
                display.show('A')
                sleep(1000)
                display.scroll(running_time() - start)
                score_A += 1
                roundStarted = False
            elif pin2.is_touched():
                display.show('B')
                sleep(1000)
                display.scroll(running_time()- start)
                score_B += 1
                roundStarted = False
        sleep(3000)
        display.clear()
    elif button_a.is_pressed() and button_b.is_pressed():
            gameOn = False

#print end game Stats
#maybe add best reation time here, need to build lists etc.
if score_A > score_B:
    A_wins = "A wins with" + str(score_A) + "points!"
    display.scroll(A_wins, 70)
elif score_B > score_A:
    B_wins = "B wins with" + str(score_B) + "points!"
    display.scroll(B_wins, 70)
else:
    display.scroll("It's a tie!")

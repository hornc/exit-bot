import autopy
import random
import subprocess
from time import sleep

STEAM_EXE = 'C:\Program Files (x86)\Steam\steam.exe'
EXIT8 = 'steam://rungameid/2653790'

TURN = 0.72
SHORT = 10
LONG = 21


class Dead(Exception):
    """Bot died exception."""


class Won(Exception):
    """Bot just won! Yay!."""  # Untested!


def left():
    autopy.key.toggle(autopy.key.Code.LEFT_ARROW, down=True)
    sleep(TURN)
    autopy.key.toggle(autopy.key.Code.LEFT_ARROW, down=False)


def right():
    autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, down=True)
    sleep(TURN)
    autopy.key.toggle(autopy.key.Code.RIGHT_ARROW, down=False)


def forward(n=1, looking=False):
    for i in range(n):
        autopy.key.toggle(autopy.key.Code.UP_ARROW, down=True)
        sleep(TURN)
        autopy.key.toggle(autopy.key.Code.UP_ARROW, down=False)
        if looking:
            look(looking)


def look(eye:list):
    """
    Samples a small number of pixels to determine whether the bot has
    either died (all black screen) or won (all white screen)
    """
    samples = []
    for point in eye:
        samples.append(hex(autopy.screen.get_color(*point)))
    print("EYE:", samples)
    dead = '0x0'
    win  = '0xffffff'
    isdead = None
    haswon = None
    # TODO: use all() and raise?
    if samples.count(dead) > (len(samples) - 2):
        raise Dead
    if samples.count(win) > (len(samples) - 2):
        raise Won
        

def main():
    print("Hello!")
    subprocess.run([STEAM_EXE, EXIT8])
    sleep(10)
    print("Ready...")
    w, h = autopy.screen.size()
    ED = 100
    eyes = [(w//2, h//2), (w//2 + ED, h//2 + ED), (w//2 - ED, h//2 + ED), (w//2 + ED, h//2 - ED), (w//2 - ED, h//2 - ED)]
    #autopy.bitmap.capture_screen().save("screenshot.png")

    while 1:
        left()
        forward(SHORT)
        right()
        try:
            forward(LONG, looking=eyes)
            left()
            forward(SHORT, looking=eyes)
        except Dead:
            print("I think I just died!")
            sleep(25)
            continue
        right()
        forward(SHORT)   

        print('COLOR:', hex(autopy.screen.get_color(w//2, h//2)))


if __name__ == '__main__':
    main()

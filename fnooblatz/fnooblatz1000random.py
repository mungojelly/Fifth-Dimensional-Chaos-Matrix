# ________________________________
#
#  FNOOBLATZ 1000 RANDOM TWIDDLER
# ________________________________
#
# License: http://sam.zoy.org/wtfpl/COPYING
#
# This is a Fnooblatz 1000 harness that just inflates 
# the display to a reasonable size and then sends random 
# commands.  I think it's pretty. 

WIDTH_OF_DISPLAY = 60
HEIGHT_OF_DISPLAY = 20
MIN_SEQUENCE_LENGTH = 1
MAX_SEQUENCE_LENGTH = 5000
RESET_TIME = 17
REPEAT_TIME = 1.7
REFRESH_TIME = 0.17

# Various distributions, for variety: 
DIST_BEGIN = [5,6,7,8,9,10,99999]
DIST_BEGIN_NO_AT = [5,6,7,8,9,10]
DIST_BEGIN_ALT = [5,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10,99999]
DIST_BEGIN_ALT_NO_AT = [5,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10]
DIST_BEGIN_NO_LR = [5,6,7,8,9,99999]
DIST_BEGIN_NO_AT_NO_LR = [5,6,7,8,9]
DIST_BEGIN_ALT_NO_LR = [5,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,99999]
DIST_BEGIN_ALT_NO_AT_NO_LR = [5,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9]
DIST_NO_MOVE = [8,9,10]
DIST_NO_MOVE_PAUSE = [7,8,9,10]
SPACEY = [11,11,11,11,11,11,11,11,11,11,11,11,11,11,5,6,7,8,8,8,9,10]
SPACEY_NO_MOVE = [11,11,11,11,11,11,11,11,11,11,11,11,11,11,7,8,8,8,9,10]
SPACEY_NO_LR = [11,11,11,11,11,11,11,11,11,11,11,11,11,11,6,7,8,8,8,9,10]
SPACEY_NO_UPDOWN = [11,11,11,11,11,11,11,11,11,11,11,11,11,11,5,7,8,8,8,9,10]
DISTRIBUTIONS = [DIST_BEGIN, DIST_BEGIN_NO_AT, 
                 DIST_BEGIN_ALT, DIST_BEGIN_ALT_NO_AT,
                 DIST_BEGIN_NO_LR, DIST_BEGIN_NO_AT_NO_LR,
                 DIST_BEGIN_ALT_NO_LR, DIST_BEGIN_ALT_NO_AT_NO_LR,
                 DIST_NO_MOVE, DIST_NO_MOVE_PAUSE,
                 SPACEY, SPACEY_NO_MOVE, SPACEY_NO_LR,
                 SPACEY_NO_UPDOWN]

import fnooblatz1000

import curses
import random
import time

def random_sequence():
    sequence = []
    distribution = random.choice(DISTRIBUTIONS)
    for i in range(random.randint(MIN_SEQUENCE_LENGTH,MAX_SEQUENCE_LENGTH)):
        sequence.append(random.choice(distribution))
    return sequence

def reset_fnooblatz(fnoo):
    fnoo.press_button(0)
    for x in range(WIDTH_OF_DISPLAY):
        fnoo.press_button(1)
    for y in range(HEIGHT_OF_DISPLAY):
        fnoo.press_button(2)

def main(stdscr):
    curses.curs_set(0)
    fnoo = fnooblatz1000.Fnooblatz1000()
    reset_fnooblatz(fnoo)
    fnooblatz_reset = time.time()
    sequence_changed = time.time()
    display_refreshed = time.time()
    sequence = random_sequence()
    while True:
        fnoo.execute_sequence(sequence)
        if time.time() - fnooblatz_reset > RESET_TIME:
            fnooblatz_reset = time.time()
            reset_fnooblatz(fnoo)
        if time.time() - sequence_changed > REPEAT_TIME:
            sequence_changed = time.time()
            sequence = random_sequence()
        if time.time() - display_refreshed > REFRESH_TIME:
            display_refreshed = time.time()
            fnoo.print_curses(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)

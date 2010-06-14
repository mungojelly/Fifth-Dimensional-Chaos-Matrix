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

MIN_SEQUENCE_LENGTH = 1
MAX_SEQUENCE_LENGTH = 5000
MIN_BACKGROUND_SEQUENCE_LENGTH = 1
MAX_BACKGROUND_SEQUENCE_LENGTH = 5000
RESET_TIME = 17
REPEAT_TIME = 1.7
REFRESH_TIME = 0.17
ALWAYS_BACKGROUNDING = False
NEVER_BACKGROUNDING = False

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
ABBA = [5,6,7,8,9,10,11,12,13,14]
MORE_A = [5,6,7,8,8,8,8,8,9,10,11,11,11,12,13,13,13,13,13,13,13,14]
MORE_B = [5,6,7,8,8,8,8,8,9,10,11,11,11,12,13,14,14,14,14,14,14,14]
SPARSELY_ABISH = [5,6,7,8,8,8,8,8,8,8,8,8,9,10,11,11,11,11,11,11,11,12,13,14]
VERY_SPARSELY_ABISH = [5,6,7,8,8,8,8,8,8,8,8,8,9,10,11,11,11,11,11,11,11,
                       11,11,11,11,11,11,11,11,11,11,11,11,11,12,13,14]
ONLY_A = [5,6,7,8,8,8,8,8,9,10,11,11,13]
ONLY_B = [5,6,7,8,8,8,8,8,9,10,11,11,14]
LEFT_SIDE = [6,6,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,10,10,10,10,10,
             11,11,11,11,11,11,11,11,11,11,11,11,11,12,13,14,17]
TOP_SHIFT = [5,5,7,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,10,10,10,10,10,
             11,11,11,11,11,11,11,11,11,11,11,11,11,12,13,14,17]
SIDE_STICK = [7,7,7,8,8,8,8,8,8,8,8,9,9,9,9,9,18,18,18,19,19,19]
UPDOWN_STICK = [7,7,7,8,8,9,9,9,10,10,10,20,20,20,21,21,21]
A_ROUND_STICK = [6,7,7,7,8,8,8,9,10,11,11,17,18,18,19,19,19,19,
                 19,19,19,19,19,19,19,20,20,21,21,99999]
A_ROUND_RAIN = [5,7,7,7,8,8,8,9,10,11,11,17,18,18,19,19,19,19,
                19,19,19,19,20,20,21,21,21,21,21,21,21,21,99999]
DISTRIBUTIONS = [DIST_BEGIN, DIST_BEGIN_NO_AT, 
                 DIST_BEGIN_ALT, DIST_BEGIN_ALT_NO_AT,
                 DIST_BEGIN_NO_LR, DIST_BEGIN_NO_AT_NO_LR,
                 DIST_BEGIN_ALT_NO_LR, DIST_BEGIN_ALT_NO_AT_NO_LR,
                 DIST_NO_MOVE, DIST_NO_MOVE_PAUSE,
                 SPACEY, SPACEY_NO_MOVE, SPACEY_NO_LR,
                 SPACEY_NO_UPDOWN, ABBA, MORE_A, MORE_B,
                 SPARSELY_ABISH, VERY_SPARSELY_ABISH,
                 ONLY_A, ONLY_B, LEFT_SIDE, TOP_SHIFT,
                 SIDE_STICK, UPDOWN_STICK, A_ROUND_STICK,
                 A_ROUND_RAIN]

# Some distributions for using the background processor. 
BACKGROUNDER = [8,8,8,11,11,11,99999]
SPACER_OUT = [11,11,11,7,7,7]
A_BACKGROUND = [7,7,7,7,7,7,7,7,7,7,13,13]
B_BACKGROUND = [7,7,7,7,7,7,7,7,7,7,14,14]
BG_ATER = [7,7,7,7,7,7,99999]
BG_CURSOR = [7,7,7,7,7,9,10]
BG_CURSOR_CORNERER = [7,7,7,7,7,7,17]
LEFT_PUSHER = [7,7,7,7,18]
RIGHT_PUSHER = [7,7,7,7,19]
UP_PUSHER = [7,7,7,7,20]
DOWN_PUSHER = [7,7,7,7,21]
AROUND_PUSHER = [18,19,20,21]
SUPER_SPACEY_DOWNER = [11,11,11,11,11,11,11,11,11,11,11,11,11,
                       11,11,11,11,11,11,11,11,11,11,11,11,11,
                       21,21,21,21,21,21,21,21,21,21,21,21,21]
BACKGROUND_DISTRIBUTIONS = [BACKGROUNDER, SPACER_OUT, 
                            A_BACKGROUND, B_BACKGROUND, BG_ATER,
                            BG_CURSOR, BG_CURSOR_CORNERER,
                            LEFT_PUSHER, RIGHT_PUSHER,
                            UP_PUSHER, DOWN_PUSHER, AROUND_PUSHER,
                            SUPER_SPACEY_DOWNER]

import fnooblatz1000

import curses
import random
import time

class RandomRunner(object):
    def __init__(self,fnooblatz,stdscr):
        self.fnoo = fnooblatz
        self.stdscr = stdscr
    def reset_fnooblatz(self):
        self.fnoo.press_button(0)
        backgrounding = random.choice([True, False])
        if ALWAYS_BACKGROUNDING:
            backgrounding = True
        if NEVER_BACKGROUNDING:
            backgrounding = False
        if backgrounding:
            background_distribution = random.choice(BACKGROUND_DISTRIBUTIONS)
            background_sequence = self.random_sequence(background_distribution,
                                                       MIN_BACKGROUND_SEQUENCE_LENGTH,
                                                       MAX_BACKGROUND_SEQUENCE_LENGTH)
            self.fnoo.execute_sequence(background_sequence)
            self.fnoo.press_button(15) # Store it.
            self.fnoo.press_button(16) # Start it.
    def random_sequence(self,distribution,min_length,max_length):
        sequence = []
        for i in range(random.randint(min_length,max_length)):
            sequence.append(random.choice(distribution))
        return sequence
    def new_sequence(self):
        self.sequence = self.random_sequence(random.choice(DISTRIBUTIONS),
                                             MIN_SEQUENCE_LENGTH,
                                             MAX_SEQUENCE_LENGTH)
    def run_forever(self):
        self.reset_fnooblatz()
        fnooblatz_reset = time.time()
        self.new_sequence()
        sequence_changed = time.time()
        self.fnoo.print_curses(self.stdscr)
        display_refreshed = time.time()
        while True:
            self.fnoo.execute_sequence(self.sequence)
            if time.time() - fnooblatz_reset > RESET_TIME:
                self.reset_fnooblatz()
                fnooblatz_reset = time.time()
            if time.time() - sequence_changed > REPEAT_TIME:
                self.new_sequence()
                sequence_changed = time.time()
            if time.time() - display_refreshed > REFRESH_TIME:
                (maxy, maxx) = self.stdscr.getmaxyx()
                self.height = maxy - 1
                self.width = maxx - 1
                self.fnoo.set_width(self.width)
                self.fnoo.set_height(self.height)
                self.fnoo.print_curses(self.stdscr)
                display_refreshed = time.time()

def main(stdscr):
    curses.curs_set(0)
    fnoo = fnooblatz1000.Fnooblatz1000()
    random_runner = RandomRunner(fnoo,stdscr)
    random_runner.run_forever()

if __name__ == "__main__":
    curses.wrapper(main)

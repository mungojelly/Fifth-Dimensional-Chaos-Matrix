# ______________________________
#
# FNOOBLATZ 2000 RANDOM TWIDDLER
# ______________________________
#
# License: http://en.wikipedia.org/wiki/WTFPL

RESET_TIME = 170
DISTRIBUTION_TIME = 17
SEQUENCE_TIME = 1.7
REFRESH_TIME = 0.17

MINIMUM_SEQUENCE = 1
MAXIMUM_SEQUENCE = 100

DISTRIBUTIONS = [
    ["Megadonutry",
     ['megadonut','right','left','up','down','a',
      'alphabetrotate','alphabetrotate','alphabetrotate']],
]

from fnooblatz2000 import Fnooblatz2000

import curses
import random
import time

class RandomRunner(object):
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.fnoo = Fnooblatz2000()
        self.reset_fnooblatz()
        self.fnooblatz_reset = time.time()
        self.distribution = ["...starting...", ['nop']]
        self.distribution_changed = time.time() - (DISTRIBUTION_TIME - 3)
        self.sequence = ['nop']
        self.sequence_changed = time.time()
    def reset_fnooblatz(self):
        self.fnoo.do(['reset'])
    def new_distribution(self):
        self.distribution = random.choice(DISTRIBUTIONS)
        self.distribution_changed = time.time()
    def new_sequence(self):
        self.sequence = []
        length = random.randint(MINIMUM_SEQUENCE, MAXIMUM_SEQUENCE)
        for command in range(length):
            next_command = random.choice(self.distribution[1])
            self.sequence.append(next_command)
    def run_forever(self):
        self.display_refreshed = time.time()
        while True:
            self.fnoo.do(self.sequence)
            if time.time() - self.fnooblatz_reset > RESET_TIME:
                self.reset_fnooblatz()
                self.fnooblatz_reset = time.time()
            if time.time() - self.sequence_changed > SEQUENCE_TIME:
                self.new_sequence()
                self.sequence_changed = time.time()
            if time.time() - self.distribution_changed > DISTRIBUTION_TIME:
                self.new_distribution()
                self.distribution_changed = time.time()
            if time.time() - self.display_refreshed > REFRESH_TIME:
                (max_y, max_x) = self.stdscr.getmaxyx()
                self.height = max_y - 2
                self.width = max_x - 1
                self.fnoo.fnoo.set_width(self.width)
                self.fnoo.fnoo.set_height(self.height)
                self.stdscr.erase()
                self.fnoo.fnoo.print_curses(self.stdscr)
                self.stdscr.addstr(self.height, 0, self.distribution[0])
                self.stdscr.refresh()
                self.display_refreshed = time.time()

def main(stdscr):
    runner = RandomRunner(stdscr)
    runner.run_forever()

if __name__ == '__main__':
    curses.wrapper(main)

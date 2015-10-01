# ______________
# 
# FNOOBLATZ 2000
# ______________
#
#
# License: http://en.wikipedia.org/wiki/WTFPL
#
# 
#   NEW!  IMPROVED!  FANCIER!  EASIER TO USE! 
#
#      THE AMAZING NEW FNOOBLATZ 2000!!!

import curses
import curses.textpad

from fnooblatz1000 import Fnooblatz1000

commands = {
'a': [13],
'alternator': [8],
'alterupdown': [9],
'alterleftright': [10],
'alphabetrotate': [25],
'b': [14],
'c': ['b', 25],
'd': ['c', 25],
'dada': ['d', 'right', 'a', 'right', 'd', 'right', 'a', 'right'],
'dd': ['down', 'down'],
'ddd': ['down', 'down', 'down'],
'donut': ['memorize', 'right', 'recall', 'right', 'recall',
          'down', 'recall', 'down', 'recall', 'left', 'recall', 
          'left', 'recall', 'up', 'recall', 'up'],
'dooa': [13],
'doob': [14],
'dooother': [12],
'down': [21],
'downspace': ['down', 'space'],
'dripdown': ['memorize','down','recall',
             'dd','recall','ddd','recall',
             'uuu','uu','up'],
'e': ['d', 25], 
'f': ['e', 25],
'g': ['f', 25],
'gleavespace': [26], 
'h': ['g', 25],
'home': [17],
'i': ['h', 25],
'j': ['i', 25],
'k': ['j', 25],
'l': ['k', 25],
'left': [18],
'leftspace': ['left', 'space'],
'll': ['left', 'left'],
'lll': ['left', 'left', 'left'],
'm': ['l', 25],
'megadonut': ['right', 'memorize', 'rr', 'recall', 'donut',
              'left', 'memorize', 'rrr', 'right', 'recall', 'donut',
              'lll', 'left', 'down', 'memorize', 'rrr', 'dd', 'right', 
              'recall', 'donut', 'up', 'lll', 'left', 'memorize', 
              'rrr', 'ddd', 'right', 'down', 'recall', 'donut',
              'uuu', 'up', 'lll', 'll', 'memorize', 'rr', 'ddd', 
              'down', 'recall', 'donut', 'uuu', 'up', 'lll', 
              'memorize', 'ddd', 'down', 'recall', 'donut', 
              'uuu', 'uu', 'memorize', 'dd', 'recall', 'donut', 
              'uuu', 'donut'],
'memorize': [23],
'n': ['m', 25],
'nop': [7],
'o': ['n', 25],
'p': ['o', 25],
'push': [27],
'pop': [28],
'q': ['p', 25],
'quiteupright': ['uuu','rrr'],
'r': ['q', 25],
'recall': [24],
'reset': [0],
'right': [19],
'rightspace': ['right', 'space'],
'rotate': [6],
'rotateboth': ['rotate', 'rotaterows'],
'rotatetwice': [6, 6],
'rotatereverse': [22],
'rotaterows': [5],
'rotaterowstwice': [5, 5],
'rr': ['right', 'right'],
'rrr': ['right', 'right', 'right'],
's': ['r', 25],
'samesquare': ['memorize', 'right', 'recall', 'down', 'recall', 'left', 'recall', 'up'],
'somestuff': ['rotate','rotate','dooother','alphabetrotate',
              'alterleftright','z','rotate'],
'space': [11],
'spacedonut': ['space', 'donut'],
'spacesquare': ['rightspace', 'downspace', 'leftspace', 'upspace'],
't': ['s', 25],
'u': ['t', 25],
'up': [20],
'upspace': ['up', 'space'],
'uu': ['up', 'up'],
'uuu': ['up', 'up', 'up'],
'v': ['u', 25],
'w': ['v', 25],
'x': ['w', 25],
'y': ['x', 25],
'z': ['y', 25],
}

class Fnooblatz2000(object):
    def __init__(self):
        self.fnoo = Fnooblatz1000()
    def do(self,command_list):
        expanded_command = self.expand(command_list)
        for button in expanded_command:
            self.fnoo.press_button(button)
    def expand(self,command):
        if isinstance(command, list):
            expanded_command = []
            for subcommand in command:
                expanded_command.extend(self.expand(subcommand))
            return expanded_command
        if isinstance(command, str):
            if command in commands:
                return self.expand(commands[command])
            else:
                return []
        if isinstance(command, int):
            return [command]

def main(stdscr):
    (max_y, max_x) = stdscr.getmaxyx()
    command_bar_window = curses.newwin(1, max_x - 1)
    command_bar = curses.textpad.Textbox(command_bar_window)
    command_bar.stripspaces = True
    display_pad = curses.newpad(max_y - 2, max_x - 1)
    fn = Fnooblatz2000()
    fn.fnoo.set_height(max_y - 2)
    fn.fnoo.set_width(max_x - 2)
    while True:
        display_pad.clear()
        for y in range(len(fn.fnoo.display)):
            for x in range(len(fn.fnoo.display[y])):
                if fn.fnoo.cursor_row == y and \
                        fn.fnoo.cursor_column == x:
                    display_pad.addch(y,x,ord(fn.fnoo.display[y][x]),curses.A_REVERSE)
                else:
                    display_pad.addch(y,x,ord(fn.fnoo.display[y][x]))
        display_pad.refresh(0, 0, 1, 1, max_y - 1, max_x - 2)
        command = command_bar.edit()
        command = command.strip()
        if command.isdigit():
            fn.do(int(command))
        else:
            fn.do(command)
        command_bar_window.clear()

if __name__ == '__main__':
    curses.wrapper(main)

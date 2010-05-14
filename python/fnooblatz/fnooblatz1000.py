# ________________
#
#  FNOOBLATZ 1000
# ________________
#
#
# License: http://en.wikipedia.org/wiki/WTFPL
#
#
# @ # * @ # * @ # * @ # * @ # * @ # * @# * @# * @#* @#*
#
#    In the Fabled and Far Away Land of Discordia, 
# Discordian programmers toil day and night, producing 
# programs in the infinite variety their varied and 
# variable customers continually demand. 
#    Modern Discordian programming is much concerned 
# with Functions and Objects and so forth just as you'll 
# find in many modern lands.  But while here we have 
# scorned our old computers and environments, with their
# seemingly unnecessary old complications, in Discordia
# all programmers hold in their hearts a special place
# for the Fnooblatz 1000, as its bizarre behaviors 
# continue to be the slippery fundament of all the 
# chaotic Discordian languages of today. 
#
# @ # * @ # * @ # * @ # * @ # * @# * @# * @#* @#*
#
#
#     Run "python fnooblatz1000.py" to use a Fnooblatz
# 1000 interactively. 

import collections 

def input_prompt():
    return "this is the input prompt: "

class Fnooblatz1000(object):
    def __init__(self):
        self.reset_everything()
    def printable_display(self):
        printable = '\n'
        for row in self.display:
            for column in row:
                printable += column
            printable += '\n'
        return printable
    def reset_everything(self):
        empty_row = collections.deque()
        empty_row.append('*')
        self.display = collections.deque()
        self.display.append(empty_row)
        self.instructions_executed = []
        self.alternator = True
        self.cursor_row = 0
        self.cursor_column = 0
    def check_cursor_bounds(self):
        if self.cursor_row < 0:
            self.cursor_row = 0
        if self.cursor_column < 0:
            self.cursor_column = 0
        while self.cursor_row >= len(self.display):
            self.cursor_row -= 1
        while self.cursor_column >= len(self.display[0]):
            self.cursor_column -= 1
    def execute_sequence(self,sequence):
        for instruction in sequence:
            self.press_button(instruction)
    def press_button(self,button_number):
        self.instructions_executed.append(button_number)
        if self.alternator:
            self.alternator = False
        else:
            self.alternator = True
        if button_number == 0:
            self.reset_everything()
            return
        # Resets everything.
        #
        # This functionality was desperately necessary 
        # of course on actual Fnooblatz 1000s, which if 
        # given difficult computations would overheat and 
        # smoke furiously.  I don't think there's an FB1000 
        # would have made it through the first night without 
        # this button.  Hopefully on this simulator it 
        # should be necessary slightly less desperately, 
        # but it's still useful for getting out of any of 
        # the confusing internal states a Fnooblatz is 
        # prone to! 
        if button_number == 1:
            for row in self.display:
                row.append('*')
            return
        if button_number == 2:
            new_row = collections.deque()
            for column in self.display[0]:
                new_row.append('*')
            self.display.append(new_row)
            return
        # The above commands to expand the Fnooblatz screen 
        # are necessary because the display starts 1 pixel by 
        # 1 pixel.  But why does it?  Well, besides the fact 
        # that in the old days people would run their Fnooblatz 
        # at as small a resolution as they actually needed, to 
        # conserve energy, or that a cheap one-pixel display 
        # would often be used to diagnose what's wrong with a 
        # sick Fnooblatz (so it couldn't burn out a whole 
        # expensive display), there's also the case of those 
        # folks who would insist that they just didn't need 
        # more than a one-pixel display to get by.  And it's 
        # true, you can read the news quite adequately one 
        # character at a time, if you're patient. 
        if button_number == 3:
            if len(self.display[0]) > 1:
                for row in self.display:
                    row.pop()
            self.check_cursor_bounds()
            return
        if button_number == 4:
            if len(self.display) > 1:
                self.display.pop()
            self.check_cursor_bounds()
            return
        # If you can make the display bigger, it's convenient 
        # to be able to make it smaller too, instead of just 
        # having to start all over! 
        if button_number == 5:
            for row in self.display:
                row.rotate()
            return
        if button_number == 6:
            self.display.rotate()
            return
        # Rotating the display, which gives us just barely
        # enough instructions to paint pictures! :D 
        if button_number == 7:
            return
        # Button seven doesn't do anything, 'anything' that is
        # except for all the stuff the Fnooblatz does every
        # instruction (alternate the alternator, etc.)-- but,
        # like, nothing EXTRA. 
        if button_number == 8:
            self.check_cursor_bounds()
            if self.alternator:
                self.display[self.cursor_row][self.cursor_column] = '|'
            else:
                self.display[self.cursor_row][self.cursor_column] = '-'
            return
        # This allows you to see the behavior of the alternator, 
        # and combined with the following instructions to move the
        # cursor can be useful for drawing. 
        if button_number == 9:
            if self.alternator:
                self.cursor_row += 1
            else:
                self.cursor_row -= 1
            self.check_cursor_bounds()
            return
        # The previous instruction allows you to go either up OR down!
        if button_number == 10:
            if self.alternator:
                self.cursor_column += 1
            else:
                self.cursor_column -= 1
            self.check_cursor_bounds()
            return
        # The previous instruction allows you to go either left OR right!
        self.display[0][0] = '@' 
        # Error signal for unpressableness, 
        # since if we've reached this point, 
        # an unpressable button has been pressed! 

def help_system():
    print """
________

HELLO AN
D WELCOM
E TO THE   please enter the number
FNOOBLAT   of the button you would
Z 1000 H   like help with, please.
ELP SYST
EM!!!!!!
________
"""
    help_with = raw_input(input_prompt())
    print
    if help_with.isdigit():
        help_with = int(help_with)
    if help_with == 'quit':
        print "Quits the Fnooblatz 1000 simulator, in case"
        print "there's ever any reason you want to leave."
        return
    if help_with == 'help':
        print "Helps you with things, like I've just helped you!"
        return
    if help_with == 'test':
        print """
Runs a series of tests on the Fnooblatz 1000 simulator, 
to see if it matches the specification specified for 
Fnooblatz 1000s by the Fnooblatz 1000 Specification 
Council.  It darn well ought to.
"""
        return
    if help_with == 0:
        print "Resets everything!!!"
        return
    if help_with == 1:
        print "Expands the Fnooblatz display by one column."
        return
    if help_with == 2:
        print "Expands the Fnooblatz display by one row."
        return
    if help_with == 3:
        print "Contracts the Fnooblatz display by one column."
        return
    if help_with == 4:
        print "Contracts the Fnooblatz display by one row."
        return
    if help_with == 5:
        print "Moves everything on the display one column to the right."
        return
    if help_with == 6:
        print "Moves everything on the display one row down."
        return
    if help_with == 7:
        print "Doesn't do anything (except alternate the alternator, etc)."
        return
    if help_with == 8:
        print "Outputs a | if the alternator is true and a - if it is false."
        return
    if help_with == 9:
        print "Goes down if the alternator is true, and up if it is false."
        return
    print "Never heard of that, sorry. :("

class TestSuiteRunner(object):
    def reset_score(self):
        self.tests_score = 0
        self.total_tests = 0
    def grade(self,boolean,error):
        if boolean:
            self.tests_score += 1
        else:
            print "FAILED: ", error
        self.total_tests += 1
    def run_test_suite(self,fnoo):
        self.reset_score()
        print
        fnoo.press_button(0) # Reset the Fnooblatz.
        # Size of the Fnooblatz should now be 1 by 1.
        self.grade(len(fnoo.display) == 1,
                   "Initial Fnooblatz display is not exactly 1 row long.")
        self.grade(len(fnoo.display[0]) == 1,
                   "Initial Fnooblatz display is not exactly 1 column wide.")
        fnoo.press_button(99999) # This button should not exist.
        self.grade(fnoo.display[0][0] == '@',
                   "Pressed button 99999 but upperlefterrorsquare didn't turn into '@'.")
        fnoo.press_button(1) # Attempt to expand Fnooblatz display one column. 
        self.grade(len(fnoo.display[0]) == 2,
                   "Pressing button 1 did not expand Fnooblatz display by a column.")
        fnoo.press_button(2) # Attempt to expand Fnooblatz display one row.
        self.grade(len(fnoo.display) == 2,
                   "Pressing button 2 did not expand Fnooblatz display by a row.")
        fnoo.press_button(3) # Attempt to contract Fnooblatz display one column.
        self.grade(len(fnoo.display[0]) == 1,
                   "Pressing button 3 did not contract Fnooblatz display by a column.")
        fnoo.press_button(3) 
        # Attempt to contract display by a column even though it's only one column 
        # wide already (should leave it the same).
        self.grade(len(fnoo.display[0]) == 1,
                   "Pressing button 3 after Fnooblatz display "
                   "was already 1 column changed width again.")
        fnoo.press_button(4) # Attempt to contract Fnooblatz display one row.
        self.grade(len(fnoo.display) == 1,
                   "Pressing button 4 did not contract Fnooblatz display by a row.")
        fnoo.press_button(4) 
        # Attempt to contract display by a row even though it's only one row 
        # long already (should leave it the same).
        self.grade(len(fnoo.display) == 1,
                   "Pressing button 4 after Fnooblatz display "
                   "was already 1 row changed length again.")
        fnoo.press_button(1)
        fnoo.press_button(1)
        fnoo.press_button(2)
        fnoo.press_button(2) # Expand the Fnooblatz a little so we can move it around. 
        self.grade(fnoo.display[0][0] == '@',
                   "The @ isn't in the upperleft corner for some reason.")
        fnoo.press_button(5) # Attempt to move display one column right. 
        self.grade(fnoo.display[0][1] == '@',
                   "Couldn't move the @ one right.")
        self.grade(fnoo.display[0][0] == '*',
                   "Upper left corner wasn't replaced with a * when the display moved right.")
        fnoo.press_button(6) # Attempt to move display one row down. 
        self.grade(fnoo.display[1][1] == '@',
                   "Couldn't move the @ one row down.")
        fnoo.press_button(99999) # Make a new @ 
        self.grade(fnoo.display[0][0] == '@',
                   "Couldn't make a new @")
        fnoo.press_button(6) # Attempt to move down one row with new @
        self.grade(fnoo.display[1][0] == '@',
                   "Couldn't move new @ down one row.")
        fnoo.execute_sequence([0]) # Should reset everything! 
        self.grade(len(fnoo.display) == 1, 
                   "Tried to reset Fnooblatz by sending a sequence with just 0,"
                   " but then display wasn't 1 row long.")
        self.grade(fnoo.display[0][0] == '*',
                   "Tried to reset Fnooblatz by sending a sequence with just 0,"
                   " but then the upper left corner wasn't a *.")
        fnoo.execute_sequence([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
                               1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
                               99999, 5, 99999, 6, 6, 99999, 6, 99999, 6, 
                               99999, 6, 99999, 6, 99999, 6, 
                               99999, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
                               5, 5, 99999, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 99999, 6, 
                               99999, 6, 99999, 6, 99999, 6, 99999, 
                               6, 6, 6, 5, 5, 5, 5, 3, 
                               3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4]) # Should draw an ! 
        self.grade(fnoo.printable_display() == """
********
********
***@@***
***@@***
***@@***
***@@***
***@@***
***@@***
********
***@@***
********
********
""", "Exclamation mark script printed out wrong.")
        fnoo.press_button(7)
        self.grade(fnoo.printable_display() == """
********
********
***@@***
***@@***
***@@***
***@@***
***@@***
***@@***
********
***@@***
********
********
""", "Pressing 7 changed the exclamation mark picture.")
        fnoo.press_button(0) # Reset, to reset the alternator. 
        self.grade(fnoo.alternator, "Alternator didn't start True.")
        fnoo.press_button(7) # Alternate the alternator. 
        self.grade(fnoo.alternator == False, "Alternator didn't alternate to False.")
        fnoo.press_button(7) # Alternate again.
        self.grade(fnoo.alternator, "Alternator didn't alternate back to True.")
        fnoo.press_button(0) # Leave the Fnooblatz clean! 
        print
        print "Passed", self.tests_score, "tests out of", self.total_tests, "!"
        print

def main():
    print "..bleep....bloop....blap.."
    fn = Fnooblatz1000()
    tester = TestSuiteRunner()
    tester.run_test_suite(fn) # tests! sweet!
    print "________________________"
    print
    print "FNOOBLATZ 1000 ACTIVATED"
    print "________________________"
    print "type 'quit' to quit"
    print "type 'help' for help on the Fnooblatz buttons"
    print "type 'print' to print a list of the instructions you've executed"
    print "otherwise, enter a number to simulate"
    print "pressing that button on the Fnooblatz 1000"
    print "________________________"
    while True:
        print
        print fn.printable_display()
        print
        input = raw_input(input_prompt())
        if input == 'quit':
            break
        if input == 'help':
            help_system()
            print 
            print "..returning from help system"
            print "||.........................."
            continue
        if input == 'print':
            print fn.instructions_executed
            continue
        if input.isdigit():
            fn.press_button(int(input))
            continue
        print "I did not understand your command. :("

if __name__ == "__main__":
    main()

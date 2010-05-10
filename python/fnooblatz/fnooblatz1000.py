# ________________
#
#  FNOOBLATZ 1000
# ________________
#
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
#     Run "python fnooblatz1000.py" to use a Fnooblatz
# 1000 interactively. 

import random
import collections

def input_prompt():
    prompt = ""
    for i in range(17):
        prompt += random.choice(['!','@','#','$','%','^','&','*'])
    prompt += ':'
    return prompt

def display_fnooblatz(fnoo):
    for row in fnoo.display:
        row_to_display = ""
        for column in row:
            row_to_display += column
        print row_to_display

class Fnooblatz1000(object):
    def __init__(self):
        self.reset_everything()
    def reset_everything(self):
        empty_row = collections.deque()
        empty_row.append('*')
        self.display = collections.deque()
        self.display.append(empty_row)
    def press_button(self,button_number):
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
            return
        if button_number == 4:
            if len(self.display) > 1:
                self.display.pop()
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

        self.display[0][0] = '@' # Error signal for unpressableness. 
        # If we've reached this point, an unpressable button 
        # has been pressed. 

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
        print
        print "Passed", self.tests_score, "tests out of", self.total_tests, "!"
        print

def main():
    print "..bleep....bloop....blap.."
    fn = Fnooblatz1000()
    print "________________________"
    print
    print "FNOOBLATZ 1000 ACTIVATED"
    print "________________________"
    print "type 'quit' to quit"
    print "type 'help' for help"
    print "type 'test' to test the simulator"
    print "otherwise, enter a number to simulate"
    print "pressing that button on the Fnooblatz 1000"
    print "________________________"
    while True:
        print
        display_fnooblatz(fn)
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
        if input == 'test':
            tester = TestSuiteRunner()
            tester.run_test_suite(fn) # tests! sweet!
            continue
        if input.isdigit():
            fn.press_button(int(input))
            continue
        print "I did not understand your command. :("

if __name__ == "__main__":
    main()

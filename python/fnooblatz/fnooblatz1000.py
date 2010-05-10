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
        self.display = [['*']]
    def press_button(self,button_number):
        if button_number == 0:
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
            self.reset_everything()
            return
        if button_number == 1:
            for row in self.display:
                row.append('*')
            return
        if button_number == 2:
            new_row = []
            for column in self.display[0]:
                new_row.append('*')
            self.display.append(new_row)
            return
        # If we've reached this point, an unpressable button 
        # has been pressed. 
        self.display[0][0] = '@' # Error signal for unpressableness. 

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
        fnoo.press_button(1) # Attempt to expand Fnooblatz one column. 
        self.grade(len(fnoo.display[0]) == 2,
                   "Pressing button 1 did not expand Fnooblatz by a column.")
        fnoo.press_button(2) # Attempt to expand Fnooblatz one row.
        self.grade(len(fnoo.display) == 2,
                   "pressing button 2 did not expand Fnooblatz by a row.")
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

# _________
#
# DOOHICKEY
# _________
#
#
# This is an absurdly simple Fifth Dimensional Chaos Matrix 
# component, to demonstrate how senselessly easy it is to 
# contribute something to the FDCM, if for any odd reason 
# you'd like to. 

class Doohickey(object):
    """
A doohickey has three methods, a, b, and other, which return 
the letter 'a', the letter 'b', and the opposite of whichever 
was returned previously (or 'b' the first time).  That's all. 

>>> doo = Doohickey()
>>> doo.other()
'b'
>>> doo.other()
'a'
>>> doo.a()
'a'
>>> doo.other()
'b'
>>> doo.b()
'b'
>>> doo.other()
'a'
>>> doo.other()
'b'
>>> doo.other()
'a'
"""
    def __init__(self):
        self.value = 'a'
    def a(self):
        self.value = 'a'
        return self.value
    def b(self):
        self.value = 'b'
        return self.value
    def other(self):
        if self.value == 'a':
            self.value = 'b'
        else:
            self.value = 'a'
        return self.value

if __name__ == '__main__':
    import doctest
    doctest.testmod()


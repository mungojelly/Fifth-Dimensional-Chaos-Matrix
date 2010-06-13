# __________________
#  
#  TRIPLE DOOHICKEY 
# __________________
# 
#
#  A triple doohickey contains three Doohickies 
# and combines their results to return three letter 
# strings. 

from doohickey import Doohickey

class TripleDoohickey(object):
    def __init__(self):
        self.first = Doohickey()
        self.second = Doohickey()
        self.third = Doohickey()
        self.a()
    def a(self):
        """Returns 'aba' and sets the Doohickies to a, b, and a.
        
        >>> doo = TripleDoohickey()
        >>> doo.a()
        'aba'
        """
        result = ''
        result += self.first.a()
        result += self.second.b()
        result += self.third.a()
        return result
    def b(self):
        """Returns 'bab' and sets the Doohickies to b, a and b.

        >>> doo = TripleDoohickey()
        >>> doo.b()
        'bab'
        """
        result = ''
        result += self.first.b()
        result += self.second.a()
        result += self.third.b()
        return result
    def other(self):
        """Returns the opposite of the last time, or 'bab' at first.

        >>> doo = TripleDoohickey()
        >>> doo.other()
        'bab'
        >>> doo.other()
        'aba'
        >>> doo.a()
        'aba'
        >>> doo.other()
        'bab'
        >>> doo.b()
        'bab'
        >>> doo.other()
        'aba'
        >>> doo.other()
        'bab'
        >>> doo.other()
        'aba'
        """
        result = ''
        result += self.first.other()
        result += self.second.other()
        result += self.third.other()
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()


#
# _______________
# ALPHABETROTATOR
# _!_!_!___!_!_!_
# __!_!_____!_!__
#    !       !   
# 
# A device which, given a letter of the alphabet, 
# returns the next letter (or 'a' for 'z').  It 
# leaves other things unchanged. 

rotation_chart = \
{'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h',
 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o',
 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v',
 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a', 'A': 'B', 'B': 'C',
 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J',
 'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O', 'O': 'P', 'P': 'Q',
 'Q': 'R', 'R': 'S', 'S': 'T', 'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X',
 'X': 'Y', 'Y': 'Z', 'Z': 'A'}

def rotate(character):
    """Rotates a character to the next in the alphabet, 
    or z back around to a.

    >>> rotate('a')
    'b'
    >>> rotate('m')
    'n'
    >>> rotate('z')
    'a'
    """
    if character in rotation_chart:
        return rotation_chart[character]
    else:
        return character

if __name__ == '__main__':
    import doctest
    doctest.testmod()

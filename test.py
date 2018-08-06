from texttools import *
import textwrap
from difflib import SequenceMatcher

if __name__ == '__main__':
    width = 80

    marqueeprint("[[PRINT TEST]]")
    marqueeprint("MARQUEE PRINT")
    leftprint('Justified Left')
    rightprint('Justified Right')
    centerprint('Center Print')
    marqueeprint("Odd number of char")
    print(lr_justify('Echoooo', 'ooooooeche', width))

    marqueeprint("[[SIMILAR STRING TEST]]")
    similarstring('A Homer Simpson', 'Mr Homo Sapiens')

    marqueeprint("[[GRID OUTPUT TEST]]")

    # takes a 1:1 dict and prints it centered and pretty
    gridoutput({'Our Hero': 'Joe Jostar'})
    gridoutput({'But it was me!': 'Dio Brando'})

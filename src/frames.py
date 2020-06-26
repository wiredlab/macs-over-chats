#!/usr/bin/env python3

from random import choices
import string
from itertools import cycle


# Reference for the Luhn mod N algorithm to compute a check symbol for a
# sequence chosen from an arbitrary set of symbols:
# https://en.wikipedia.org/wiki/Luhn_mod_N_algorithm


alphabet = string.ascii_uppercase

nato = {
    # ICAO or NATO phonetic alphabet
    'A': 'ALFA',
    'B': 'BRAVO',
    'C': 'CHARLIE',
    'D': 'DELTA',
    'E': 'ECHO',
    'F': 'FOXTROT',
    'G': 'GOLF',
    'H': 'HOTEL',
    'I': 'INDIA',
    'J': 'JULIETT',
    'K': 'KILO',
    'L': 'LIMA',
    'M': 'MIKE',
    'N': 'NOVEMBER',
    'O': 'OSCAR',
    'P': 'PAPA',
    'Q': 'QUEBEC',
    'R': 'ROMEO',
    'S': 'SIERRA',
    'T': 'TANGO',
    'U': 'UNIFORM',
    'V': 'VICTOR',
    'W': 'WHISKEY',
    'X': 'X-RAY',
    'Y': 'YANKEE',
    'Z': 'ZULU',
}

nato_inv = {v: k for k, v in nato.items()}


def encode(i, alphabet=alphabet):
    """Code --> Symbol

    Code is a zero-based integer index into the alphabet list.
    """
    if isinstance(i, int):
        return alphabet[i]
    else:
        return [alphabet[x] for x in i]


def decode(c, alphabet=alphabet):
    """Symbol --> Code

    Code is a zero-based integer index into the alphabet list.
    """
    if isinstance(c, type(alphabet[0])):
        return alphabet.index(c)
    else:
        return tuple(alphabet.index(x) for x in c)


def _modNCheckCode(s, N=len(alphabet)):
    """Given an iterable s of codes, return the Luhn mod N check code.

    Codes are zero-based integer indices into the alphabet list.
    """
    remainder = 0

    for code, factor in zip(reversed(decode(s)),
                            cycle((2, 1))):
        # factor alternates 2, 1, 2, 1, ...
        addend = factor * code
        addend = int(addend / N) + (addend % N)
        remainder = (remainder + addend) % N

    return (N - remainder) % N


def generate(s, alphabet=alphabet):
    """Generate a Luhn mod N check symbol given the input s.

    s can be a single symbol or an iterable of symbols from the given alphabet.
    """
    return encode(_modNCheckCode(s, len(alphabet)))


def validate(s, alphabet=alphabet):
    """Check if the last symbol matches the Luhn mod N check of the rest of the
    symbols according to the given alphabet.
    """
    checkCode = _modNCheckCode(s[:-1], len(alphabet))
    return checkCode == decode(s[-1])


def genframe(n, alphabet=alphabet):
    """Generate a random frame of n symbols from the given alphabet where the
    last digit is the Luhn mod N check of the rest of the symbols.
    """
    frame = choices(alphabet, k=(n-1))
    frame += generate(frame, alphabet)
    return frame


for i in range(1000):
    f = genframe(5)
    phonetic = [nato[x] for x in f]
    s = ' '.join(phonetic)
    print(s)

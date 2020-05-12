try:
    # python 3 compat
    from html.entities import codepoint2name, name2codepoint
    unichr = chr
except ImportError:
    from htmlentitydefs import codepoint2name, name2codepoint

import re


__version__ = '0.3.0'


def encode(source):
    new_source = ''

    for char in source:
        val = ord(char)
        if val in codepoint2name:
            char = '&%s;' % codepoint2name[val]
        new_source += char

    return new_source


def decode(source):
    for entitie in re.findall('&(?:[a-z][a-z0-9]+);', source, re.I):
        entitie = entitie.replace('&', '')
        entitie = entitie.replace(';', '')
        source = source.replace('&%s;' % entitie, unichr(name2codepoint[entitie]))
    return source

try:
    # python 3 compat
    from html.entities import codepoint2name, name2codepoint
    unichr = chr
except ImportError:
    from htmlentitydefs import codepoint2name, name2codepoint

import re


__version__ = '0.3.0'


def encode(source, mcodepoint2name=None):
    new_source = ''

    if mcodepoint2name is None:
        mcodepoint2name = codepoint2name

    for char in source:
        val = ord(char)
        if val in mcodepoint2name:
            char = '&%s;' % mcodepoint2name[val]
        new_source += char

    return new_source


def decode(source, name2codepointm=None):
    if name2codepointm is None:
        name2codepointm = name2codepoint

    for entitie in re.findall('&(?:[a-z][a-z0-9]+);', source, re.I):
        entitie = entitie.replace('&', '')
        entitie = entitie.replace(';', '')
        source = source.replace('&%s;' % entitie, unichr(name2codepointm[entitie]))
    return source

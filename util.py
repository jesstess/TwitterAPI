# -*- coding: utf-8 -*-
import os
import codecs
import sys

def encode(text):
    """
    Encode text so it can be safely printed to the terminal regardless of
    operating system.

    Tweets are in UTF-8, which will crash Windows cmd.exe.
    """
    if os.name == 'nt':     # Windows
        encoding = 'cp437'
    else:
        encoding = 'utf8'   # Mac / Linux
    return text.encode(encoding, 'xmlcharrefreplace').decode(encoding)

def safe_print(text):
    '''
    This prints text to the terminal, regardless of the OS.

    It uses sys.stdout plus the codecs module to enforce UTF-8.
    '''
    assert type(text) == unicode
    if os.name == 'nt':     # Windows
        encoding = 'cp437'
    else:
        encoding = 'utf8'   # Mac / Linux
    wrapped_stdout = codecs.getwriter(encoding)(sys.stdout)
    wrapped_stdout.write(text)
    wrapped_stdout.write('\n')

def test_safe_print():
    '''
    This has a bunch of possibly scary Unicode test cases to make
    sure that safe_print works on your platform.
    '''
    safe_print(u'☂☀♠')


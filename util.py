# -*- coding: utf-8 -*-
import os
import codecs
import sys

def safe_print(text):
    '''
    This prints text to the terminal, regardless of the OS.

    It uses sys.stdout plus the codecs module to enforce UTF-8.
    '''
    if os.name == 'nt':     # Windows
        codec = codecs.lookup('cp437')
    else:                   # Mac / Linux
        codec = codecs.lookup('utf8')
    wrapped_stdout = codec.streamwriter(sys.stdout, errors='replace')
    wrapped_stdout.write(text)
    wrapped_stdout.write('\n')

def test_safe_print():
    '''
    This has a bunch of possibly scary Unicode test cases to make
    sure that safe_print works on your platform.
    '''
    safe_print(u'☂☀♠')

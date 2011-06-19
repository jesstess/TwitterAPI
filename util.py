import os

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

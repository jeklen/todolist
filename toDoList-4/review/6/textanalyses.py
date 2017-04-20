import string

def main():
    fname = raw_input('File to analyze: ')
    f = open('fname', 'r')
    text = f.read()
    numchars = len(text)
    f.seek(0)
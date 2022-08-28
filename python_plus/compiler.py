import argparse

def convert(s):
    r = ''
    for l in s.splitlines():
        string = ''
        newline = True
        colon = False
        check = True
        for p, q in zip(l, list(l[1:])+[None]):
            if check:
                if not string:
                    if p == '$':
                        r += 'print'
                    elif p == '§':
                        r += 'input'
                    elif p == '£':
                        if not newline:
                            r += ' '
                        else:
                            colon = True
                        r += 'for '
                    elif p == '€':
                        if not newline:
                            r += ' '
                        else:
                            colon = True
                        r += 'while '
                    elif p == '?':
                        if not newline:
                            r += ' '
                        else:
                            colon = True
                        r += 'if '
                    elif p == '!':
                        if not newline:
                            r += ' '
                        else:
                            colon = True
                        r += 'else '
                    elif p == '±':
                        colon = True
                        r += 'elif '
                    elif p == ':':
                        r += ' in '
                    elif p == q == '&':
                        r += ' and '
                        check = False
                    elif p == q == '|':
                        r += ' or '
                        check = False
                    elif p == q == '~':
                        r += ' not '
                        check = False
                    elif p in '"\'':
                        string = p
                    elif p in ' \t':
                        r += p
                        newline = newline and True
                        continue
                    else:
                        r += p
                    newline = False
                    continue
                r += p
            else:
                check = True
        r += colon * ':' + '\n'
    return r

def from_file():
    parser = argparse.ArgumentParser(prog ='pythonplus',
                                     description ='Run a Python+ file using the pythonplus command')
    parser.add_argument('filename', metavar ='filename', type=str, nargs=1, help= 'The filename of the file to run using the Python+ Compiler')
    args = parser.parse_args()
    try:
        with open(args.filename[0]) as f:
            exec(convert(f.read()))
            return 0
    except:
        pass
    print('An error occurred')
    return 1

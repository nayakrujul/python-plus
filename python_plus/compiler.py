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
    parser.add_argument('debug', metavar ='d', type=bool, nargs='?', const=False, help= 'Debug the program by showing the converted Python code?')
    args = parser.parse_args()
    try:
        with open(args.filename[0]) as f:
            python_plus_code = f.read().rstrip()
            python_code = convert(python_plus_code)
            if parser.debug:
                print('\033[2mPython+ Code:\033[0m\n' + python_plus_code + '\n')
                print('\033[2mPython3 Code:\033[0m\n' + python_code + '\n')
                print('\033[2mOutput:\033[0m')
            exec(python_code)
            return 0
    except Exception as e:
        print('\033[1;31mAn error occurred:', e, '\033[0m')
        return 1

import sys


def error():
    quit(f'Error on Line {line_num}:\n{line}')


__author__ = 'Aarav Dave'
if len(sys.argv) > 1:
    __file__ = sys.argv[1]
else:
    __file__ = 'code.qps'

vars = {}
nest = []

with open(__file__) as file:
    for line_num, line in enumerate(file.readlines()):
        line = line.rstrip()
        if (not line) or line.startswith('//'):
            continue

        line = line.lstrip()
        current = ['']
        in_string = 0
        for char in line:
            if char == '\'':
                in_string = 1 - in_string
            if char in '(). ' and not in_string:
                current.append('')
                continue
            if char == ';':
                break

            current[-1] += char

        while '' in current:
            current.remove('')

        main, *rest = current

        if main == 'log':
            if rest:
                if len(rest) > 1:
                    if rest[0] in vars:
                        rest[0] = vars[rest[0]]
                    print(rest[0].strip('\''))
                else:
                    error()
            else:
                print()
        if main == 'var':
            name, _, *rest = rest
        else:
            print(current)

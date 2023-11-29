import sys
import fileinput

if len(sys.argv) < 2:
    print('Usage: python import_fix.py <filename>')
    sys.exit(1)

filename = sys.argv[1]

print(f'Working with file: {filename}')

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('import res_rc', 'from . import res_rc'), end='')

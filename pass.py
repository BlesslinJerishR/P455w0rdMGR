#! python3.
# pass.py - An insecure easily crackable Password Manager with -3 Levels of Zero Day Security written in python 3.

import sys
import pyperclip

PASSWORDS = {
    'email': 'wd&lemfkoejf98ueyuf984u9htfjrebfg439',
    'instagram': 'fneiufg8eygfr4376y84ryf8gtgh',
    'facebook': '12345678'
}

if len(sys.argv) > 2:
    print('usage : python pass.py [acc] - ctrl+c password')
    sys.exit()

acc = sys.argv[1]

if acc in PASSWORDS:
    pyperclip.copy(PASSWORDS[acc])
    print(f'Secret key for {acc} copied to your clipboard.')
else:
    print('Zero Accounts found')


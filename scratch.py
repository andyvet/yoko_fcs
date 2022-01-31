import re

with open(r'H:\python\projects\yoko_fcs\TIR10601.edf', 'rb') as file:
    line = str(file.read())
    pos = line.find('BKCM')
    print(pos)
    print(line.find('PVI', pos, pos + 150))

with open(r'H:\python\projects\yoko_fcs\AIRA10101.edf', 'rb') as file:
    line = str(file.read())
    print(re.findall(r'[A-Z,_]{2,}', line))

with open(r'H:\python\projects\yoko_fcs\RL_AXENS1.edf', 'rb') as file:
    line = str(file.read())
    print(re.findall(r'[A-Z,_]{2,}', line))


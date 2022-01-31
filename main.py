import re

BLOCK = []

with open(r'H:\python\projects\yoko_fcs\TIR10601.edf', 'rb') as file:
    for line in file:
        line = str(line)
        print(re.findall(r'[A-Z]{2,}\d+', line)[-1])
        print(re.findall(r'[A-Z]{3,}', line)[13])

with open(r'H:\python\projects\yoko_fcs\AIRA10101.edf', 'rb') as file:
    for line in file:
        line = str(line)
        print(re.findall(r'[A-Z]{2,}\d+', line)[-1])
        print(re.findall(r'[A-Z]{3,}', line)[13])

with open(r'H:\python\projects\yoko_fcs\RL_AXENS1.edf', 'rb') as file:
    for line in file:
        line = str(line)
        print(re.findall(r'[A-Z]{2,}\d+', line))
        print(re.findall(r'[A-Z]{2,}', line))
import re
import os


def add_fb(path_to_file):
    global func_blocks
    with open(path_to_file, 'rb') as file:
        line = file.read()
        #key = str(re.findall(r'[A-Z-_0-9]{3,}\d*', str(line[512:528])))
        key = str(re.findall(r'[A-Z-]{2,}\d*', str(line[532:540]))[0])
        func_blocks[key] += 1


func_blocks = {'PVI': 0, 'PID': 0, 'CALCU': 0, 'MLD-SW': 0, 'LC64': 0, 'SPLIT': 0,
               'AS-H': 0, 'FOUT': 0, 'ST16': 0, 'VELLIM': 0, 'RL': 0, 'RS': 0,
               'SFCSW': 0, 'BDSET-1': 0, 'INTEG': 0, 'TM': 0, 'SIO-22': 0,
               'MC-2': 0, 'SIO-11': 0, 'SW-33': 0, 'ONOFF': 0, 'BDA-L': 0,
               'DSET': 0, 'MC-3': 0, 'SIO-21': 0}
project_path = r'H:/Yoko/ISOMER/'
paths_to_FBs = []
path_to_file = ''

with os.scandir(project_path) as listOfEntries:
    for entry in listOfEntries:
        if 'FCS' in str(entry):
            paths_to_FBs.append(project_path + entry.name + '/FUNCTION_BLOCK/')

for fcs in paths_to_FBs:
    for dr in range(1,201):
        path_to_file = str(fcs) + 'DR0' + '{:03}'.format(dr) + '/'
        list_FBs = os.listdir(path_to_file)
        for file in list_FBs:
            if file.endswith('.edf'):
                add_fb(path_to_file + file)

print(func_blocks)
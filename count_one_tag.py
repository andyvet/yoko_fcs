import os
import re

tag_counter = 0
project_path = r'H:/Yoko/ISOMER/'
paths_to_FBs = []
path_to_file = ''


def counter(path_to_file):
    with open(path_to_file, 'rb') as file:
        line = str(file.read())
        pos = line.find('BKCM')
        if line.find('PVI', pos, pos + 150) != -1:
            global tag_counter
            tag_counter += 1
            #print(path_to_file)

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
                counter(path_to_file + file)

print(tag_counter)
print(paths_to_FBs)
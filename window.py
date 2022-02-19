import os

path_to_file = r'H:\Yoko\ISOMER\HIS1064\WINDOW\11~EDF\\'


def change_scale(path_to_file, scale_type):
    x = 0
    with open(path_to_file, 'r+', encoding="utf8") as file:
        for line in file:
            if 'ScalingMode' in line:
                print(line, end='')


change_scale(path_to_file + 'main.xaml', 'FreeScale')

import os
import pathlib

#project_path = pathlib.Path.cwd()
project_path = 'H:/Yoko/ISOMER/HIS1064/WINDOW'


def get_windows_names(project_path):
    paths_to_grs = []
    with os.scandir(project_path) as entries_list:
        for entry in entries_list:
            if 'EDF' in str(entry):
                paths_to_grs.append(str(project_path) + r'/' + entry.name + r'/')
    return paths_to_grs


def change_something(path_to_file, var_1, var_2):
    path = pathlib.Path(path_to_file)
    text = path.read_text(encoding="utf-8-sig").replace(var_1, var_2)
    path.write_text(text, encoding="utf-8-sig")


for window_name in get_windows_names(project_path):
    #change_something(window_name + 'main.xaml', 'FixedRatio', 'FreeScale')
    print(window_name)

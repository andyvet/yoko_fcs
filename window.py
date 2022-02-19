import os
import pathlib

project_path = pathlib.Path.cwd()
paths_to_GRs = []


with os.scandir(project_path) as entries_list:
    for entry in entries_list:
        if 'EDF' in str(entry):
            paths_to_GRs.append(str(project_path) + r'/' + entry.name + r'/')


def change_something(path_to_file, var_1, var_2):
    path = pathlib.Path(path_to_file)
    text = path.read_text(encoding="utf-8-sig").replace(var_1, var_2)
    path.write_text(text, encoding="utf-8-sig")


for gr_window in paths_to_GRs:
    change_something(gr_window + 'main.xaml', 'FixedRatio', 'FreeScale')

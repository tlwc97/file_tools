import os
import sys
import pandas
from pprint import pprint as pp


here = os.path.dirname(os.path.realpath(__file__))
parent = "\\".join(here.split("\\")[:-2])
sys.path.append(parent)


from file_tools.path_container import *

path = "{}\\test_file.txt".format(here)

x = Path(path)


def show_path_object(print_flag=True):

    if print_flag == False:

        return

    print("Path elements:\n---------------")
    print("path: ")
    print(x.Path)
    print("\n")

    print("file")
    print(x.File)
    print("\n")

    print("dir")
    print(x.dir)
    print("\n")

    print("name")
    print(x.name)
    print("\n")

    print("ext")
    print(x.ext)
    print("\n-------------------")


def run_main_test(print_flag=True):

    ext_change = "xlsx"

    name_change = "new_test_file"

    dir_change = "C:\\Program Files'"

    path_change = path

    file_change = "third_file.sql"

    show_path_object(print_flag)

    print("\n")

    print("x.ext = \"{}\"\n------------".format(ext_change))
    x.ext = ext_change
    show_path_object(print_flag)

    assert ext_change == x.ext
    print("extension change passed")

    print("\n")

    print("x.name = \"{}\"\n------------".format(name_change))
    x.name = name_change
    show_path_object(print_flag)

    assert name_change == x.name
    print("name change passed")

    print("\n")

    print("x.dir = \"{}\"\n------------".format(dir_change))
    x.dir = dir_change
    show_path_object(print_flag)

    assert dir_change == x.dir

    print("dir change passed")

    print("\n")

    print("x.Path = \"{}\"\n------------".format(path_change))
    x.Path = path_change
    show_path_object(print_flag)

    assert path_change == x.Path

    print("path change passed")

    print("\n")

    print("x.File = \"{}\"\n------------".format(file_change))
    x.File = file_change
    show_path_object(print_flag)

    assert file_change == x.File

    print("file change passed")

    print("\npath_container_test.run_main_test() passed")




















#
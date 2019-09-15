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

from pprint import pprint as pp


def show_path_object():

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


def run_main_test():

    show_path_object()

    input("\n")

    print("x.ext = 'xlsx'\n------------")
    x.ext = "xlsx"
    show_path_object()

    input("\n")

    print("x.name = 'new_test_file'\n------------")
    x.name = "new_test_file"
    show_path_object()

    input("\n")

    print("x.dir = 'C:\\Program Files'\n------------")
    x.dir = "C:\\Program Files"
    show_path_object()

    input("\n")

    print("x(path)\n------------")
    x.Path = path
    show_path_object()

    input("\n")

    print("x.file('third_file.sql')\n------------")
    x.File = "third_file.sql"
    show_path_object()

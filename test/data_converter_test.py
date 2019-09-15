import os
import sys
import pandas
from pprint import pprint as pp

here = os.path.dirname(os.path.realpath(__file__))
parent = "\\".join(here.split("\\")[:-2])
sys.path.append(parent)


def show_data_converter():

    from file_tools import data_converter

    print(data_converter)
    print(type(data_converter))
    print(dir(data_converter))

    input()
    print("\n")
    print("__cached__\n------------")
    print(data_converter.__cached__)
    input("\n")
    print("__builtins__\n------------")
    print(data_converter.__builtins__)
    # for i in data_converter.__builtins__:
    #
    #     print(i + "\n---------------")
    #     print(data_converter.__builtins__[i])
    #     input("\n")

    print("__doc__\n------------")
    print(data_converter.__doc__)
    input("\n")
    print("__file__\n------------")
    print(data_converter.__file__)
    input("\n")
    print("__loader__\n------------")
    print(data_converter.__loader__)
    input("\n")
    print("__name__\n------------")
    print(data_converter.__name__)
    input("\n")
    print("__package__\n------------")
    print(data_converter.__package__)
    input("\n")
    print("__spec__\n------------")
    print(data_converter.__spec__)
    input("\n")

    del data_converter


from file_tools.data_converter import *


class _Test:

    @classmethod
    def _data_path_list(cls):

        return [
            "{}\\exists.csv".format(here),
            "{}\\exists.xlsx".format(here),
            "{}\\exists.json".format(here),
        ]

    @classmethod
    def _file_path_list(cls):
        return [
            "{}\\exists.txt".format(here),
            "{}\\exists.sql".format(here),
            "{}\\exists.py".format(here),
            "{}\\exists.html".format(here),
            "{}\\exists.bat".format(here),
        ]

    @classmethod
    def _get_test_df(cls):

        cols = ["test_col_1", "test_col_2", "test_col_3"]

        row1 = ["hello", "coffee", "blue"]

        row2 = ["goodbye", "tea", "red"]

        return pandas.DataFrame(data=[row1, row2], columns=cols)

    @classmethod
    def _df_test(cls):

        path_list = cls._data_path_list()

        df_list = []

        for i in path_list:

            df_list.append(df(i))

        for i in df_list:

            assert isinstance(i, pandas.DataFrame)

        print("_df_test() passed")


    @classmethod
    def _string_test(cls):

        path_list = cls._file_path_list()

        string_list = []

        for i in path_list:

            string_list.append(string(i))

        for i in string_list:

            assert isinstance(i, str)

        print("_string_test() passed")


    @classmethod
    def _csv_test(cls):

        path = "{}\\df_to_file.csv".format(here)

        df(path, cls._get_test_df())

        print("_csv_test() passed")


    @classmethod
    def _xlsx_test(cls):

        path = "{}\\df_to_file.xlsx".format(here)

        df(path, cls._get_test_df())

        print("_xlsx_test() passed")


    @classmethod
    def _json_test(cls):

        path = "{}\\df_to_file.json".format(here)

        df(path, cls._get_test_df())

        print("_json_test() using df() passed")
        #
        # json(path, cls._get_test_df())
        #
        # print("_json_test() using json() passed")


    @classmethod
    def _html_test(cls):

        path = "{}\\df_to_file.html".format(here)

        df(path, cls._get_test_df())

        print("_html_test() from df passed")

        path = "{}\\string_to_file.html".format(here)

        string(path, "<p>Here goes nothin kid</p>")

        print("_html_test() from string passed")


    @classmethod
    def _files_test(cls):

        for i in cls._data_path_list():

            other_path = [j for j in cls._data_path_list() if j != i]

            for k in other_path:

                try:

                    dest_path = file(i, k)

                    print("file() passed with src={} and dest={}".format(i, k))

                except:

                    raise RuntimeError("file() failed with src={} and dest={}".format(i, k))

    @classmethod
    def run_all_tests(cls):

        try:

            cls._df_test()

        except:

            print("_df_test() failed")

        try:

            cls._string_test()

        except:

            print("_string_test() failed")

        try:

            cls._csv_test()

        except:

            print("_csv_test() failed")

        try:

            cls._xlsx_test()

        except:

            print("_xlsx_test() failed")

        try:

            cls._json_test()

        except:

            print("_json_test() failed")

        try:

            cls._html_test()

        except:

            print("_html_test() failed")

        cls._files_test()

_Test.run_all_tests()

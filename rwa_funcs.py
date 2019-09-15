import os
import sys
import pandas
from datetime import datetime
from collections import namedtuple

here = os.path.dirname(os.path.realpath(__file__))

"""
function naming convention:
def [data_code]_[output_type_code]_[w/a flag](in, out, wa_flag):
data_code - data type or file type being read
output_type_code - data type or file type being writen to
w/a flag - indicates whether to overwrite or append
"""

str_list = [
    "txt",
    "py",
    "sql",
    "html",
]

ext_list = ["csv", "xlsx", "json"] + str_list

class FileFunctions:


    @classmethod
    def _get_file(cls, path):

        return path.split("\\")[-1]

    @classmethod
    def _get_file_name(cls, path):

        return ".".join(cls._get_file(path).split(".")[:-1])

    @classmethod
    def _get_file_ext(cls, path):

        return cls._get_file(path).split(".")[-1]

    @classmethod
    def _get_header_flag(cls, mode=None):

        if mode == "a":

            return False

        else:

            return True

    @classmethod
    def str_file_w(cls, src, dest):
        print("str_file_w()")
        print(src)
        print(dest)

        path = dest

        with open(path, "w") as f:

            f.write(src)

        return path

    @classmethod
    def str_file_a(cls, src, dest):

        path = dest

        with open(path, "a") as f:

            f.write(src)

        return path

    @classmethod
    def file_str_w(cls, src, dest):

        str_obj = dest

        with open(src, "r") as f:

            str_obj = f.read()

        return str_obj

    @classmethod
    def file_str_a(cls, src, dest):

        str_obj = dest

        with open(src, "r") as f:

            new_str = f.read()

        return "{}\n{}".format(str_obj, new_str)

    @classmethod
    def csv_df_w(cls, src, dest):

        path = src

        return pandas.read_csv(path)

    @classmethod
    def csv_df_a(cls, src, dest):

        path = src

        df = dest

        new_df = pandas.read_csv(path)

        return pandas.concat([df, new_df])

    @classmethod
    def df_csv_w(cls, src, dest, mode="w"):

        df = src

        path = dest

        with open(path, mode) as csv_file:

            df.to_csv(csv_file, na_rep="null", index=False,

                      header=cls._get_header_flag(mode))

        return path

    @classmethod
    def df_csv_a(cls, src, dest):

        return cls.df_csv_w(src, dest, "a")

    @classmethod
    def xlsx_df_w(cls, src, dest):

        path = src

        try:

            return pandas.read_excel(path, sheet_name=cls._get_file_name(path))

        except:

            return pandas.read_excel(path)

    @classmethod
    def xlsx_df_a(cls, src, dest):

        path = src

        df = dest

        try:

            new_df = pandas.read_excel(path, sheet_name=cls._get_file_name(path))

        except:

            new_df = pandas.read_excel(path, sheet_name=0)


        return pandas.concat([df, new_df])

    @classmethod
    def df_xlsx_w(cls, src, dest):

        df = src

        path = dest

        df.to_excel(path, index=False, sheet_name=cls._get_file_name(path))

        return path

    @classmethod
    def df_xlsx_a(cls, src, dest):

        new_df = src

        path = dest

        if cls.is_path(path):

            df = cls.xlsx_df_w(src, dest)

            new_df = pandas.concat(df, new_df)

        new_df.to_excel(path, index=False, header=False,

                    sheet_name=cls._get_file_name(path))

        return path

    @classmethod
    def json_df_w(cls, src, dest):

        path = src

        df = dest

        return pandas.read_json(path)

    @classmethod
    def json_df_a(cls, src, dest):

        path = src

        df = dest

        new_df = pandas.read_json(path)

        return pandas.concat([df, new_df])

    @classmethod
    def df_json_w(cls, src, dest, mode="w"):

        df = src

        path = dest

        with open(path, mode) as json_file:

            df.to_json(json_file)

        return path

    @classmethod
    def df_json_a(cls, src, dest):

        return cls.df_json_w(src, dest, "a")

    @classmethod
    def html_df_w(cls, src, dest):

        path = src

        return pandas.read_html(path)

    @classmethod
    def html_df_a(cls, src, dest):

        path = src

        df = dest

        new_df = pandas.read_html(path)

        return pandas.concat([df, new_df])

    @classmethod
    def df_html_w(cls, src, dest, mode="w"):

        df = src

        path = dest

        with open(path, mode) as html_file:

            df.to_html(html_file)

        return path

    @classmethod
    def df_html_a(cls, src, dest):

        return cls.df_html_w(src, dest, "a")

    @classmethod
    def is_str(cls, obj):

        return isinstance(obj, str)

    @classmethod
    def id_dataframe(cls, obj):

        return isinstance(obj, pandas.DataFrame)

    @classmethod
    def in_file_types(cls, obj):

        if cls.is_str(obj):

            return FileFunctions._get_file_ext(obj) in ext_list

        return False

    @classmethod
    def is_path(cls, str_obj):

        if cls.in_file_types(str_obj):

            if os.path.isfile(str_obj):

                return True

        return False

    @classmethod
    def is_dataframe(cls, obj):

        return isinstance(obj, pandas.DataFrame)

    @classmethod
    def get_src_code(cls, src):

        if cls.is_dataframe(src):

            return "df"

        elif cls.is_str(src):

            ext = FileFunctions._get_file_ext(src)

            if ext in ext_list:

                if cls.is_path(src):

                    if ext in set(ext_list).difference(str_list):

                        return ext

                    else:

                        return "file"
                else:

                    if ext in set(ext_list).difference(str_list):

                        raise FileNotFoundError

                    else:

                        return "str"

            else:

                return "str"

        else:

            raise TypeError("src object must be str or pandas.DataFrame")

    @classmethod
    def get_dest_code(cls, dest):

        if cls.is_dataframe(dest):

            return "df"

        elif cls.is_str(dest):

            if cls.in_file_types(dest):



                ext = FileFunctions._get_file_ext(dest)

                if ext not in str_list:

                    return ext

                else:

                    return "file"
            else:

                return "str"

    @classmethod
    def get_file_function(cls, src, dest, mode):

        print("get_file_functions()")

        src_cd = cls.get_src_code(src)

        dest_cd = cls.get_dest_code(dest)

        print(src_cd)

        print(dest_cd)

        try:
            func = getattr(cls, "{}_{}_{}".format(src_cd, dest_cd, mode))
        except:
            print("failed getting function")
        return getattr(cls, "{}_{}_{}".format(src_cd, dest_cd, mode))


def convert(src, dest):

    print("convert()")
    func = FileFunctions.get_file_function(src, dest, "w")

    val = func(src, dest)

    return val

def append(src, dest):

    func = FileFunctions.get_file_function(src, dest, "w")

    val = func(src, dest)

    return val
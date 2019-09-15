import pandas

__all__ = [
    "get_file_name",
    "get_ext",
    "df",
    "string",
    "file",
]

class _Df:

    @classmethod
    def _is(cls, obj):

        return isinstance(obj, pandas.DataFrame)


    @classmethod
    def csv(cls, path):

        return pandas.read_csv(path)


    @classmethod
    def xlsx(cls, path):

        try:

            return pandas.read_excel(path, sheet_name=_File._get_file_name(path))

        except:

            return pandas.read_excel(path)


    @classmethod
    def json(cls, path):

        return pandas.read_json(path)


    @classmethod
    def df(cls, path, obj=None):

        if obj is None:

            ext = _File._get_ext(path)

            func = getattr(cls, ext)

            return func(path)

        else:

            if cls._is(obj):

                ext = _File._get_ext(path)

                func = getattr(_File, ext)

                return func(path, obj)

            else:

                raise TypeError


class _String:

    @classmethod
    def _is(cls, obj):

        return isinstance(obj, str)


    @classmethod
    def ext_list(cls):

        return [
            "txt",
            "sql",
            "py",
            "html",
            "bat",
        ]


    @classmethod
    def read(cls, path):

        with open(path, "r") as f:

            return f.read()


    @classmethod
    def write(cls, path, string):

        with open(path, "w") as f:

            f.write(string)

        return path


    @classmethod
    def string(cls, path, str_obj=None):

        if str_obj is None:

            ext = _File._get_ext(path)

            import os

            if os.path.isfile(path):

                extensions = cls.ext_list()

                if ext in extensions:

                    return cls.read(path)

                else:

                    raise TypeError("path points to an unsupported file type. \".{}\"".format(ext))

            else:

                raise FileNotFoundError

        else:

            cls.write(path, string=str_obj)


class _File:

    @classmethod
    def _get_file_name(cls, path):

        return ".".join(path.split("\\")[-1].split(".")[:-1])


    @classmethod
    def _get_ext(cls, path):

        return path.split(".")[-1]


    @classmethod
    def csv(cls, path, df):

        df.to_csv(path, na_rep="null", index=False)

        return path


    @classmethod
    def xlsx(cls, path, df):

        file_name = _File._get_file_name(path)

        df.to_excel(path, index=False, sheet_name=file_name)

        return path


    @classmethod
    def json(cls, path, df):

        df.to_json(path)

        return path


    @classmethod
    def html(cls, path, obj):

        if _String._is(obj):

            with open(path, "w") as f:

                f.write(obj)

        elif _Df._is(obj):

            obj.to_html(path)

        else:

            raise TypeError("cannot convert {} type to html file"

                            .format(str(type(obj))))

        return path


    @classmethod
    def files(cls, read, write):

        if (_File._get_ext(read) == "html" and _File._get_ext(write) == "txt")\
            \
            or (_File._get_ext(read) == "txt" and _File._get_ext(write) == "html"):

            _String.string(write, _String.string(read))

        else:

            _Df.df(write, _Df.df(read))

        return write


get_file_name = _File._get_file_name

get_ext = _File._get_ext

df = _Df.df

string = _String.string

file = _File.files


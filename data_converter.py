import pandas
from path_container import Path

__all__ = [
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

            return pandas.read_excel(path, sheet_name=Path(path).name)

        except:

            return pandas.read_excel(path)


    @classmethod
    def json(cls, path):

        return pandas.read_json(path)


    @classmethod
    def df(cls, path, obj=None):

        ext = Path(path).ext

        if obj is None:

            func = getattr(cls, ext)

            return func(path)

        else:

            if cls._is(obj):

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

        ext = Path(path).ext

        if str_obj is None:

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
    def csv(cls, path, df):

        df.to_csv(path, na_rep="null", index=False)

        return path


    @classmethod
    def xlsx(cls, path, df):

        df.to_excel(path, index=False, sheet_name=Path(path).name)

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
    def files(cls, src, dest):

        src_ext = Path(src).ext

        dest_ext = Path(dest).ext

        if (src_ext == "html" and dest_ext == "txt")\
            \
            or (dest_ext == "txt" and dest_ext == "html"):

            _String.string(dest, _String.string(src))

        else:

            _Df.df(dest, _Df.df(src))

        return dest


df = _Df.df

string = _String.string

file = _File.files


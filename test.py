from rwa_funcs import *

EMPTIES = namedtuple("EMPTIES", [
    "str",
    "df",
])

Instruction = namedtuple("Instruction", [
    "src",
    "dest",
])

Empties = EMPTIES("", pandas.DataFrame())


class TestValues:

    @classmethod
    def _attr_generator(cls):

        for i in cls.__dict__:

            if i[0] != "_":

                yield i, cls.__dict__[i]

    @classmethod
    def _file_path_generator(cls):

        for i, j in cls._attr_generator():

            if str(i)[-3:] == "_ne":

                yield j

    @classmethod
    def _data_obj_generator(cls):

        for i, j in cls._attr_generator():

            if str(i)[:3] in ["str", "df_"]:

                yield j

    str_empty = Empties.str

    df_empty = Empties.df

    str_pop = "Hello. This is a string"

    df_pop = pandas.DataFrame([["A", "C", "E"], ["B", "D", "F"]], columns=["one", "two", "three"])

    csv_e = "{}\\exists.csv".format(here)

    csv_ne = "{}\\not_exist.csv".format(here)

    xlsx_e = "{}\\exists.xlsx".format(here)

    xlsx_ne = "{}\\not_exist.xlsx".format(here)

    json_e = "{}\\exists.json".format(here)

    json_ne = "{}\\not_exist.json".format(here)

    html_e = "{}\\exists.html".format(here)

    html_ne = "{}\\not_exist.html".format(here)

    txt_e = "{}\\exists.txt".format(here)

    txt_ne = "{}\\not_exist.txt".format(here)

    sql_e = "{}\\exists.sql".format(here)

    sql_ne = "{}\\not_exist.sql".format(here)

    py_e = "{}\\exists.py".format(here)

    py_ne = "{}\\not_exist.py".format(here)


def show_test_objects():

    x = TestValues._attr_generator()

    for i, j in x:

        print(i)
        print("--------")
        print(type(j))

def show_functions():

    for i in FileFunctions.__dict__:

        print(i)

def get_src_code_test():

    x = TestValues._attr_generator()

    pass_list = []

    fail_list = []

    for i, j in x:

        try:

            pass_list.append("{} passed. dest_code = {}".format(i, FileFunctions.get_src_code(j)))

        except:

            fail_list.append("{} failed.".format(i))

    for i in pass_list + fail_list:

        print(i)

def get_dest_code_test():

    x = TestValues._attr_generator()

    pass_list = []

    fail_list = []

    for i, j in x:

        try:

            pass_list.append("{} passed. dest_code = {}".format(i, FileFunctions.get_dest_code(j)))

        except:

            fail_list.append("{} failed.".format(i))

    for i in pass_list + fail_list:

        print(i)

def instruction_generator():

    instruction_list = []

    for i in TestValues._data_obj_generator():

        for j in TestValues._file_path_generator():

            instruction_list.append(Instruction(i, j))

    for i in TestValues._file_path_generator():

        for j in TestValues._data_obj_generator():

            instruction_list.append(Instruction(i, j))

    return instruction_list

def test_all_combinations():

    x = instruction_generator()

    for i in x:

        src = i.src

        dest = i.dest

        print(src)
        print(dest)

        print("-------")

        input("\n")

        try:

            FileFunctions.convert(src, dest)

        except:

            print("convert() failed with {} as src and {} as dest".format(src, dest))
            input("continue?")

        # try:
        #
        #     FileFunctions.append(src, dest)
        #
        # except:
        #
        #     print("append() failed with {} as src and {} as dest".format(src, dest))
        #     input("continue?")


# test_all_combinations()

src = TestValues.txt_ne

dest = TestValues.str_empty

print("testing")
print(src)
print(dest)
print("\n")

try:
    x = convert(src, dest)

    print(x)

except Exception as e:
    print(str(e))
    print("failed")


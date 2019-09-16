from collections import namedtuple
from data_converter import *

def command_parser(path):

    Command = namedtuple("Command", [
        "cmd",
        "param1",
        "param2",
        "script",
    ])

    split1 = string(path).split("--*-**-")

    return [

        Command(i, j, k, l) for i, j, k, l

            in string(path).split("--*-**-")

                .split("-**|")

            ]


import os
import sys
import pandas
from pprint import pprint as pp


here = os.path.dirname(os.path.realpath(__file__))
test_dir = "{}\\test".format(here)
sys.path.append(test_dir)


print("\nrunning data_converter tests:\n------------------\n")

import data_converter_test

data_converter_test._Test.run_all_tests()

print("\nrunning path_container tests:\n------------------\n")

import path_container_test

path_container_test.run_main_test(False)













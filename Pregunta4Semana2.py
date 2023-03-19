import sys

variable=sys.argv
def my_path_function(*args):
    print(type(args))

my_path_function(variable)

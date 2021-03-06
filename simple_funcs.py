import os

a_string = """

This is a multi line string

"""

VAR = 50  # A Variable

#####################

#### COMMENT #######

####################

def add(a, b: int=10):
    def check_if_even(num):
        return True if num % 2 == 0 else False
    return a * b


def check_even_numbers_in_a_list (base_list):
    return [a for a in base_list if a % 2 == 0]


def open_file(file_path):
    return open(file_path, "r")


def add_tensors (t, t1):
    return t + t1


def print_hello_greetings():
    print("Hello")


def echo_name(name):
    return f"Hello {name}"


# if __name__ == "__main__":
#     print(add(12, 12))


def area_rectangle(length, width):
    if length < 0 or width < 0:
        raise ValueError("only accepts non-negative values")
    return length * width

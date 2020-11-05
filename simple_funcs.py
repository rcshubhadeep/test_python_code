import os

a_string = """

This is a multi line string

"""

VAR = 50  # A Variable

#####################

#### COMMENT #######

####################

def add(a, b: int=10):
    """
    Return true if two numeric

    Args:
        a: (int): write your description
        b: (int): write your description
    """
    def check_if_even(num):
        """
        Checks if num is a number.

        Args:
            num: (int): write your description
        """
        return True if num % 2 == 0 else False
    return a * b


def check_even_numbers_in_a_list (base_list):
    """
    Check if a list is a list numbers.

    Args:
        base_list: (list): write your description
    """
    return [a for a in base_list if a % 2 == 0]


def open_file(file_path):
    """
    Open a file.

    Args:
        file_path: (str): write your description
    """
    return open(file_path, "r")


def add_tensors (t, t1):
    """
    R add_tensors

    Args:
        t: (todo): write your description
        t1: (todo): write your description
    """
    return t + t1


def print_hello_greetings():
    """
    Prints out the greetings

    Args:
    """
    print("Hello")


def echo_name(name):
    """
    Return the name of a user

    Args:
        name: (str): write your description
    """
    return f"Hello {name}"


# if __name__ == "__main__":
#     print(add(12, 12))


def area_rectangle(length, width):
    """
    Calculate area of the rectangle.

    Args:
        length: (int): write your description
        width: (int): write your description
    """
    if length < 0 or width < 0:
        raise ValueError("only accepts non-negative values")
    return length * width

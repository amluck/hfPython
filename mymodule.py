"""This is DocString
"""


def print_lo(list_item):
    """This function aimed at print the movies
    """
    for item in list_item:
        if isinstance(item, list):
            print_lo(item)
        else:
            print(item)

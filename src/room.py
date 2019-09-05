# Implement a class to hold room information. This should have name and
# description attributes.
from colors import colors


class Room():

    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        print_list = "\n".join([i.__str__() for i in self.items])

        return f'{colors.BOLD}{colors.YELLOW}{self.name}{colors.END}\n{colors.DARKCYAN}{self.description}{colors.END}\n{colors.RED}**Available Items: \n{print_list}{colors.END}'

    n_to = ''
    s_to = ''
    w_to = ''
    e_to = ''

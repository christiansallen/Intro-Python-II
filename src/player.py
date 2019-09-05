# Write a class to hold player information, e.g. what room they are in
# currently.
from colors import colors


class Player():

    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'{self.current_room}\n{colors.GREEN}Player Inventory: {self.inventory}{colors.END}'

    def move(self, d):
        if d == 'n' and self.current_room.n_to:
            self.current_room = self.current_room.n_to
            print(f'\nMoved to: {self.current_room}\n')

        elif d == 's' and self.current_room.s_to:
            self.current_room = self.current_room.s_to
            print(f'\nMoved to: {self.current_room}\n')

        elif d == 'w' and self.current_room.w_to:
            self.current_room = self.current_room.w_to
            print(f'\nMoved to: {self.current_room}\n')

        elif d == 'e' and self.current_room.e_to:
            self.current_room = self.current_room.e_to
            print(f'\nMoved to: {self.current_room}\n')

        else:
            print('\nThere are no rooms in that direction. Try again.')

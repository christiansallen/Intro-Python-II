from room import Room
from player import Player
from item import Item
from colors import colors

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('Shield', 'Not really a weapon'), Item('Armor', 'also not a weapon')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Sword', 'A sharp metal thing')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('Knife', 'A shorter metal thing')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('Knife', 'A shorter metal thing')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('Axe', 'Not that cool of a weapon')]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player('Bobby', room['outside'], [])
print(newPlayer)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
i = ''

while i is not 'q':
    i = input('\nEnter a command:')
    i = i.lower().strip().split()

    if(i == ['n']):
        newPlayer.move('n')
        print(
            f'{colors.GREEN}Current Player Inventory: {[weapon.name for weapon in newPlayer.inventory]}{colors.END}')
    elif(i == ['s']):
        newPlayer.move('s')
        print(
            f'{colors.GREEN}Current Player Inventory: {[weapon.name for weapon in newPlayer.inventory]}{colors.END}')
    elif(i == ['e']):
        newPlayer.move('e')
        print(
            f'{colors.GREEN}Current Player Inventory: {[weapon.name for weapon in newPlayer.inventory]}{colors.END}')
    elif(i == ['w']):
        newPlayer.move('w')
        print(
            f'{colors.GREEN}Current Player Inventory: {[weapon.name for weapon in newPlayer.inventory]}{colors.END}')

    # drop
    elif(i[0] == 'drop'):
        try:
            i[1]
        except IndexError:
            print('Tell me what to drop.')
        else:
            found = False
            for weapon in newPlayer.inventory:
                if (weapon.name.lower() == i[1]):
                    found = True
                    index = newPlayer.inventory.index(weapon)
                    newPlayer.current_room.items.append(
                        newPlayer.inventory.pop(index))
                    print(
                        f'{colors.RED}**Available Items: {[item.name for item in newPlayer.current_room.items]}{colors.END}')
                    print(
                        f'{colors.GREEN}Current Player Inventory: {[weapon.name for weapon in newPlayer.inventory]}{colors.END}')

                if (found == False):
                    print('You dont have that item in your inventory')
    # take
    elif(i[0] == 'take'):
        try:
            i[1]
        except IndexError:
            print('***Tell me what to take.')
        else:
            found = False
            for item in newPlayer.current_room.items:

                if (item.name.lower() == i[1]):
                    found = True
                    index = newPlayer.current_room.items.index(item)
                    newPlayer.inventory.append(
                        newPlayer.current_room.items.pop(index))
                    print(
                        f'{colors.RED}**Available Items: {[item.name for item in newPlayer.current_room.items]}{colors.END}')
                    print(
                        f'{colors.GREEN}Current Player Inventory: {[weapon.name for weapon in newPlayer.inventory]}{colors.END}')

                if (found == False):
                    print('***That item isnt in this room')

    # quit
    elif(i == 'q'):
        print('bye bye quitter')

    else:
        print(f'\nTake (item)\nDrop (inventory)\n(N)orth\n(S)outh\n(E)ast\n(W)est\n(Q)uit')

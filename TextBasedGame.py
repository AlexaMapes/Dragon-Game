# Alexa Mapes

# Room information dictionary
rooms = {
    'Cave Entrance': {
        'East': 'Main Cavern',
        'Item': 'None'
    },
    'Main Cavern': {
        'West': 'Cave Entrance',
        'South': 'Dusty Crypt',
        'North': 'Underground River',
        'East': 'Lava Lake',
        'Item': 'Stalagmite'
    },
    'Underground River': {
        'East': 'Crystal Cavern',
        'South': 'Main Cavern',
        'Item': 'Water'
    },
    'Crystal Cavern': {
        'West': 'Underground River',
        'Item': 'Crystal'
    },
    'Dusty Crypt': {
        'North': 'Main Cavern',
        'East': 'Forgotten Tomb',
        'Item': 'Shield'
    },
    'Forgotten Tomb': {
        'West': 'Dusty Crypt',
        'Item': 'Sword'
    },
    'Lava Lake': {
        'West': 'Main Cavern',
        'North': 'Dragon Lair',
        'Item': 'Berries'
    },
    'Dragon Lair': {
        'South': 'Lava Lake',
        'Item': 'Dragon'
    }
}

# Print the various commands
print('Dragon Text Adventure Game\nCollect all the items to defeat the dragon!\n'
      'Move commands: go South, go North, go East, go West, Exit\n'
      'Add item to inventory: get "item name"\n----------------------------\n')

# Set current room and blank inventory
currentRoom = 'Cave Entrance'
inventory = []

# Loop forever
while True:
    currentRoomInfo = rooms[currentRoom]
    # Main menu prints current room, room item, and current inventory
    mainMenu = 'You are in the {}\nRoom Item: {}\nCurrent Inventory: {}\n' \
               'Enter your move:'.format(currentRoom, currentRoomInfo['Item'], inventory)
    print(mainMenu)
    # Checks if player is in the Dragon Lair
    if currentRoomInfo['Item'] == 'Dragon':
        # Checks for full inventory
        if len(inventory) == 6:
            print('You collected all the items and defeated the dragon!\nYou won!')
            break
        else:
            print('You were not prepared for the dragon!\nYou lost!')
            break
    user_input = input('>').strip().title().split()
    # Checks for exit command
    if user_input[0] == 'Exit':
        print('Thanks for playing!')
        break
    # Checks the input command
    elif user_input[0] == 'Go':
        # If user only enters "go"
        if len(user_input) == 1:
            print('No direction entered!')
            print('----------------------------\n')
        # Move rooms
        elif user_input[1] in currentRoomInfo:
            currentRoom = currentRoomInfo[user_input[1]]
            print('----------------------------\n')
        # Invalid direction, print error message
        else:
            print('Can\'t go that way!')
            print('----------------------------\n')
    elif user_input[0] == 'Get':
        # If user only inputs "get"
        if len(user_input) == 1:
            print('No item entered!')
            print('----------------------------\n')
        # Prevents user from adding "None" item from Cave Entrance to inventory
        elif user_input[1] == 'None':
            print('Invalid action!')
            print('----------------------------\n')
        # User already has the item, print error message
        elif user_input[1] in inventory:
            print('You already have that item!')
            print('----------------------------\n')
        # Add item to inventory
        elif user_input[1] in currentRoomInfo['Item']:
            inventory.append(user_input[1])
            print('Added {} to inventory!'.format(user_input[1]))
            print('----------------------------\n')
        # Invalid item entered
        else:
            print('Can\'t get that item!')
            print('----------------------------\n')
    # User enters an invalid command
    else:
        print('Invalid action!')
        print('----------------------------\n')

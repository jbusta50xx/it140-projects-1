"""A simplified dragon text game with room movement and an exit command."""

rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}


def main():
    """Prompt for commands until the player enters the exit room."""
    current_room = 'Great Hall'
    directions = ('north', 'south', 'east', 'west')

    print('Welcome to the simplified dragon text game!')
    print('Enter go north, go south, go east, go west, or exit.')

    while current_room != 'exit':
        print(f'\nYou are in the {current_room}.')
        print('Available directions: ' + ', '.join(rooms[current_room]))
        command = input('Enter your command: ').strip().lower().split()

        if command == ['exit']:
            current_room = 'exit'
        elif len(command) == 2 and command[0] == 'go':
            direction = command[1]

            if direction not in directions:
                print('Invalid direction. Use north, south, east, or west.')
            elif direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print('You cannot go that way from this room.')
        else:
            print('Invalid command. Enter go followed by a direction, or exit.')

    print('Thanks for playing!')


if __name__ == '__main__':
    main()

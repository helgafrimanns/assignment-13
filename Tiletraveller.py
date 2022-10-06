from typing import Tuple


# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)


def main():
    counter = 0
    location = STARTING_LOCATION
    while location == FINAL_DESTINATION:
        play()
        again = input("Play again (y/n): ")

        
        



def play_one_move(location: Tuple[int],counter) -> Tuple[int]:
    """Plays one move of the game.

    Returns updated location.
    """

    valid_directions = find_directions(location)
    direction = get_direction(valid_directions)

    if direction in valid_directions:
        location = move(direction, location)
        counter = pull_lever(location,counter)
    else:
        print("Not a valid direction!")

    return location,counter


def find_directions(location: Tuple[int]) -> Tuple[str]:
    """Returns valid directions as a string given the supplied location."""

    if location == (1, 1):
        valid_directions = (NORTH,)
    elif location == (1, 2):
        valid_directions = NORTH, EAST, SOUTH
    elif location == (1, 3):
        valid_directions = EAST, SOUTH
    elif location == (2, 1):
        valid_directions = (NORTH,)
    elif location == (2, 2):
        valid_directions = SOUTH, WEST
    elif location == (2, 3):
        valid_directions = EAST, WEST
    elif location == (3, 2):
        valid_directions = NORTH, SOUTH
    elif location == (3, 3):
        valid_directions = SOUTH, WEST

    return valid_directions


def get_direction(valid_directions: Tuple[str]) -> str:
    print_directions(valid_directions)
    return input("Direction: ").lower()


def print_directions(available_directions: Tuple[str]) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def move(direction: str, location: Tuple[int]) -> Tuple[int]:
    """Returns updated location given the direction."""

    x, y = location

    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == EAST:
        x += 1
    elif direction == WEST:
        x -= 1

    return x, y

def pull_lever(location, counter):
    if location == (1,2) or location == (2,2) or location == (2,3) or location == (3,2) :
        x = input("Pull a lever (y/n): ")
        if x == "y":
            counter += 1
            print(f"You received 1 coin, your total is now {counter}.")
        
    return counter
    
def play(location):
    counter = 0
    while location != FINAL_DESTINATION:
        location, counter = play_one_move(location,counter)
        valid_directions = find_directions(location)
        print(valid_directions)
        play_one_move(location, counter)


    print(f"Victory! Total coins {counter}.")

    

            

if __name__ == "__main__":
    main()

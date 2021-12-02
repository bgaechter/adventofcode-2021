from typing import List

def read_input() -> List[str]:
    with open("input.txt") as f:
        return f.readlines()

def get_final_position(input: List[str]) -> int:
    position = {'horizontal': 0, 'depth': 0}
    for line in input:
        command = line.split(' ')
        if command[0] == "up":
            position['depth'] -= int(command[1])
        elif command[0] == "down":
            position['depth'] += int(command[1])
        elif command[0] == "forward":
            position['horizontal'] += int(command[1])
        else:
            print("Unknown command")

    return position['horizontal'] * position['depth']

def get_final_position_aim(input: List[str]) -> int:
    position = {'horizontal': 0, 'depth': 0, 'aim': 0}
    for line in input:
        command = line.split(' ')
        if command[0] == "up":
            position['aim'] -= int(command[1])
        elif command[0] == "down":
            position['aim'] += int(command[1])
        elif command[0] == "forward":
            position['horizontal'] += int(command[1])
            position['depth'] += position['aim'] * int(command[1])
        else:
            print("Unknown command")
    return position['horizontal'] * position['depth']


if __name__ == "__main__":
    input = read_input()
    print(get_final_position(input))
    print(get_final_position_aim(input))

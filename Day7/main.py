from typing import List

def read_input() -> List[str]:
    with open("/workspaces/adventofcode-2021/Day7/input.txt") as f:
        return f.readlines()

def part_one(position_list: List[int]) -> int:
    position_list.sort()
    fuel_usage = []
    for position in position_list:
        fuel_usage.append(sum([ abs(pos-position) for pos in position_list]))
    return min(fuel_usage)

def calculate_fuel_consumption(distance: int) -> int:
    return distance * (distance+1) // 2

def part_two(position_list: List[int]) -> int:
    position_list.sort()
    fuel_usage = []
    for position in position_list:
        fuel_usage.append(sum([calculate_fuel_consumption(abs(pos-position)) for pos in position_list]))
    return min(fuel_usage)

if __name__ == "__main__":
    input = read_input()
    position_list = list(map(int, input[0].split(",")))
    print(part_one(position_list))
    print(part_two(position_list))

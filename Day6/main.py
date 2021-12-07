from typing import List

def read_input() -> List[str]:
    with open("/workspaces/adventofcode-2021/Day6/input.txt") as f:
        return f.readlines()

def part_one(input_fish: List[int], days: int) -> int:
    fish = [0 for _ in range(9)]
    for f in input_fish:
        fish[f] += 1

    for _ in range(days):
        new_fish = [0 for _ in range(9)]
        for day, count in enumerate(fish):
            if day == 0:
                new_fish[6] += count
                new_fish[8] += count

            else:
                new_fish[day-1] += count

        fish = new_fish

    return sum(fish)
        
    

if __name__ == "__main__":
    input = read_input()
    fish_list = list(map(int, input[0].split(",")))
    print(part_one(fish_list, 80))
    print(part_one(fish_list, 256))

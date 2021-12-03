from typing import List

def read_input() -> List[str]:
    with open("input.txt") as f:
        return f.readlines()

def convert_list_elements_int (string_list: List[str]) -> List[int]:
    return list(map(int, string_list))

def get_rates(report: List[str]) -> int:
    positions = [0 for i in range(len(report[0]))]
    most_common_bits = ""
    for line in report:
        for i,pos in enumerate(line):
            if pos == "0":
                positions[i] -= 1
            if pos == "1":
                positions[i] += 1

    for num in positions:
        if num > 0:
            most_common_bits += "1"
        if num < 0:
            most_common_bits += "0"
        else:
            print("even number of 0 and 1")

    most_common_bits = int(most_common_bits, 2)
    bitmask = 4095
    least_common_bits = most_common_bits ^ bitmask

    return most_common_bits * least_common_bits

def get_oxygen_rating(report: List[str], position: int, filter: str) -> str:
    if len(report) == 1:
        return report[0]

    most_common_bit = 0
    for line in report:
        if line[position] == "0":
            most_common_bit -= 1
        if line[position] == "1":
            most_common_bit += 1

    if most_common_bit > 0:
        filter += "1"
    elif most_common_bit < 0:
        filter += "0"
    else:
        filter += "1"
    return get_oxygen_rating([rating for rating in report if rating.startswith(filter)], position+1, filter)

def get_life_support_rating(report: List[str], position: int, filter: str) -> str:
    if len(report) == 1:
        return report[0]

    most_common_bit = 0
    for line in report:
        if line[position] == "0":
            most_common_bit -= 1
        if line[position] == "1":
            most_common_bit += 1
    # Looking for least common bit so just inverse msb
    if most_common_bit > 0:
        filter += "0"
    elif most_common_bit < 0:
        filter += "1"
    else:
        filter += "0"
    return get_life_support_rating([rating for rating in report if rating.startswith(filter)], position+1, filter)


if __name__ == "__main__":
    input = read_input()
    print(get_rates(input))
    oxygen_rating = get_oxygen_rating(input, 0, "")
    life_support_rating = get_life_support_rating(input, 0, "")
    
    print(int(oxygen_rating,2)* int(life_support_rating,2))

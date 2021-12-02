from typing import List

def read_input() -> List[str]:
    with open("input.txt") as f:
        return f.readlines()

def count_depth_increase(measurements: List[str]) -> int:
    counter = 1
    for i,measurement in enumerate(measurements):
        if i != 0:
            if measurement > measurements[i-1]:
                counter += 1
    return counter

def convert_list_elements_int (string_list: List[str]) -> List[int]:
    return list(map(int, string_list))

def count_depth_increase_window(measurements: List[str]) -> int:
    counter = 1
    for i,_ in enumerate(measurements):
        if i != 0 and i+3 < len(measurements):
            if sum(convert_list_elements_int(measurements[i:i+3])) > sum(convert_list_elements_int(measurements[i-1:i+2])):
                counter += 1
    return counter

 
if __name__ == "__main__":
    input = read_input()
    print(count_depth_increase(input))
    print(count_depth_increase_window(input))

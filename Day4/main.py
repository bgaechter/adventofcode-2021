from typing import List

class BingoBoard:

    def __init__(self, lines: List[str]):
        self.rows = []
        self. cols = []
        int_lines = []
        for line in lines:
            int_lines.append(self.line_to_int_list(line))

        for line in int_lines:
            self.rows.append(line)

        for i in range(5):
            col = []
            for j in range(5):
                col.append(int_lines[j][i])
            self.cols.append(col)

    def line_to_int_list(self, line: str) -> List[int]:
        line = line.replace('  ', ' ') # remove double space
        line = line.strip()
        return list(map(int, line.split(' ')))

    def sum_of_unmarked(self, marked_numbers: List[int]) -> int:
        unmarked_numbers = []
        for row in self.rows:
            unmarked_numbers += list(set(row) - set(marked_numbers))
        for col in self.cols:
            unmarked_numbers += list(set(col) - set(marked_numbers))
        print(f"unmarked numbers are {set(unmarked_numbers)}")
        return sum(set(unmarked_numbers))

    def has_bingo(self, numbers: List[int]) -> bool:
        for col in self.cols:
            if set(col).issubset(set(numbers)):
                print(f"Column bingo {col}")
                return True
            # if(all(x in numbers for x in col)):
            #     print(f"Column bingo {col}")
            #     return True
        for row in self.rows:
            if set(row).issubset(set(numbers)):
                print(f"Row bingo {col}")
                return True
            # if(all(x in numbers for x in row)):
            #     print(f"Row bingo {row}")
            #     return True
        return False

def read_input() -> List[str]:
    with open("/workspaces/adventofcode-2021/Day4/input.txt") as f:
        return f.readlines()

def convert_list_elements_int (string_list: List[str]) -> List[int]:
    return list(map(int, string_list))

def part_one() -> int:
    input = read_input()
    numbers = convert_list_elements_int(input[0].split(','))
    bingo_boards = []
    board_numbers = []
    for i in range(2,len(input)):
        if input[i] == '\n':
            bingo_boards.append(BingoBoard(board_numbers))
            board_numbers = []
        else:
            board_numbers.append(input[i])

    for i in range(len(numbers)):
        for board in bingo_boards:
            print(f"calling number {numbers[i]}")
            if board.has_bingo(numbers[:i]):
                print("BINGO")
                return numbers[i] * board.sum_of_unmarked(numbers[:i])

def part_two() -> int:
    last_score = 0
    input = read_input()
    numbers = convert_list_elements_int(input[0].split(','))
    bingo_boards = []
    board_numbers = []
    for i in range(2,len(input)):
        if input[i] == '\n':
            bingo_boards.append(BingoBoard(board_numbers))
            board_numbers = []
        else:
            board_numbers.append(input[i])

    for i in range(len(numbers)):
        print(f"calling number {numbers[i]}")
        print(f"makred numbers are {numbers[:i]}")
        for board in bingo_boards:
            if board.has_bingo(numbers[:i]):
                print(f"BINGO with {numbers[i]}")
                last_score = numbers[i] * board.sum_of_unmarked(numbers[:i])
    return last_score


if __name__ == "__main__":
    #print(part_one())
    print(part_two())
from typing import List

def read_input() -> List[str]:
    with open("/workspaces/adventofcode-2021/Day5/input.txt") as f:
        return f.readlines()

def diag(a,b):
    return abs(a[0] - b[0]) == abs(a[1] - b[1])

def part_one(lines: List[str], solve_diag: bool) -> int:
    map = [ [0] * 1000 for i in range(1000) ]
    for line in lines:
        points = line.split('->')
        x1 = int(points[0].strip().split(',')[0])
        y1 = int(points[0].strip().split(',')[1])
        x2 = int(points[1].strip().split(',')[0])
        y2 = int(points[1].strip().split(',')[1])

        if x1 == x2:
            for i in range(min(y1,y2), max(y1,y2)+1):
                map[x1][i] += 1
        elif y1 == y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                map[i][y1] += 1
        else:
            print(f"Not a horizontal line {line}")
            if solve_diag:
                diagonal_points = [i for i in zip(range(x1, y1+1-2*int(x1>y1), -1+2*int(x1<y1)),
                               range(x2, y2+1-2*int(x2>y2), -1+2*int(x2<y2)))]
                for point in diagonal_points:
                    map[point[1]][point[0]] += 1

    count = 0
    for row in map:
        count += len([x for x in row if x > 1])
    return count
    

if __name__ == "__main__":
    lines = read_input()
    print(part_one(lines, False))
    print(part_one(lines, True))


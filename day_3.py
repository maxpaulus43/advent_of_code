import re
from collections import defaultdict

def parse_line(line):
    return map(int, re.findall(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)[0])

def get_overlaps(file):
    size = 1000
    overlaps = 0
    board = [[0 for _ in range(size)] for _ in range(size)]

    for line in file:
        _, row, col, width, height = parse_line(line)

        for i in range(row, row + width):
            for j in range(col, col + height):
                board[i][j] += 1
                if board[i][j] == 2:
                    overlaps += 1

    return overlaps

def get_free_square(file):
    board = defaultdict(set)
    valid_ids = set()

    for line in file:
        id, row, col, width, height = parse_line(line)
        valid_ids.add(id)
        for i in range(row, row + width):
            for j in range(col, col + height):
                board[(i, j)].add(id)

    for _, id_hits in board.items():
        if len(id_hits) > 1:
            valid_ids -= id_hits

    return valid_ids.pop()

if __name__ == "__main__":
    with open("input/day_3.txt") as f:
        # print(get_overlaps(f))
        print(get_free_square(f))
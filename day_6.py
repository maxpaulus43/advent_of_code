import time

def find_closest_coord(coords, point_of_interest):
    min_distance = 2**16
    closest_coord = None

    for c in coords:
        distance = abs(c[0] - point_of_interest[0]) + abs(c[1] - point_of_interest[1])

        if distance < min_distance:
            min_distance = distance
            closest_coord = c
        elif distance == min_distance:
            closest_coord = None # if the point of interest is equidistant from 2 coords

    return closest_coord


def find_sum_distance(coords, point_of_interest):
    sum = 0
    for c in coords:
        sum += abs(c[0] - point_of_interest[0]) + abs(c[1] - point_of_interest[1])
    return sum


def process_islands(file):
    # parse lines into coordinates
    coords = list(map(lambda line : tuple(map(int, line.split(","))), file))
    to_x_coord = lambda xy : xy[0]
    to_y_coord = lambda xy : xy[1]
    min_x = min(map(to_x_coord, coords)) # find minimum x coord
    min_y = min(map(to_y_coord, coords)) # find min y coord
    # find the tightest box you can wrap around these coordinates
    coords = list(map(lambda xy : (xy[0] - min_x, xy[1] - min_y), coords))
    right_most_edge = max(map(to_x_coord, coords))
    bottom_most_edge = max(map(to_y_coord, coords))

    # part 1: keep track of the danger area for each coordinate
    danger_area = {coord:0 for coord in coords}
    # part 2: safe area size
    safe_area_size = 0

    for i in range(right_most_edge + 1):
        for j in range(bottom_most_edge + 1):
            closest_coord = find_closest_coord(coords, (i, j))
            if closest_coord:
                danger_area[closest_coord] += 1

            if find_sum_distance(coords, (i, j)) < 10000:
                safe_area_size += 1

    is_non_edge = lambda c : 0 > c[0][0] < right_most_edge and 0 < c[0][1] < bottom_most_edge
    coords = filter(is_non_edge, danger_area) # filter the edge coordinates because those have infinite area

    return max(danger_area.values()), safe_area_size

if __name__ == "__main__":
    with open("input/day_6.txt") as f:
        start = time.time()
        max_danger_area, safe_area = process_islands(f)
        print(max_danger_area)
        print(safe_area)
        print(time.time() - start)

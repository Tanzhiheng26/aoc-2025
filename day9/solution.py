import heapq

def read_input(file):
    red_tiles = []
    
    with open(file, "r") as f:    
        for line in f:
            c, r = map(int, line.strip().split(','))
            red_tiles.append((r, c))
          
    return red_tiles

def part1(input_file):
    red_tiles = read_input(input_file)
    num_red_tiles = len(red_tiles)
    max_area = 0

    for i in range(num_red_tiles):
        for j in range(i + 1, num_red_tiles):
            r1, c1 = red_tiles[i]
            r2, c2 = red_tiles[j]
            area = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
            max_area = max(area, max_area)

    return max_area

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def part2(input_file):
    red_tiles = read_input(input_file)
    num_red_tiles = len(red_tiles)
    
    max_r = 0
    max_c = 0
    for r, c in red_tiles:
        max_r = max(r, max_r)
        max_c = max(c, max_c)

    grid = [['.'] * (max_c + 1) for _ in range(max_r + 1)]

    # Mark edges
    for i in range(num_red_tiles):
        r1, c1 = red_tiles[i]
        grid[r1][c1] = '#'
        r2, c2 = red_tiles[(i + 1) % num_red_tiles]

        if r1 == r2:
            for c in range(min(c1, c2) + 1, max(c1, c2)):
                grid[r1][c] = 'X'
        elif c1 == c2:
            for r in range(min(r1, r2) + 1, max(r1, r2)):
                grid[r][c1] = 'X'
    
    # Mark tiles inside the loop
    for r in range(max_r + 1):
        c1 = 0
        c2 = 0
        for c in range(max_c + 1):
            if grid[r][c] in ['#', 'X']:
                if c1 == 0:
                    c1 = c
                c2 = c
        
        for c in range(c1 + 1, c2):
            if grid[r][c] == '.':
                grid[r][c] = 'X'
    
    max_heap = []
    for i in range(num_red_tiles):
        for j in range(i + 1, num_red_tiles):
            r1, c1 = red_tiles[i]
            r2, c2 = red_tiles[j]
            area = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
            max_heap.append((-area, i, j))
    heapq.heapify(max_heap)

    # Start from the rectangle with the biggest potential area
    while len(max_heap) > 0:
        neg_area, i, j = heapq.heappop(max_heap)
        r1, c1 = red_tiles[i]
        r2, c2 = red_tiles[j]
        is_valid = True
        for r in range(min(r1, r2), max(r1, r2) + 1):
            for c in range(min(c1, c2), max(c1, c2) + 1):
                if grid[r][c] == '.':
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            return -neg_area

print(part1("input.txt"))
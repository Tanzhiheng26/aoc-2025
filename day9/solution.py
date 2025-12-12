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

# Using coordinate compression idea from https://www.reddit.com/r/adventofcode/comments/1pibab2/comment/nt4t2bg/
def part2(input_file):
    red_tiles = read_input(input_file)
    num_red_tiles = len(red_tiles)
    
    r_values = set()
    c_values = set()
    for r, c in red_tiles:
        r_values.add(r)
        c_values.add(c)
    
    sorted_r_values = sorted(r_values)
    sorted_c_values = sorted(c_values)
    r_map = {} 
    c_map = {}

    next_i = 0
    for i, r in enumerate(sorted_r_values):
        r_map[r] = next_i
        next_i += 1
        if i < len(sorted_r_values) - 1 and sorted_r_values[i + 1] > r + 1:
            # Compress the [r + 1, sorted_r_values[i + 1]) range to 1 value
            next_i += 1
    num_r = next_i # Number of compressed r values

    next_i = 0
    for i, c in enumerate(sorted_c_values):
        c_map[c] = next_i
        next_i += 1
        if i < len(sorted_c_values) - 1 and sorted_c_values[i + 1] > c + 1:
            next_i += 1
    num_c = next_i

    red_tiles_compressed = []
    for i in range(num_red_tiles):
        r, c = red_tiles[i]
        red_tiles_compressed.append((r_map[r], c_map[c]))

    grid = [['.'] * num_c for _ in range(num_r)]

    # Add edges
    for i in range(num_red_tiles):
        r1, c1 = red_tiles_compressed[i]
        grid[r1][c1] = '#'
        r2, c2 = red_tiles_compressed[(i + 1) % num_red_tiles]

        if r1 == r2:
            for c in range(min(c1, c2) + 1, max(c1, c2)):
                grid[r1][c] = 'X'
        elif c1 == c2:
            for r in range(min(r1, r2) + 1, max(r1, r2)):
                grid[r][c1] = 'X'
    
    # Add tiles inside the loop
    for r in range(num_r):
        c1 = -1
        c2 = -1
        for c in range(num_c):
            if grid[r][c] in ['X', '#']:
                if c1 == -1:
                    c1 = c
                c2 = c
        
        for c in range(c1 + 1, c2):
            if grid[r][c] == '.':
                grid[r][c] = 'X'
    # print_grid(grid)

    max_area = 0
    for i in range(num_red_tiles):
        for j in range(i + 1, num_red_tiles):
            r1, c1 = red_tiles[i]
            r2, c2 = red_tiles[j]
            area = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
            if area <= max_area:
                continue

            r1, c1 = red_tiles_compressed[i]
            r2, c2 = red_tiles_compressed[j]
            is_valid = True
            for r in range(min(r1, r2), max(r1, r2) + 1):
                for c in range(min(c1, c2), max(c1, c2) + 1):
                    if grid[r][c] == '.':
                        is_valid = False
                        break
                if not is_valid:
                    break
            if is_valid:
                max_area = max(area, max_area)
    
    return max_area

print(part1("input.txt"))
print(part2("input.txt"))
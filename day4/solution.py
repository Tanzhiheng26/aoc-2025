def read_input(file):
    grid = []
    
    with open(file, "r") as f:    
        for line in f:
            row = list(line.strip())
            grid.append(row)
          
    return grid

def part1(input_file):
    grid = read_input(input_file)
    num_rows = len(grid)
    num_cols = len(grid[0])
    accessible_rolls = 0

    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == '@':
                adj_rolls = 0
                for i in range(max(r - 1, 0), min(r + 1, num_rows - 1) + 1):
                    for j in range(max(c - 1, 0), min(c + 1, num_cols - 1) + 1):
                        if not (i == r and j == c) and grid[i][j] == '@':
                            adj_rolls += 1
                if adj_rolls < 4:
                    accessible_rolls += 1
    
    return accessible_rolls

def part2(input_file):
    grid = read_input(input_file)
    num_rows = len(grid)
    num_cols = len(grid[0])
    accessible_rolls = 0

    while True:
        can_remove = False
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '@':
                    adj_rolls = 0
                    for i in range(max(r - 1, 0), min(r + 1, num_rows - 1) + 1):
                        for j in range(max(c - 1, 0), min(c + 1, num_cols - 1) + 1):
                            if not (i == r and j == c) and grid[i][j] == '@':
                                adj_rolls += 1
                    if adj_rolls < 4:
                        can_remove = True
                        grid[r][c] = 'x'
                        accessible_rolls += 1
        if not can_remove:
            break
    
    return accessible_rolls

print(part1("input.txt"))
print(part2("input.txt"))
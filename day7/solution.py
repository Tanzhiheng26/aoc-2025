def read_input(file):
    grid = []
    
    with open(file, "r") as f:    
        for line in f:
            row = list(line.strip())
            grid.append(row)
          
    return grid

def part1(input_file):
    grid = read_input(input_file)
    num_rows, num_cols = len(grid), len(grid[0])
    start_col = grid[0].index('S')
    beam_cols = {start_col}
    split = 0

    for r in range(1, num_rows):
        for c in range(num_cols):
            if grid[r][c] == '^':
                if c in beam_cols:
                    beam_cols.remove(c)
                    beam_cols.add(c - 1)
                    beam_cols.add(c + 1)
                    split += 1

    return split

def part2(input_file):
    grid = read_input(input_file)
    num_rows = len(grid)
    start_col = grid[0].index('S')
    memo = {}

    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        
        if r == num_rows - 1:
            return 1
        
        if grid[r + 1][c] == '.':
            return dfs(r + 1, c)
        
        if grid[r + 1][c] == '^':
            left = dfs(r + 1, c - 1)
            right = dfs(r + 1, c + 1)
            result = left + right
            memo[(r, c)] = result
            return result

    return dfs(0, start_col)
 
print(part1("input.txt"))
print(part2("input.txt"))
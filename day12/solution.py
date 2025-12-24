def read_input(file):
    with open(file, "r") as f:    
        split_input = f.read().split('\n\n')
        
        shapes = split_input[:-1]
        for i, shape in enumerate(shapes):
            rows = shape.split()[1:]
            shapes[i] = rows

        regions = split_input[-1].split('\n')
        for i, line in enumerate(regions):
            split_line = line.split()
            width, length = map(int, split_line[0][:-1].split('x'))
            num_shapes = list(map(int, split_line[1:]))
            regions[i] = (width, length, num_shapes)

        return shapes, regions

# Based on https://www.reddit.com/r/adventofcode/comments/1pkjynl/comment/ntlq9n3/
def part1(input_file):
    shapes, regions = read_input(input_file)

    num_units = {}
    for i, shape in enumerate(shapes):
        units = 0
        for r in range(3):
            for c in range(3):
                if shape[r][c] == '#':
                    units += 1
        num_units[i] = units

    can_fit = 0
    cannot_fit = 0
    indeterminate = 0

    for width, length, num_shapes in regions:
        total_shapes = sum(num_shapes)
        # Assume every present is a 3x3 square
        if (width // 3) * (length // 3) >= total_shapes:
            can_fit += 1
        # Assume every present can be any shape
        else:
            total_units = 0
            for i, num in enumerate(num_shapes):
                total_units += num * num_units[i]
                
            if (width * length) < total_units:
                cannot_fit += 1
            else:
                indeterminate += 1
    
    return can_fit, cannot_fit, indeterminate

print(part1("input.txt"))
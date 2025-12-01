START = 50
TOTAL_NUMBERS = 100

def read_input(file):
    rotations = []
    
    with open(file, "r") as f:    
        for line in f:
            rotation = line.strip()
            direction = rotation[0]
            distance = int(rotation[1:])
            rotations.append(distance if direction == 'R' else -distance)
            
    return rotations

def part1(input_file):
    rotations = read_input(input_file)
    number = START
    zeros = 0

    for rotation in rotations:
        number = (number + rotation) % TOTAL_NUMBERS
        if number == 0:
            zeros += 1
    
    return zeros

def part2(input_file):
    rotations = read_input(input_file)
    number = START
    zeros = 0

    for rotation in rotations:
        distance = abs(rotation)
        complete_rounds = distance // TOTAL_NUMBERS
        zeros += complete_rounds

        if number != 0:
            distance_to_zero = (TOTAL_NUMBERS - number) if rotation > 0 else number
            offset = distance % TOTAL_NUMBERS
            if offset >= distance_to_zero:
                zeros += 1
    
        number = (number + rotation) % TOTAL_NUMBERS

    return zeros

print(part1("input.txt"))
print(part2("input.txt"))
def read_input(file):
    id_ranges = []
    
    with open(file, "r") as f:    
        for id_range in f.read().split(','):
            start, end = map(int, id_range.split('-'))
            id_ranges.append((start, end))
            
    return id_ranges

def part1(input_file):
    id_ranges = read_input(input_file)
    invalid_sum = 0
    for start, end in id_ranges:
        for num in range(start, end + 1):
            num_str = str(num)
            if len(num_str) % 2 == 1:
                continue
            mid = len(num_str) // 2
            if num_str[:mid] == num_str[mid:]:
                 invalid_sum += num
    return invalid_sum

def is_invalid(num):
    num_str = str(num)
    digits = len(num_str)
    for seq_len in range (1, digits // 2 + 1):
        if digits % seq_len != 0:
            continue
        first_seq = num_str[:seq_len]
        has_mismatch = False
        for i in range(seq_len, digits, seq_len):
            if num_str[i:i + seq_len] != first_seq:
                has_mismatch = True
                break
        if not has_mismatch:
            return True
    return False

def part2(input_file):
    id_ranges = read_input(input_file)
    invalid_sum = 0
    for start, end in id_ranges:
        for num in range(start, end + 1):
            if is_invalid(num):
                invalid_sum += num
      
    return invalid_sum

print(part1("input.txt"))
print(part2("input.txt"))
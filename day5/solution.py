def read_input(file):
    fresh_ranges = []
    available = []
    
    with open(file, "r") as f:
        is_range = True
        for line in f:
            if line == '\n':
                is_range = False
                continue
            
            if is_range:
                start, end = map(int, line.strip().split('-'))
                fresh_ranges.append((start, end))
            else:
                available.append(int(line.strip()))

    return fresh_ranges, available

def part1(input_file):
    fresh_ranges, available = read_input(input_file)
    fresh_count = 0

    for id in available:
        is_fresh = False
        for start, end in fresh_ranges:
            if start <= id <= end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1
    
    return fresh_count

# Based on solution to https://leetcode.com/problems/merge-intervals/description/
def part2(input_file):
    fresh_ranges, _ = read_input(input_file)
    # Sort by start ID
    fresh_ranges.sort(key=lambda x: x[0])
    non_overlapping_ranges = []

    for start, end in fresh_ranges:
        if len(non_overlapping_ranges) == 0 or start > non_overlapping_ranges[-1][1]:
            non_overlapping_ranges.append([start, end])
        else:
            non_overlapping_ranges[-1][1] = max(end, non_overlapping_ranges[-1][1]) 
    
    fresh_ids = 0
    for start, end in non_overlapping_ranges:
        fresh_ids += (end - start + 1)
    
    return fresh_ids
                            
print(part1("input.txt"))           
print(part2("input.txt"))
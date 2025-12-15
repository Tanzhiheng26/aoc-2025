from collections import deque
from z3 import *

# Eg. [...#.] (0,2,3,4) 
# [...#.] -> reverse 00010 -> 01000 -> 8
# (0,2,3,4) -> 11101 -> 29
def read_input(file):
    machines = []
    
    with open(file, "r") as f:    
        for line in f:
            manual = line.strip().split()
            target = int(''.join('1' if e == '#' else '0' for e in manual[0][1:-1][::-1]), 2)
            buttons = []
            for button in manual[1:-1]:
                num = 0
                for i in map(int, button[1:-1].split(',')):
                    num += 2 ** i
                buttons.append(num)
            counters = list(map(int, manual[-1][1:-1].split(',')))
            machines.append((target, buttons, counters))    
    
    return machines

def bfs(target, buttons):
    q = deque([0])
    visited = set()
    presses = 0
    
    while q:
        presses += 1
        for _ in range(len(q)):
            state = q.popleft()
            for button in buttons:
                new_state = state ^ button
                if new_state == target:
                    return presses
                if new_state not in visited:
                    visited.add(new_state)
                    q.append(new_state)

def part1(input_file):
    machines = read_input(input_file)
    ans = 0

    for target, buttons, _ in machines:
        ans += bfs(target, buttons)

    return ans

def part2(input_file):
    machines = read_input(input_file)
    ans = 0

    for _, buttons, counters in machines:
        num_buttons = len(buttons)
        # vi represents the number of times to press buttons[i]
        vars = [Int(f"v{i}") for i in range(num_buttons)]
        opt = Optimize()

        for var in vars:
            opt.add(var >= 0)

        for i, counter in enumerate(counters):
            # Check which buttons increment current counter
            coeffs = []
            for button in buttons:
                increments_counter = button & (1 << i) != 0
                coeffs.append(1 if increments_counter else 0)
            opt.add(Sum([coeffs[i] * vars[i] for i in range(num_buttons)]) == counter) 
        
        total = Int('total')
        opt.add(total == Sum(vars))
        opt.minimize(total)

        if opt.check() == sat:
            m = opt.model()
            ans += m[total].as_long()

    return ans

print(part1("input.txt"))
print(part2("input.txt"))
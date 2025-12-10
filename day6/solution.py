from collections import defaultdict

def read_input1(file):
    problems = defaultdict(list)
    
    with open(file, "r") as f:    
        for line in f:
            row = line.split()
            for i, num in enumerate(row):
                problems[i].append(num)
          
    return problems

def solve(problem):
    ans = 0

    if problem[-1] == '+':    
        for num in problem[:-1]:
            ans += int(num)
    elif problem[-1] == '*':
        ans = 1
        for num in problem[:-1]:
            ans *= int(num)
    
    return ans
        
def part1(input_file):
    problems = read_input1(input_file)
    total = 0

    for problem in problems.values():
        total += solve(problem)

    return total

def read_input2(file):
    cols = defaultdict(list)
    
    with open(file, "r") as f:    
        for line in f:
            for i, num in enumerate(line):
                cols[i].append(num)
          
    return cols

def part2(input_file):
    cols = read_input2(input_file)
    total = 0
    operation = ''
    ans = 0

    for col in cols.values():
        if col[-1] in ['+', '*']:
            operation = col[-1]
            ans = int(''.join(col[:-1]).strip())
        else:
            joined = ''.join(col).strip()
            if joined == '':
                total += ans
            else:
                num = int(joined)
                if operation == '+':
                    ans += num
                elif operation == '*':
                    ans *= num

    return total

print(part1("input.txt"))
print(part2("input.txt"))
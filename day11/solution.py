def read_input(file):
    adj_list ={}

    with open(file, "r") as f:    
        for line in f:
            devices = line.split()
            adj_list[devices[0][:-1]] = devices[1:]
    
    return adj_list

def part1(input_file):
    adj_list = read_input(input_file)
    memo = {}
    
    def dfs(device):
        if device in memo:
            return memo[device]
        if device == 'out':
            return 1

        paths = 0
        for neighbor in adj_list[device]:
            paths += dfs(neighbor)
        memo[device] = paths
        
        return paths

    return dfs("you")

def part2(input_file):
    adj_list = read_input(input_file)
    
    def dfs(device, end, memo):
        if device in memo:
            return memo[device]
        if device == end:
            return 1
        if device == 'out':
            return 0

        paths = 0
        for neighbor in adj_list[device]:
            paths += dfs(neighbor, end, memo)
        memo[device] = paths
        
        return paths

    # All paths found will visit both dac and fft in the same order.
    # If not, there will be cycle and infinite paths.
    if dfs("fft", "dac", {}) > 0:
        return dfs("svr", "fft", {}) * dfs("fft", "dac", {}) * dfs("dac", "out", {})
    else:
        return dfs("svr", "dac", {}) * dfs("dac", "fft", {}) * dfs("fft", "out", {})

print(part1("input.txt"))
print(part2("input.txt"))
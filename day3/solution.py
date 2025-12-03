def read_input(file):
    banks = []
    
    with open(file, "r") as f:    
        for line in f:
            banks.append(line.strip())
          
    return banks

def part1(input_file):
    banks = read_input(input_file)
    total_joltage = 0

    for bank in banks:
        i = 0   # Index of first battery
        second_battery = 0
        for j in range(1, len(bank)):
            if j < (len(bank) - 1) and int(bank[j]) > int(bank[i]):
                i = j
                second_battery = 0
            else:
                second_battery = max(second_battery, int(bank[j]))
        first_battery = int(bank[i])
        joltage = first_battery * 10 + second_battery
        total_joltage += joltage
    
    return total_joltage

NUM_BATTERIES = 12

# Greedy method based on https://www.reddit.com/r/adventofcode/comments/1pcxj6c/comment/ns16nrk/
def part2_greedy(input_file):
    banks = read_input(input_file)
    total_joltage = 0

    for bank in banks:
        joltage = 0
        on_index = -1
        for i in range(NUM_BATTERIES):
            highest_rating = 0
            # Exclude last NUM_BATTERIES - i - 1 indices
            for j in range(on_index + 1, len(bank) - (NUM_BATTERIES - i - 1)):
                if int(bank[j]) > highest_rating:
                    highest_rating = int(bank[j])
                    on_index = j
            joltage = joltage * 10 + highest_rating
        total_joltage += joltage
    
    return total_joltage

# DP method based on https://www.reddit.com/r/adventofcode/comments/1pcxj6c/comment/ns1lz63/
def part2_dp(input_file):
    banks = read_input(input_file)
    total_joltage = 0

    for bank in banks:
        # dp[i][j] is the best solution using i digits from the first j digits
        dp = [([0] * (len(bank) + 1)) for _ in range(NUM_BATTERIES + 1)]
        for i in range(1, NUM_BATTERIES + 1):
            for j in range(i, len(bank) + 1):
                exclude_j = dp[i][j - 1]
                include_j = (dp[i - 1][j - 1]) * 10 + int(bank[j - 1])
                dp[i][j] = max(exclude_j, include_j)
        total_joltage += dp[NUM_BATTERIES][len(bank)]
    
    return total_joltage

print(part1("input.txt"))
print(part2_greedy("input.txt"))
print(part2_dp("input.txt"))
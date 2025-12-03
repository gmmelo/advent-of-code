INPUT_FILE = "input.txt"
PART = 2

# Determine the number of digits based on part 1 or 2
DIGIT_COUNT = 2 if PART == 1 else 12

def main():
    with open(INPUT_FILE, "r") as file:
        total_joltage = 0
        for line in file:
            total_joltage += pack_joltage(line.strip())
        print("The provided batteries can provide you "
              f"with a total of {total_joltage} jolts.")

# The joltage of a pack is the maximum number that can be formed
# by combining the joltage digit of two batteries in the pack
# without rearranging their order.
def pack_joltage(pack: str) -> int:
    if len(pack) < DIGIT_COUNT: return 0
    joltages = [int(x) for x in pack]
    max_joltages = []
    for i in reversed(range(DIGIT_COUNT)):
        max_joltage = max(joltages[:-i]) if i!=0 else max(joltages)
        max_joltages.append(max_joltage)
        max_joltage_index = joltages.index(max_joltage)
        joltages = joltages[max_joltage_index+1:]
    pack_joltage = 0
    for i, joltage in enumerate(reversed(max_joltages)):
        pack_joltage += joltage * 10**i
    return pack_joltage

if __name__ == "__main__":
    main()
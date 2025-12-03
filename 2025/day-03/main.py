def main():
    with open('input.txt', 'r') as file:
        total_joltage = 0
        for line in file:
            line = line.strip()
            if not line: continue
            total_joltage += pack_joltage(line)
        print(f"The provided batteries can provide you with a total of {total_joltage} jolts.")

# The joltage of a pack is the maximum number that can be formed
# by combining the joltage digit of two batteries in the pack
# without rearranging their order.
def pack_joltage(pack: str) -> int:
    joltages = [int(x) for x in pack]
    left_joltage = max(joltages[:-1])
    left_index = joltages.index(left_joltage)
    right_joltage = max(joltages[left_index+1:])
    return left_joltage * 10 + right_joltage

if __name__ == "__main__":
    main()
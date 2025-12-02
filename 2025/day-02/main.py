def main():
    # Initiate an accumulator for our grand total
    total = 0
    # Open file for reading
    with open("input.txt", "r") as file:
        # Loop for reading chunks at a time
        while True:
            # Try to read until next ','
            substr = read_until_comma(file)
            # Exit loop if we've reached the end of the file already
            if substr == '': break
            # Otherwise, parse the substring to find current range
            min, max = parse(substr)
            # Add the sum of invalid numbers within the range to our grand total
            total += invalid_total_in_range(min, max)
    # Print out the total sum of all invalid numbers
    print(f"Total was {total}")

# Takes an integer as the input, and returns True if it's
# valid and False if it's invalid.
# This function is specific for part 1 and only considers
# double repetitions to be invalid.
def part1_is_valid(input_num: int) -> bool:
    # We only care about the string properties of this number
    input_str = str(input_num)
    # Odd length integers can't be composed of two identical-length
    # substrings, so they're always valid.
    is_len_odd = len(input_str) % 2 == 1
    if is_len_odd: return True
    # Otherwise, split input in the middle
    halfway_index = len(input_str) // 2
    first_half = input_str[:halfway_index]
    second_half = input_str[halfway_index:]
    # If the two halves are identical, input is invalid
    if first_half == second_half: return False
    # Otherwise, it is valid
    else: return True

# Takes an integer as the input, and returns True if it's
# valid and False if it's invalid.
# This function is specific for part 2 and considers
# any number of repetitions to be invalid.
def part2_is_valid(input_num: int) -> bool:
    # We only care about the string properties of this number
    input_str = str(input_num)
    # Find every single divisor of the input length
    divisors = []
    for i in range(1, len(input_str)):
        # Check if it's a "perfect" divisor and add to list if it is
        if len(input_str) % i == 0:
            divisors.append(i)
    # Check validity for every possible substring length
    for divisor in divisors:
        # Grab the initial substring to check if it repeats
        initial_substr = input_str[:divisor]
        # Check if it repeats for the rest of the input
        is_repeating = True
        cur_index = divisor
        while cur_index < len(input_str):
            # Next index is the index of the start of the next "repetition"
            next_index = cur_index + divisor
            cur_substr = input_str[cur_index:next_index]
            # If the current substr is not a repetition, set the flag to False (and break the loop)
            if initial_substr != cur_substr:
                is_repeating = False
                break
            # Otherwise, keep checking for the rest of the substrings
            cur_index = next_index
        # If we found that the string is repeating for this size of substring, return that it is invalid
        if is_repeating: return False
        # Otherwise, keep checking for the rest of the divisors
    # If we got here, it means that we didn't find a repeating pattern for any substring/slice length.
    # In this case, the string must be non-repeating, and thus valid.
    return True

# Takes a "dirty" input substring for range as input,
# returns a tuple of (min, max) integers contained within
# the substring.
def parse(input: str):
    dash_index = input.find('-')
    comma_index = input.find(',')
    # Find min and max based on our indexes
    min_str = input[:dash_index]
    min = int(min_str)
    # Assume there is no comma in input
    max_str = input[dash_index+1:]
    # Handle case when comma is found at the end of the input
    if comma_index != -1:
        max_str = max_str[:-1] # Remove last character from the max str
    max = int(max_str)
    return (min, max)

# Takes the minimum and maximum values of a inclusive range as input.
# Returns the sum of every invalid number within that range.
def invalid_total_in_range(min: int, max: int) -> int:
    # Current total of the invalid sum within the range
    total = 0
    for i in range(min, max+1):
        # Add i to accumulator if it's not valid
        if not part2_is_valid(i): total += i
    return total

# Helper function to read from a file until the next ','
# Takes a file and returns a string.
def read_until_comma(file) -> str:
    substr = ''
    while True:
        char = file.read(1)
        substr += char
        if char == '' or char == ',':
            break
    return substr

if __name__ == "__main__":
    main()
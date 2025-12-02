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
def is_valid(input: int) -> bool:
    # We only care about the string properties of this number
    input = str(input)
    # Odd length integers can't be composed of two identical-length
    # substrings, so they're always valid.
    is_len_odd = len(input) % 2 == 1
    if is_len_odd: return True
    # Otherwise, split input in the middle
    halfway_index = len(input) // 2
    first_half = input[:halfway_index]
    second_half = input[halfway_index:]
    # If the two halves are identical, input is invalid
    if first_half == second_half: return False
    # Otherwise, it is valid
    else: return True

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
        if not is_valid(i): total += i
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
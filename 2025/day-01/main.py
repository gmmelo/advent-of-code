# Starting dial state
state = 50

# Change the global state of the dial and return
# how many times we touched 0 during the rotation.
def change_state(direction, amount):
    global state
    old_state = state
    # Calculate new dial state based on direction
    if direction == 'r':
        new_state = old_state + amount
    elif direction == 'l':
        new_state = old_state - amount
    # How many times have we touched 0 in our rotations?
    touches = abs(int(new_state / 100))
    if new_state <= 0 and old_state != 0:
        touches += 1
    # Wrap around the dial state
    new_state = new_state % 100
    # Update the global state
    state = new_state
    # Return the number of '0' touches
    return touches

# Read input file and process each line
counter = 0
with open('input.txt', 'r') as file:
    for line in file:
        direction = line[0].lower()
        amount = int(line[1:].strip())
        old_state = state
        touches = change_state(direction, amount)
        counter += touches

# Output the results
print(f"Total additions: {counter}")
print(f"Final state: {state}")

# Step 1 - Understanding
This problem seems pretty straightforward.

We have packs of batteries represented by lines in our input text file. Each character in the line represents a single battery and its *joltage*.

Our task is to output the sum of the maximum joltage produced by each pack of batteries.

To find the joltage of a pack, we select the maximum two-digit number formed by two batteries in the pack.

It's important to note that we can't rearrange the batteries, meaning that the left digit of our pack joltage has to correspond to a battery that resides to the left of the battery representing the right digit.

### Part 2 Adjustments
The problem is the same, except for the number of digits that we'll use do determine a pack's max joltage. Before, we used 2 digits for the joltage. Now, we'll use 12 digits.

That should mean repeating the max-digit search 12 times, instead of two. I'll have to remove the hard-coded assumptions (like only slicing off the last digit of the input.)

# Step 2a - Planning (Part 1)
I antecipate the following steps to solve the problem:
1. Read the text file and extract every line
2. For each line, find max joltage
    a. Find the maximum jolted battery in the slice including the first to the second-to-last batteries in the pack
    b. Slice the string, keeping only batteries to the right of our battery selected in 'a'.
    c. Find the maximum jolted battery in the slice created in step 'b'.
    d. Use battery 'a' as left digit and 'c' as right digit to craft and save joltage maximum for pack.
3. Sum all max joltages and print the result

# Step 2b - Planning (Part 2)
I antecipate the following steps to solve the problem:
1. Read the text file and extract every line
2. For each line, find max joltage
    a. Find the maximum jolted battery in the slice (excluding the last 11 batteries in the pack)
    b. Repeat this process, but only excluding 10 batteries from the end, then 9, then 8...
    d. Join all joltage digits collected into a 12-digit pack joltage value
3. Sum all pack joltages and print the result

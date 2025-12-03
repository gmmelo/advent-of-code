# Step 1 - Understanding
This problem seems pretty straightforward.

We have packs of batteries represented by lines in our input text file. Each character in the line represents a single battery and its *joltage*.

Our task is to output the sum of the maximum joltage produced by each pack of batteries.

To find the joltage of a pack, we select the maximum two-digit number formed by two batteries in the pack.

It's important to note that we can't rearrange the batteries, meaning that the left digit of our pack joltage has to correspond to a battery that resides to the left of the battery representing the right digit.

# Step 2 - Planning
I antecipate the following steps to solve the problem:
1. Read the text file and extract every line
2. For each line, find max joltage
    a. Find the maximum jolted battery in the slice including the first to the second-to-last batteries in the pack
    b. Slice the string, keeping only batteries to the right of our battery selected in 'a'.
    c. Find the maximum jolted battery in the slice created in step 'b'.
    d. Use battery 'a' as left digit and 'c' as right digit to craft and save joltage maximum for pack.
3. Sum all max joltages and print the result

"""
This is a solution to the second puzzle of Day 1. As the title says, it counts the number of times the
value of the counter increases.
"""

f = open('input.txt', 'r')
increases = 0
nums = [int(i) for i in f.read().split('\n') if i != '']
for i, num in enumerate(nums):
    curr = sum(nums[i:i+3])
    if i > 0:
        prev = sum(nums[i-1:i+2])
        if curr > prev:
            increases += 1
print(f"Numbers increased {increases} times")
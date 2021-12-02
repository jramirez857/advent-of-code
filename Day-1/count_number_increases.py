f = open('input.txt', 'r')
increases = 0
nums = [int(i) for i in f.read().split('\n') if i != '']
for i, num in enumerate(nums):
    if i > 0:
        prev = nums[i-1]
        if num > prev:
            increases += 1
print(f"Numbers increased {increases} times")
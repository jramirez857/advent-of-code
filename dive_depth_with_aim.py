f = open('input.txt', 'r')
directions = [str(i) for i in f.read().split('\n') if i != '']
depth = 0
horizontal = 0
aim = 0

for direction in directions:
    if direction.startswith('forward'):
        horizontal += int(direction.split()[1])
        depth += aim * int(direction.split()[1])
    elif direction.startswith('down'):
        aim += int(direction.split()[1])
    else:
        aim -= int(direction.split()[1])
print(depth, horizontal, depth * horizontal)
    
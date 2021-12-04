import numpy as np

# Reads in the data from the file line by line into a list and converts the
# lists into a numpy array.
bin_nums = np.array(
    [list(i) for i in open("input.txt", "r").read().strip().split("\n")], dtype="int"
)


def binary_to_decimal(binary: list):
    # Raises each binary digit to the power of the index and adds them together
    # to get the decimal value.
    return sum(n * 2 ** i for i, n in enumerate(binary[::-1]))


def _filter(numbers, j, mode):
    # Filters the data based on the mode.
    # If mode is 'co2' then the bits list is filtered to include only the bits
    # with the most common value in that column. If mode is 'oxygen' then the
    # bits list is filtered to include only the bits with the least common value
    # in that column. In both cases, the lists are filtered until only one bit in
    # the list remains.

    # If there are any bits in the column.
    if len(numbers[:, j]) > 1:
        if mode == "CO2":
            # Check if the length of the list of bits minus twice the sum of all bits 
            # in the column is less than 0.
            # If it is, then 0 is the least common value.
            # Otherwise, 1 is the least common value.
            binary_sum = 0 if len(numbers[:, j]) - 2 * sum(numbers[:, j]) <= 0 else 1
        elif mode == "oxygen":
            # Check if the sum of all bits in that column is greater than half the length
            # of the whole column. If it is then 1 is the most common value.
            # Otherwise, 0 is the most common value.
            binary_sum = 1 if sum(numbers[:, j]) >= len(numbers[:, j]) / 2 else 0
        # Filter the bits list to only include the bits that match the most common 
        # or least column value.
        numbers = np.array([b for b in numbers if b[j] == binary_sum])
        # If there is only one bit left in the list, return the bit.
    if numbers.shape[0] < 2:
        return list(numbers[0])
        # Add one to recursively call the function on each column until there is only one list left.
    j += 1
    numbers = _filter(numbers, j, mode)
    return numbers


print(
    f"The oxygen generator rating is { binary_to_decimal(_filter(bin_nums.copy(), 0, 'oxygen')) }\n"
    f"The CO2 Scrubber rating is {binary_to_decimal(_filter(bin_nums.copy(), 0, 'CO2'))}\n"
    f"The life support rating of the submarine is "
    f"{binary_to_decimal(_filter(bin_nums.copy(), 0, 'oxygen')) * binary_to_decimal(_filter(bin_nums.copy(), 0, 'CO2'))}"
)

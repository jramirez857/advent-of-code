import numpy as np
# Reads in the data from the file line by line into a list and converts the
# lists into a numpy array.
bin_nums = np.array([list(i) for i in open('input.txt','r').read().strip().split('\n')], dtype='int')
def binary_to_decimal(binary: list):
# Raises each binary digit to the power of the index and adds them together
# to get the decimal value.
  return sum(n * 2**i for i,n in enumerate(binary[::-1]))

# Calculates the gamma rate using the sum of the binary digits in each column
# of the binary array. If the sum is greater than than half the size of the array, 
# add 1 to the gamma rate. Otherwise, add 0. Do this for every column in the array
# by checking the size of the first array.
gamma_rate = [1 if sum(bin_nums[:, i]) > len(bin_nums[:, i])/2 else 0 for i in range(len(bin_nums[0,:]))]
# Calculates the epsilon rate by raising 2 to each gamma rate value and
# then we use the modulo operator to change the decimal value 2 to binary 0.
epsilon_rate = [2**i % 2 for i in gamma_rate]
print('Part 1 result is:', binary_to_decimal(gamma_rate)*binary_to_decimal(epsilon_rate))


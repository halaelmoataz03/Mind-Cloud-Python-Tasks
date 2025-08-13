"""
The user enters number of lists(K) and the modulo value(M)
I take all the lists, remove the first element which represents the number of elements in each list, and store them in 1 list
Over each combination: I calculate the maximum S and compare it with the previous value then take the maximum of the 2 values
"""

import itertools

K, M = map(int, input().split())

all_lists = []
for i in range(K):
    current_list = list(map(int, input().split()))
    current_list.pop(0)
    all_lists.append(current_list)


maximum = 0
for combination in itertools.product(*all_lists):
    current_value = sum(x**2 for x in combination) % M
    maximum = max(maximum, current_value)

print(maximum)
"""
The user enters the size of matrix then enters the matrix itself
Then I transpose the matrix
Finally I replace any character other than alphanumeric characters between each 2 alphanumeric characters with a single space
"""

import re

# Taking Size
n, m = map(int, input("Enter size (n m): ").split())

# Taking Matrix
matrix = []
for i in range(n):
    matrix.append(input())

# Transposing matrix then appending each character to another list
temp_matrix = []
for j in range(m):
    for i in matrix:
        temp_matrix.append(i[j])

# Replacing any character other than alphanumeric characters between each 2 alphanumeric characters with a single space
tenp_string = ''.join(temp_matrix)
decoded_string = re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',tenp_string)
print(decoded_string)

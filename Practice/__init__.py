import sys

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

max = -sys.maxsize - 1
for i in range(0, len(arr) - 2):
    for j in range(0, len(arr[i]) - 2):
        sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
              arr[i + 2][j + 2]
        if sum > max:
            max = sum


print(max)
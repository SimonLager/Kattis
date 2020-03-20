import math
import sys

inf = open("inout/4.in")
# Parse input
n, k = [int(value) for value in inf.readline().split()]
t = [int(value) for value in inf.readlines()]

requests = [1 for i in range(n)]


for i in range(n - 1): #loopa n varv
    for j in range(i + 1, n): # loopa i till n
        if t[j] < t[i] + 1000:
            requests[i] = requests[i] + 1
            requests[j] = requests[j] + 1
        else:
            break

print(math.ceil(max(requests) / k))
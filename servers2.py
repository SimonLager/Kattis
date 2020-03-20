import math
import sys

nf = open("inout/1.in")
# Parse input
n, k = [int(value) for value in nf.readline().split()]
t = [int(value) for value in nf.readlines()]

# Retrive the last element in the list (the total time we need to cout for)
t_tot = t[-1] #(+1000 but it is not needed since the max can't happen after last request)

max_num_requests = 0
active_requests = [] #using a list as a simple queue
for i in range(t_tot+1):
    
    # add reqest if the request has started
    while(len(t) != 0 and t[0] == i):
        active_requests.append(t.pop(0)+1000) #+1000 to get when req ends
    
    # remove inactive requests
    while(len(active_requests) > 0 and active_requests[0] == i):
        active_requests.pop(0) 
    
    # calculate the max number of reqeusts run simultainiusly
    if len(active_requests) > max_num_requests:
        max_num_requests = len(active_requests)


print(math.ceil(max_num_requests / k))

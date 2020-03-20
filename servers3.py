import math
import sys

# Parse input
n, k = [int(value) for value in sys.stdin.readline().split()]
t = [int(value) for value in sys.stdin.readlines()]

# Retrive the last element in the list (the total time we need to cout for)
t_tot = t[-1] #(+1000 but it is not needed since the max can't happen after last request)

max_num_requests = 0
active_requests = [] #using a list as a simple queue
key_events = []
key_event_queue = []
last_event = t[-1]+1 #initiate with something that should not be the first number

# build key event list
for ti in t:
    
    while(len(key_event_queue) != 0 and key_event_queue[0] < ti):
        key_events.append(key_event_queue.pop(0)) #+1000 to get when req ends
        
    if ti != last_event: #remove doublets, several requests at the same time
        key_events.append(ti)
        key_event_queue.append(ti+1000)
        last_event = ti


print(key_events)
for i in key_events:
    
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
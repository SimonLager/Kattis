import math
import sys


# Parse input
n, k = [int(value) for value in sys.stdin.readline().split()]
t = [int(value) for value in sys.stdin.readlines()]

# Retrive the last element in the list (the total time we need to cout for)
t_tot = t[-1] #(+1000 but it is not needed since the max can't happen after last request)

max_num_requests = 0
active_requests = [] #using a list as a simple queue
# key_events = []
key_event_queue = []
last_event = t[-1]+1 #initiate with something that should not be the first number
active_event_counter = 0

# build key event list
for ti in t:
    
    while(len(key_event_queue) != 0 and key_event_queue[0] <= ti):
        # key_events.append(key_event_queue.pop(0)) #+1000 to get when req ends
        key_event_queue.pop(0)        
        active_event_counter-=1
        
    if ti != last_event: #remove doublets, several requests at the same time
        key_event_queue.append(ti+1000)
        active_event_counter+=1

    if active_event_counter > max_num_requests:
        max_num_requests = active_event_counter

print(math.ceil(max_num_requests / k))
import time
from collections import deque

list_els = [el for el in range(1, 10000)]
quee = deque(list_els)
start_time = time.time()
while list_els:
    el = list_els.pop(0)

diff = time.time() - start_time
print(diff)

start_time = time.time()
while quee:
    el = quee.popleft()

diff = time.time() - start_time
print(diff)
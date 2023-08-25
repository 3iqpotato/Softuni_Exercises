import time
from collections import deque
elements = [el for el in range(1, 100000)]
start1 = time.time()
for _ in range(len(elements)):
    elements.pop(0)
diff = time.time() - start1
print(diff)

elements = deque([el for el in range(1, 100000)])
start2 = time.time()
for _ in range(len(elements)):
    elements.popleft()
diff = time.time() - start2
print(diff)
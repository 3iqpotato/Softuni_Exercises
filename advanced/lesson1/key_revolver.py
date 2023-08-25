from collections import deque

bullets_price = int(input())
gun_barrel_size = int(input())
bullets = [int(el) for el in input().split()]
locks = deque(int(el) for el in input().split())
money = int(input())
bullets_used = 0
bullets_in_gun = min(len(bullets), gun_barrel_size)

while True:
    if not locks:
        print(f'{len(bullets)} bullets left. Earned ${money - bullets_used * bullets_price}')
        break
    else:
        lock = locks.popleft()

    if not bullets:
        locks.appendleft(lock)
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    else:
        bullet = bullets.pop()
        bullets_in_gun -= 1
    bullets_used += 1
    if bullet <= lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(lock)

    if bullets_in_gun == 0 and bullets:
        print('Reloading!')
        bullets_in_gun = min(len(bullets), gun_barrel_size)




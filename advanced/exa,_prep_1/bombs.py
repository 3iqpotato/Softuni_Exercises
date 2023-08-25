from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]

dict_made_bombs = {}
dict_bombs = {
    60: 'Cherry Bombs',
    40: 'Datura Bombs',
    120: 'Smoke Decoy Bombs',
}
all_made = False

while bomb_effects and bomb_casings:

    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    bomb = effect + casing

    if bomb in dict_bombs.keys():
        if dict_bombs[bomb] in dict_made_bombs:
            dict_made_bombs[dict_bombs[bomb]] += 1
        else:
            dict_made_bombs[dict_bombs[bomb]] = 1
    else:
        bomb_casings.append(casing - 5)
        bomb_effects.appendleft(effect)

    if len(dict_made_bombs) == 3:
        min_bombs = min(list(dict_made_bombs.values()))
        if min_bombs == 3:
            all_made = True
            break
            


if all_made:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings) if bomb_casings else 'empty'}")

for key, value in dict_bombs.items():
    print(f'{value}: {dict_made_bombs.get(value, 0)}')
num_electrons = int(input())
shells = []
n = 0
while num_electrons > 0:
    n += 1
    electrons = min(2*n**2, num_electrons)
    num_electrons -= electrons
    shells.append(electrons)
print(shells)
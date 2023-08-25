def percents(num):
    lista = ['.'] * 10
    for n in range(int(num) // 10):
        lista[n] = '%'
    return lista


number = int(input())
if number == 100:
    print('100% Complete!')
    # print(percents(number))
    print(f"[{''.join(percents(number))}]")
else:
    print(f'{number}% [{"".join(percents(number))}]')
    print('Still loading...')

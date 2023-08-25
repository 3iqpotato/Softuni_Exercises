def generate_vector(n, my_vector):
    if n == len(my_vector):
        print(''.join(str(x) for x in my_vector))
        return
    for number in range(0, 2):
        my_vector[n] = number
        generate_vector(n+1, my_vector)




num = int(input())
vector = [0] * num
generate_vector(0, vector)
times = int(input())
stack = []

my_funcs ={
    1: lambda x: stack.append(input_data[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for _ in range(times):
    input_data = [int(el) for el in input().split()]
    my_funcs[input_data[0]](input_data)

stack.reverse()
print(*stack, sep=', ')
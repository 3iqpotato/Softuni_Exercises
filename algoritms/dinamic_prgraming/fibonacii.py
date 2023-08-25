def fibonacii(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacii(n-1, memo) + fibonacii(n-2, memo)
    return memo[n]

num = int(input())

print(fibonacii(num, {}))


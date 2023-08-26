def binomial(n, k, memo):
    key = f'{n}, {k}'
    if key in memo:
        return memo[key]

    if k == n or n == 0 or k == 0:
        return 1
    res = binomial(n-1, k-1, memo) + binomial(n-1, k, memo)
    memo[key] = res
    return res




n = int(input())
k = int(input())

print(binomial(n, k, {}))
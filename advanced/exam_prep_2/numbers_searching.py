def numbers_searching(*args):
    set_args = set(args)
    min_num = min(set_args)
    max_num = max(set_args)
    missing_num = max([x for x in range(min_num, max_num) if x not in set_args])
    nums_list = [num for num in set_args if args.count(num) > 1]
    return [missing_num, sorted(nums_list)]




print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))


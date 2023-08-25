def grocery_store(**kwargs):
    res = [f"{item}: {count}" for item, count in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]
    return '\n'.join(res)

print(grocery_store(
 bread=5,
 pasta=12,
 eggs=12,
))
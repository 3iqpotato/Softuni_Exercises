import re

pattern = r'^(?P<m>.*)\>\d+\|[a-z]+\|[A-Z]+\|[^<>]+<(?P=m)'
pattern1 = r'\d+\|[a-z]+\|[A-Z]+\|[^<>]+'
n = int(input())
for _ in range(n):
    password = input()
    res = re.fullmatch(pattern, password)
    if res:
        x = res.group()
        if len(x) == len(password):
            r = re.findall(pattern1, password)

            c = ''
            count = 0
            # start = False
            for ch in r[0]:


                if ch == '|':
                    count += 1
                    if count > 3:
                        c += ch
                    continue
                c += ch
            print(f"Password: {c}")
        else:
            print("Try another password!")
    else:
        print("Try another password!")


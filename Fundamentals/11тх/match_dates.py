import re
pettern = r"\b(?P<Day>\d{2})(?P<sep>\/|-|.)(?P<Month>[A-Z][a-z][a-z])(?P=sep)(?P<year>\d{4})"
text = input()
result = re.finditer(pettern, text)
for res in result:
    a = res.groupdict()
    print(f"Day: {a['Day']}, Month: {a['Month']}, Year: {a['year']}")
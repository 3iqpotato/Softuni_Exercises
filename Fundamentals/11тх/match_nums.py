import re
text = input()
pattern = r"\b(\w|\.|\-)*@([A-Za-z|\-])*\.([A-Za-z|\-])*(\.[A-Za-z]+)?"

result = re.finditer(pattern, text)
for res in result:
    res.groupdict()
    print(res[0], )


# Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.
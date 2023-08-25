import re
# pattern = r"\b(\w|\.|\-)*@([A-Za-z|\-])*\.([A-Za-z|\-])*([A-Za-z|\-]|\.)*"
pattern = r"(?<=\s)[A-Za-z][\w\-.]*[A-Za-z]@[A-Za-z][A-Za-z\-]*[A-Za-z]\.[A-Za-z][A-Za-z\-]*[A-Za-z](\.[A-Za-z][A-Za-z\-]*[A-Za-z])*"
line = input()
result = re.finditer(pattern, line)
for res in result:
    res.groupdict()
    print(res[0])

    # Many users @ SoftUni confuse email addresses. We @Softuni.BG provide high-quality training @ home or @ class.–- steve.parker@softuni.de.
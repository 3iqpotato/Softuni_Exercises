import re

text = input()

tags_pattern = r"<([^<>]*)>"

found_tags = re.finditer(tags_pattern, text)
for tag in found_tags:
    if tag[1] != "title" and tag[1] != "/title" and tag[1] != "body" and tag[1] != "/body":
        text = text.replace(tag[1], "", 1)

text = text.replace('\\n', '').replace('<>', '').replace('</>', '')

title_pattern = r'<title>(?P<title>.+)</title>'
body_pattern = r'<body>(?P<body>.+)</body>'
title = re.findall(title_pattern, text)
body = re.findall(body_pattern, text)

print(f"Title: {' '.join(title)}")
print(f"Content: {' '.join(body)}")

# <html>\n<head><title>Some title</title></head>\n<body>Here<p> is some</p>content <ahref="www.somesite.com">\nclick</body>\n</html>

rage_text = input().upper()

ast_to_copy = ''
pr_str = ''
all_chrs = ''
for idx in range(len(rage_text)):
    if rage_text[idx].isdigit():
        if len(rage_text) > idx+1:
            if rage_text[idx+1].isdigit():
                ch = int(rage_text[idx] + rage_text[idx+1])
                pr_str += ast_to_copy * ch
                ast_to_copy = ''
                continue
        ch = int(rage_text[idx])
        pr_str += ast_to_copy * ch
        ast_to_copy = ''
    else:
        ast_to_copy += rage_text[idx]
        if rage_text[idx] not in all_chrs:
            all_chrs += rage_text[idx]
print(f'Unique symbols used: {len(all_chrs)}')
print(pr_str)

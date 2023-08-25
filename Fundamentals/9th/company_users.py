data = input().split(" -> ")
company_dict = {}
while "End" not in data:
    company = data[0]
    user_id = data[1]
    if company not in company_dict:
        company_dict[company] = [user_id]
    else:
        if user_id not in company_dict[company]:
            company_dict[company].append(user_id)

    data = input().split(" -> ")
for company in company_dict:
    print(company)
    for user_id in company_dict[company]:
        print(f'-- {user_id}')

# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End
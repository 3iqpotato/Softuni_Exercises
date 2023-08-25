class Party:
    def __init__(self):
        self.people_going = []


party = Party()


people = input()
while people != 'End':
    party.people_going.append(people)
    people = input()
print(f'Going: {", ".join(party.people_going)}')
print(f"Total: {len(party.people_going)}")

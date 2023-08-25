class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people
        self._current_index = 0

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        name = f"{self.name} {other.name}"
        people = self.people.copy()
        people.extend(other.people)
        return Group(name, people)

    def __repr__(self):
        members = []
        for m in self.people:
            members.append(str(m))
        return f"Group {self.name} with members {', '.join(members)}"

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self.people):
            if self._current_index < len(self.people):
                member = f'Person {self._current_index}: {self.people[self._current_index]}'
            self._current_index += 1
            return member
        raise StopIteration

    def __getitem__(self, num):
        return f'Person {num}: {self.people[num]}'

p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(len(first_group))
print(second_group)
print(third_group[0])
for person in third_group:
    print(person)

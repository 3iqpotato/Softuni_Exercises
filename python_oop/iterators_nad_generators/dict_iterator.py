class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.length = len(dictionary)
        self.items = [x for x in self.dictionary.keys()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.items:
            item = self.items.pop(0)
            my_tuple = (item, self.dictionary[item])
            return my_tuple

        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
 print(x)

result = dictionary_iter({"name": "Peter",
"age": 24})
for x in result:
 print(x)

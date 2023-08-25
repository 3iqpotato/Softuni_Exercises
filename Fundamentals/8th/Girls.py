class girl:
    def __init__(self, name, age, is_single, is_cute, is_crazy, tities):
        self.name = name
        self.age = age
        self.is_single = is_single
        self.is_cute = is_cute
        self.is_crazy = is_crazy
        self.tities = tities


gitls = ['Zarina', 'Viki', 'Maikata na Dani', 'Dani', 'Lora']
age = [16, 16, 36, 14, 16]
has_bf = [False, False, True, False, False]
cute = [True, True, True, True, False]
crazy = [False, False, False, True, True]
titis = ['small', 'small', "huge", 'none', 'small']
girls = []
for idx in range(len(gitls)):
    girls.append(girl(gitls[idx], age[idx], has_bf[idx], cute[idx], crazy[idx], titis[idx]))

# for x in girls:
#     print(x.__dict__)
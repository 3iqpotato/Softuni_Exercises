class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        return [x for x in self.products if x[0] == letter]

    def __repr__(self):
        self.result = f"Items in the {self.name} catalogue:"
        for product in sorted(self.products):
            self.result += '\n' + product
        return self.result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):

        res = [p for p in self.products if p.name == product_name]

        if res:
            return res[0]

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        res = "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
        return res

from library import Library


class Book(Library):
    def turn_page(self, page):
        self.page = page

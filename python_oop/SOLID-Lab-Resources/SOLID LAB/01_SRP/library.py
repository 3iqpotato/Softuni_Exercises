class Library:
    BOOKS = []
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def find_book(self, title):
        book = [b for b in Library.BOOKS if b.name == title]
        return book
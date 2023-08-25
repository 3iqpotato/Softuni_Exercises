from math import ceil

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for _ in range(pages):
            self.photos.append([])


    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count/4))

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) > 3:
                if page + 1 == len(self.photos):
                    return "No more free slots"
                else:
                    continue

            self.photos[page].append(label)
            return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        res = ''
        for p in range(self.pages):
            res += '-----------\n'
            s = '[] ' * len(self.photos[p])
            res += s.strip() + '\n'
        res += '-----------\n'
        return res



album = PhotoAlbum(0)
print(album.display())
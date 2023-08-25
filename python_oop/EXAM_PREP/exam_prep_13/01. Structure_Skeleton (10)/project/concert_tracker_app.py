from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIAN_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer":Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if self.find_musician_by_name(name):
            raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIAN_TYPES[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.find_band_by_name(name):
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.find_concern_by_place(place)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        c = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(c)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_musician_by_name(musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        m = self.find_musician_in_band_by_name(band, musician_name)
        if m:
            band.members.remove(m)
            return f"{musician_name} was removed from {band_name}."

        raise Exception(f"{musician_name} isn't a member of {band_name}!")

    def start_concert(self, concert_place: str, band_name: str):
        band = self.find_band_by_name(band_name)
        concern = self.find_concern_by_place(concert_place)

        if self.check_if_band_can_participate(band):

            if self.check_if_band_have_the_skills_to_play(band, concern.genre):

                profit = (concern.audience * concern.ticket_price) - concern.expenses
                return f"{band_name} gained {profit:.2f}$ from the {concern.genre} concert in {concert_place}."
            else:
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        else:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

    def find_musician_by_name(self, name):
        for m in self.musicians:
            if m.name == name:
                return m

    def find_band_by_name(self, name):
        for band in self.bands:
            if band.name == name:
                return band

    def find_concern_by_place(self, place):
        for c in self.concerts:
            if c.place == place:
                return c

    @staticmethod
    def find_musician_in_band_by_name(band, musician_name):
        for m in band.members:
            if m.name == musician_name:
                return m

    @staticmethod
    def check_if_band_can_participate(band):
        set_types = {"Guitarist", "Drummer", "Singer"}
        new_set = set()
        for m in band.members:
            new_set.add(m.__class__.__name__)

        if new_set == set_types:
            return True
        return False

    @staticmethod
    def check_if_band_have_the_skills_to_play(band, genre):
        dict_genres_and_skills = {
            'Rock': {"play the drums with drumsticks", "sing high pitch notes", "play rock"},
            'Metal': {'play metal', 'sing low pitch notes', 'play the drums with drumsticks'},
            'Jazz': {'play the drums with drum brushes', 'sing high pitch notes', 'sing low pitch notes', 'play jazz'}
        }
        bend_members_skills = set([s for m in band.members for s in m.skills])
        if bend_members_skills == dict_genres_and_skills[genre]:
            return True

        print(bend_members_skills)



# a = ConcertTrackerApp()
# print(a.create_musician('Singer', 'bobi', 19))
# print(a.create_musician('Guitarist', 'bobo', 19))
# print(a.create_musician('Drummer', 'bobii', 19))
# a.musicians[0].skills.append('sing low pitch notes')
# a.musicians[1].skills.append('play metal')
# a.musicians[2].skills.append('play the drums with drumsticks')
# print(a.create_band('kur'))
# print(a.create_concert('Metal', 10, 10, 10, 'pleven'))
# print(a.add_musician_to_band('bobi', 'kur'))
# print(a.add_musician_to_band('bobo', 'kur'))
# print(a.add_musician_to_band('bobii', 'kur'))
# # print(a.remove_musician_from_band('bobo', 'kur'))
# # print(a.remove_musician_from_band('bobi', 'kur'))
# print(a.start_concert('pleven', 'kur'))

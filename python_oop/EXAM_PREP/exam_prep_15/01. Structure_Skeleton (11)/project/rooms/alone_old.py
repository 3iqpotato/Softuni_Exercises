from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, 1)
        self.calculate_expenses(*self.appliances)

    @property
    def room_cost(self):
        return 10

    @property
    def appliances(self):
        return []


from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumtions: {total_consumption:.2f}$."

    def pay(self):
        res = []
        rooms_to_remove = []
        for room in self.rooms:
            room_montly_cost = room.expenses + room.room_cost
            if room.budget > room_montly_cost:
                room.budget -= room_montly_cost
                res.append(f"{room.family_name} paid {room_montly_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                res.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                rooms_to_remove.append(room)
        for room in rooms_to_remove:
            self.rooms.remove(room)

        return '\n'.join(res)

    def status(self):
        all_people = sum(r.members_count for r in self.rooms)
        res = []
        text = f'Total population: {all_people}\n'
        for room in self.rooms:
            text += f'{room.family_name} with {room.members_count} members.' \
                    f' Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            idx = 1
            childs_money = 0
            for child in room.children:
                childs_money += child.get_monthly_expense()
                text += f'--- Child {idx} monthly cost: {child.get_monthly_expense():.2f}$\n'
                idx += 1
            text += f'--- Appliances monthly cost: {(room.expenses - childs_money):.2f}$\n'
        res.append(text)
        return '\n'.join(res)

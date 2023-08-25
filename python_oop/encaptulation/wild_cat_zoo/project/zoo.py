class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity - len(self.animals) > 0 and self.__budget >= price:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity - len(self.workers) > 0:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda l: l.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        all_workers_money = sum(p.salary for p in self.workers)
        if all_workers_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= all_workers_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        all_animals_money = sum(a.money_for_care for a in self.animals)
        if all_animals_money > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= all_animals_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [p.__repr__() + '\n' for p in self.animals if p.__class__.__name__ == 'Lion']
        tigers = [p.__repr__() + '\n' for p in self.animals if p.__class__.__name__ == 'Tiger']
        cheetahs = [p.__repr__() + '\n' for p in self.animals if p.__class__.__name__ == 'Cheetah']
        if cheetahs:
            cheetahs[-1] = cheetahs[-1][:-1]
        return f"You have {len(self.animals)} animals\n"\
                f"----- {len(lions)} Lions:\n"\
                f"{''.join(lions)}"\
                f"----- {len(tigers)} Tigers:\n"\
                f"{''.join(tigers)}"\
                f"----- {len(cheetahs)} Cheetahs:\n"\
                f"{''.join(cheetahs)}"

    def workers_status(self):
        keepers = [p.__repr__() + '\n' for p in self.workers if p.__class__.__name__ == 'Keeper']
        caretakers = [p.__repr__() + '\n' for p in self.workers if p.__class__.__name__ == 'Caretaker']
        vets = [p.__repr__() + '\n' for p in self.workers if p.__class__.__name__ == 'Vet']
        if vets:
            vets[-1] = vets[-1][:-1]
        return f"You have {len(self.workers)} workers\n"\
                f"----- {len(keepers)} Keepers:\n"\
                f"{''.join(keepers)}"\
                f"----- {len(caretakers)} Caretakers:\n"\
                f"{''.join(caretakers)}"\
                f"----- {len(vets)} Vets:\n"\
                f"{''.join(vets)}"

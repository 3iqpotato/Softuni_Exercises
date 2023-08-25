

class Worker:
    def __init__(self, name, salary, energy):

        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):

        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):

        self.energy += 1

    def get_info(self):

        return f'{self.name} has saved {self.money} money.'

import unittest

class TestWorker(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('Test', 100, 3)

    def test_init_method(self):
        self.assertEqual('Test', self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(3, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_method(self):
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(3, self.worker.energy)
        self.assertEqual(0, self.worker.money)

        self.worker.work()

        self.assertEqual(100, self.worker.salary)
        self.assertEqual(2, self.worker.energy)
        self.assertEqual(100, self.worker.money)

        self.worker.work()

        self.assertEqual(100, self.worker.salary)
        self.assertEqual(1, self.worker.energy)
        self.assertEqual(200, self.worker.money)

    def test_worker_work_with_no_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', ex.exception.args[0])

    def test_worker_work_with_negative_energy(self):
        self.worker.energy = -3

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', ex.exception.args[0])

    def test_the_rest_function(self):
        self.assertEqual(3, self.worker.energy)

        self.worker.rest()

        self.assertEqual(4, self.worker.energy)

        self.worker.rest()

        self.assertEqual(5, self.worker.energy)

    def test_get_info_method(self):
        result = self.worker.get_info()
        self.assertEqual(f'Test has saved 0 money.', result)
        self.worker.work()
        result = self.worker.get_info()
        self.assertEqual(f'Test has saved 100 money.', result)
        self.worker.work()
        result = self.worker.get_info()
        self.assertEqual(f'Test has saved 200 money.', result)


if __name__ == '__main__':
    unittest.main()
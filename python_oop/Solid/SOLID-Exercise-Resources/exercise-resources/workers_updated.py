from abc import ABC, abstractmethod
import time


class Work(ABC):
    @staticmethod
    @abstractmethod
    def work():
        pass


class Eat(ABC):
    @staticmethod
    @abstractmethod
    def eat():
        pass


class Worker(Work, Eat):

    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Work, Eat):

    @staticmethod
    def work():
        print("I'm super worker. I work very hard!")

    @staticmethod
    def eat():
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Work):
    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class BreakManager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, Eat):
            raise AssertionError(f"`worker` must be of type {Eat}")

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class WorkManager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, Work):
            raise AssertionError(f"`worker` must be of type {Work}")

        self.worker = worker

    def manage(self):
        self.worker.work()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()

except:
    pass

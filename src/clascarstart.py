from  abc import ABC,abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Engine): # has to use start stop to drive

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def drive(self):
        self.start()
        self.stop()


car = Car()
car.drive()















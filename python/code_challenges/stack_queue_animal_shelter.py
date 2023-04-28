from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dog.enqueue(animal)
        elif animal.species == "cat":
            self.cat.enqueue(animal)

    def dequeue(self, pref):
        if pref != "dog" and pref != "cat":
            return None
        elif pref == "dog":
            if self.dog.is_empty():
                return None
            else:
                return self.dog.dequeue()
        else:
            if self.cat.is_empty():
                return None
            else:
                return self.cat.dequeue()


class Dog:
    def __init__(self, name):
        self.name = name
        self.species = "dog"


class Cat:
    def __init__(self, name):
        self.name = name
        self.species = "cat"

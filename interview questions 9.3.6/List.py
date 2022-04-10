class Animal:
   def __init__(self, name):
      self.order = 0
      self.name = name

   # @abc.abstractmethod
   def setOrder(self, ord):
      self.order = ord

   # @abc.abstractmethod
   def getOrder(self):
      return self.order

   # Compare orders of animals to return the older item.
   def isOlderThan(self, animal):
      return self.order < animal.getOrder()

class AnimalShelter:
   def __init__(self):
      self.dogs = []
      self.cats = []
      self.order = 0

   def enqueue(self, animal):
      # Order is used as a sort of timestamp, so that we can compare the insertion order of a dog to a cat.
      animal.setOrder(self.order)
      self.order += 1

      if isinstance(animal, Dog):
         self.dogs.append(animal)
      elif isinstance(animal, Cat):
         self.cats.append(animal)

   def dequeueAny(self):
      # Look at tops of dog and cat queues, and pop the queue with the oldest value.
      if len(self.dogs) == 0:
         return self.dequeueCats()
      elif len(self.cats) == 0:
         return self.dequeueDogs()

      dog = self.dogs[0]
      cat = self.cats[0]

      if dog.isOlderThan(cat):
         return self.dequeueDogs()
      else:
         return self.dequeueCats()

   def dequeueDogs(self):
      return self.dogs.pop(0)

   def dequeueCats(self):
      return self.cats.pop(0)

   def printQueue(self):
      print("Dogs: ", end = "\n")

      for dog in self.dogs:
         print("name: ", dog.name, " order: ", dog.order)

      print("Cats: ", end = "\n")

      for cat in self.cats:
         print("name: ", cat.name, " order: ", cat.order)

class Dog(Animal):
   def __init__(self, name):
      super().__init__(name)

class Cat(Animal):
   def __init__(self, name):
      super().__init__(name)

# ==================== Example =====================

animals = [
   Dog('a'),
   Cat('b'),
   Cat('c'),
   Dog('d'),
   Cat('e'),
   Dog('f'),
   Dog('g'),
]

animalShelter = AnimalShelter()

for animal in animals:
   animalShelter.enqueue(animal)

print("=====before=====")
animalShelter.printQueue()
print("=====before=====")
# animalShelter.dequeueAny()
# animalShelter.dequeueDogs()
animalShelter.dequeueCats()
print("=====after=====")
animalShelter.printQueue()
print("=====after=====")

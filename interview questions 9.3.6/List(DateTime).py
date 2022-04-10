import time

class Animal:
   def __init__(self, name):
      self.arrivalTime = time.strftime("%Y/%m/%d %H:%M:%S")
      self.name = name

   def setArrivalTime(self, arrivalTime):
      self.arrivalTime = arrivalTime

   def getArrivalTime(self):
      return self.arrivalTime

   # Compare orders of animals to return the older item.
   def isOlderThan(self, animal):
      return self.arrivalTime < animal.getArrivalTime()

class AnimalShelter:
   def __init__(self):
      self.dogs = []
      self.cats = []

   def enqueue(self, animal):
      # Order is used as a sort of timestamp, so that we can compare the insertion arrivalTime of a dog to a cat.
      animal.setArrivalTime(time.strftime("%Y/%m/%d %H:%M:%S"))

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
         print("name: ", dog.name, " arrivalTime: ", dog.arrivalTime)

      print("Cats: ", end = "\n")

      for cat in self.cats:
         print("name: ", cat.name, " arrivalTime: ", cat.arrivalTime)

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
   time.sleep(1)

print("=====before=====")
animalShelter.printQueue()
print("=====before=====")
# animalShelter.dequeueAny()
# animalShelter.dequeueDogs()
animalShelter.dequeueCats()
print("=====after=====")
animalShelter.printQueue()
print("=====after=====")

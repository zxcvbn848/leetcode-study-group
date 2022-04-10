import abc

class ListNode:
   def __init__(self, data):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def getSize(self):
      ptr = self.head
      size = 0

      while ptr:
         size += 1
         ptr = ptr.next

      return size

   def append(self, data):
      newNode = ListNode(data)

      if not self.head:
         self.head = newNode
         self.tail = newNode
      else:
         self.tail.next = newNode
         self.tail = self.tail.next

   def deleteFirstNode(self):
      if not self.head:
         return

      # 1. if head is not null, create a temp node pointing to head
      deleteNode = temp = self.head

      # 2. move head to next of head
      self.head = self.head.next

      #3. delete temp node
      temp = None
      
      return deleteNode

class Animal: # (metaclass=abc.ABCMeta)
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
      self.dogs = LinkedList()
      self.cats = LinkedList()
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
      if self.dogs.getSize() == 0:
         return self.dequeueCats()
      elif self.cats.getSize() == 0:
         return self.dequeueDogs()

      dog = self.dogs.head.data
      cat = self.cats.head.data

      if dog.isOlderThan(cat):
         return self.dequeueDogs()
      else:
         return self.dequeueCats()

   def dequeueDogs(self):
      return self.dogs.deleteFirstNode()
   
   def dequeueCats(self):
      return self.cats.deleteFirstNode()

   def printQueue(self):
      dogPtr = self.dogs.head

      print("Dogs: ", end = "\n")

      while dogPtr:
         print("name: ", dogPtr.data.name, " order: ", dogPtr.data.order)
         dogPtr = dogPtr.next

      catPtr = self.cats.head

      print("Cats: ", end = "\n")

      while catPtr:
         print("name: ", catPtr.data.name, " order: ", catPtr.data.order)
         catPtr = catPtr.next

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
animalShelter.dequeueAny()
animalShelter.dequeueDogs()
animalShelter.dequeueCats()
print("=====after=====")
animalShelter.printQueue()
print("=====after=====")

# ==================== Test =====================
# dogNodes = ['a', 'b', 'c', 'd']
# dogs = LinkedList().linkNodes(dogNodes)
# LinkedList.printList(dogs)
# print(LinkedList.getSize(dogs))

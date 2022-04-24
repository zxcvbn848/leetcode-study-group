class Solution:
   def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
      arr1 = sentence1.split(' ')
      arr2 = sentence2.split(' ')

      while arr1 and arr2 and arr1[-1] == arr2[-1]:
         arr1.pop()
         arr2.pop()

      arr1.reverse()
      arr2.reverse()

      while arr1 and arr2 and arr1[-1] == arr2[-1]:
         arr1.pop()
         arr2.pop()

      return not arr1 or not arr2

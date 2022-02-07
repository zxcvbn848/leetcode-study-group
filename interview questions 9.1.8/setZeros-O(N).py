
class Matrix:
   def setZeros(matrix):
      row    = [False] * len(matrix)
      column = [False] * len(matrix[0])

      # Store the row and column index with value 0
      for i in range(len(matrix)):
         for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
               row[i]    = True
               column[j] = True
      
      # Nullify rows
      for i in range(len(row)):
         if row[i]:
            Matrix.nullifyRow(matrix, i)

      # Nullify columns
      for j in range(len(column)):
         if column[j]:
            Matrix.nullifyColumn(matrix, j)

      return matrix

   def nullifyRow(matrix, row):
      for j in range(len(matrix[0])):
         matrix[row][j] = 0

   def nullifyColumn(matrix, column):
      for i in range(len(matrix)):
         matrix[i][column] = 0

matrix = [
   [1, 2, 3, 4],
   [0, 0, 7, 8],
]
result = Matrix.setZeros(matrix)
print(result)

class Matrix:
   def setZeros(matrix):
      rowHasZero    = False
      columnHasZero = False

      # Check if first row has a zero
      for j in range(len(matrix[0])):
         if matrix[0][j] == 0:
            rowHasZero = True
            break

      # Check if first column has a zero
      for i in range(len(matrix)):
         if matrix[i][0] == 0:
            columnHasZero = True
            break

      # Check for zeros in the rest of the array
      for i in range(1, len(matrix)):
         for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
               matrix[i][0] = 0
               matrix[0][j] = 0

      # Nullify rows based on values in first column
      for i in range(1, len(matrix)):
         if matrix[i][0] == 0:
            Matrix.nullifyRow(matrix, i)

      # Nullify columns based on values in first row
      for j in range(1, len(matrix[0])):
         if matrix[0][j] == 0:
            Matrix.nullifyColumn(matrix, j)

      # Nullify first row
      if rowHasZero:
         Matrix.nullifyRow(matrix, 0)
    
      # Nullify first column
      if columnHasZero:
         Matrix.nullifyColumn(matrix, 0)

      return matrix

   def nullifyRow(matrix, row):
      for j in range(len(matrix[0])):
         matrix[row][j] = 0

   def nullifyColumn(matrix, column):
      for i in range(len(matrix)):
         matrix[i][column] = 0

matrix = [
   [1, 2, 3, 4],
   [0, 1, 7, 8],
   [1, 1, 0, 8],
   [1, 1, 7, 8],
]
"""
result:
[
   [0, 2, 0, 4],
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 1, 0, 8]
]
"""
result = Matrix.setZeros(matrix)
print(result)
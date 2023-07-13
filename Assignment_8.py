#Problem 1: Program to add two matrices
#Sol:
matrix1 =[[1,2,3],[6, 4, 9],[7,6,9]]
matrix2 = [[6,9,3],[1,21,1],[1, 19, 11]]
rs = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1)):
        row.append(matrix1[i][j]+matrix2[i][j])
    rs.append(row)


#Problem 2: Program to Multiply Two Matrices 
#Sol:

matrix1 =[[1,2,3],[6, 4, 9],[7,6,9]]
matrix2 = [[6,9,3],[1,21,1],[1, 19, 11]]
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
# Print the result
for row in result:
    print(row)


#Problem 3: Program to print Transpose of a Matrix
#Sol:
matrix = [[12, 7],
          [4, 5],
          [3, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]

# iterating through rows
for i in range(len(matrix)):
    # iterating through columns
    for j in range(len(matrix[0])):
        result[j][i] = matrix[i][j]

for row in result:
    print(row)



#Problem 4: Write a Python Program to Sort Words in Alphabetic Order?
#Sol:
def sort_words(words):
    sorted_words = sorted(words)
    return sorted_words

# Example list of words
word_list = ["banana", "apple", "orange", "grape", "kiwi"]

# Sort the words
sorted_words = sort_words(word_list)

# Print the sorted words
for word in sorted_words:
    print(word)

#Problem 5: Write a Python Program to Remove Punctuation From a String?
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter the string: ")

outputString = ""

for char in string:
    if char not in punctuations:
        outputString += char
        
print(outputString)




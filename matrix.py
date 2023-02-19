def transpose(matrix):
    newmatrix = []
    if not matrix: # om matrisen är tom returneras en tom matris/ hoppar ner till rad 13
        pass
    else: 
        for j in  range(len(matrix[0])): # för varje kolonn där j är kolonnnr
            newmatrix.append([matrix[i][j] for i in range(len(matrix))]) 
    return newmatrix

def powers(inputList,a,b):
    newMatrix = []
    powersList = range(a,b+1)
    for element in inputList:
        newMatrix.append([element**power for power in powersList])
    return newMatrix

def matmul(A, B):
    C = [] #i = rad, j = kolonn
    newRow = []
    newVal=0
    if not B or not A:
        pass
    elif len(A[0]) != len(B):
        print('debug: här kan du inte multiplicera')
        pass
    else:
        for i in range(len(A)): # för varje rad i A
            for j in range(len(B[0])): #för varje kolonn i B
                for k in range(len(B)): # för varje rad i kolonnen B
                    newVal = newVal + A[i][k]*B[k][j]
                newRow.append(newVal)
                newVal = 0
            C.append(newRow)
            newRow = []
    return C
            
def invert(matrix):
    newMatrix = []
    
    det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    
    for row in matrix:
        newMatrix.append([(val/det) for val in row])
        
    newMatrix[0][0], newMatrix[1][1] = newMatrix[1][1], newMatrix[0][0]
    newMatrix[0][1], newMatrix[1][0] = -newMatrix[0][1], -newMatrix[1][0]
    
    return newMatrix

def loadtxt(path):
    matrix = []
    with open(path) as file:
        for lines in file:
            matrix.append([float(val) for val in lines.split()])
    return matrix
        
loadtxt('chirps.txt')
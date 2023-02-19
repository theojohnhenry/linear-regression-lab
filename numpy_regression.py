from numpy import *
import sys
import matplotlib.pyplot as plt
# Samma powerfunktion från matrix.py men returnerar istället en ndarray från numpy biblioteket
def powers(inputList,a,b):
    newMatrix = []
    powersList = range(a,b+1)
    for element in inputList:
        newMatrix.append([element**power for power in powersList])
    return array(newMatrix)

#Tar in lista med koeffecient och ett x-värde.
# approximerar mängden kvitter mha formlen för polynomial regression = 
# y_approx = a_0*x^0 + a_1*x^1 + a_2*x^2 ... + a_n*x^n

def poly(a,x): 
    y = a[0] 
    for degree in range(len(a)): 
        y = y + a[degree] * (x**degree)
    return y


    

matrix = loadtxt(sys.argv[1]) 
n = int(sys.argv[2])

X = transpose(matrix)[0] #endimensionell lista med temperatur
Y = transpose(matrix)[1] # endimensionell lista med kvitter

# allt nedan är avancerad linjär algebra för att ta fram koeffecienter som behövs för vårt ändamål
# "svart låda": som tar in ett dataset och returnerar värden som sedan används för att approximera.
# -------------------------------------------------------
Xp  = powers(X,0,n) 
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()
a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0] # endimensionel ndarray med koeffecienter för varje x
# "svart" låda slutar -----------------------------------
stepsize = int(abs((X[-1]-X[0])/0.2))
X2 = linspace(X[0],X[-1],stepsize).tolist() # skapar en lista med 500 steg (100/0.2) mellan största och minsta x värdet i datasettet.
Y2 = [poly(a,i) for i in X2] #lista för yvärden för den approximerade grafen

plt.plot(X,Y,'ro') #plottar punkterna från datasettet
plt.plot(X2,Y2) # plottar nya snygga grafen
plt.show() 
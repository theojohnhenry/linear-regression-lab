from matrix import *
import sys
import matplotlib.pyplot as plt

matrix = loadtxt(sys.argv[1])
X= transpose(matrix)[0]
Y = transpose(matrix)[1]
# svart låda med avancerad linalg
Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)
[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
chirpPredict = [b + m*temp for temp in X]

plt.plot(X,Y,'ro')
plt.plot(X,chirpPredict)
plt.show()
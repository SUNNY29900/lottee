#06random.py
#파이썬 일반수학함수 접근
import numpy as np


# x= np.random.randint(1,45)  #정답
# x= np.random.randint(45).reshape(3,5)   #에러
x= np.random.rand(45)
print(x)
print()
y= np.random.rand(15) #reshape(3,5) #3행*5열
print(y)
print()

z= np.random.rand(15) #reshape(3,5) #3행*5열
print(z)
print()

#0.000~0.999범위를 벗어남
a= np.random.rand(15) #reshape(3,5) #3행*5열
print(a)
print('0.000~0.999')

b= np.random.rand(15).reshape(5,3) #5행*3열
print(b)
print('0.000~0.999 범위를 벗어남')

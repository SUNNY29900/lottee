#13eye.py

import numpy as np

x=np.zeros(9)   #[0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(x)
print()

y=np.ones(9)   #[1. 1. 1. 1. 1. 1. 1. 1. 1.]
print(y)
print()

z=np.full((), 79)    #결과값 79
print(z)
print()

z=np.full((4,6), 1)   #정수 4행에 6열 1숫자로 4*6
print(z)
print()

print('eye함수(5행*5열)')   #print()'eye함수 zeros +대각 ones')
print('eye함수 zeros +대각 ones')

#결과값 
#  

a=np.eye(5)
print(a)
print()
print('13eye.py문서입니다')
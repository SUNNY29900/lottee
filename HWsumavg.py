
# HWsumavg.py
import numpy as np
import math
my=[175,177,179,181,183]  #변량
my_v=[]
my_value=[]

#1 넘피 np.sum(), np.mean(my)
#2 pow(), sqrt(), sum(my)/ len(my)
#3 [리스트 for반복문] 권장

#math.sqrt(8)결과 2.828427  #표준편차
#print(round(math sqrt(8),2)) 결과 2.83


#1 넘피 np.sum(), np.mean(my)
import numpy as np
import math
my=[175,177,179,181,183]  #변량

#합계계산
total_sum=np.sum(my)

#평균계산
average=np.mean(my)

#출력
print("total_sum", total_sum )
print("average", average )
print()

#2 pow(), sqrt(), sum(my)/ len(my) /각 요소의 제곱과 제곱근을 계산 
#3 [리스트 for반복문] 권장
for value in my:
    my_v.append(pow(value,2)) #제곱 계산
    my_value.append(math.sqrt(value))  #제곱근계산

#합계및 평균 계산
total_sum=sum(my)
average=total_sum/len(my)

#표준편차 계산
std_dev=np.std(my)

#출력
print("my_v", my_v)
print("my_value.", my_value)
print("total_sum", total_sum)
print("average", average)
print("std_dev", std_dev)
print("std_dev", round(std_dev, 2))
print()a
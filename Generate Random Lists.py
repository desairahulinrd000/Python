#Generate Random lists
import random
n=int(input('Number of elements:-'))
n1=int(input('Number of lists:-'))
r=int(input('Enter the range:-'))
num=0
for i in range(n1):
    l=str(i)
    j='l'+l
    j=[]
    for i in range(n):
        j.append(random.randrange(r))
    print('list'+str(num)+'=',j)
    num+=1

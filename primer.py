from time import time
def prime(a):
    k=[2]
    u=[]
    k=range(1,a,2)
    c=0
    for i in k:
        e='\r'
        if c>len(k)-2:
            e='\n'
        print('Part 1 :',(c*100)/len(k),'%',end=e)
        if i%2!=0 and i!=1 and i%3!=0 and i%5!=0 and i%7!=0:
            u.append(i) 
        elif i==2 or i==3 or i==5 or i==7:
            u.append(i)
        c+=1
    return u
   
num=int(input('Enter a number : '))
s=time()
k=prime(num)
c=0
for i in k:
    e='\r'
    if c>len(k):
        e='\n'
    print('Part 2 :',(c*100)/len(k),'%',end=e)
    c+=1
    if num%i==0:
        print('\n\n',i,end='\n\n')
a=[]

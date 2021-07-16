from time import time
red = '\33[91m'
grn= '\33[92m'
start = time()
def p(a):
    k=[2]
    u=['2','3','5','7']
    for I in range(2,a+1):
        if I%2!=0:
            k.append(I) 
    for i in k:
        if i!=2 and i%3!=0 and i%5!=0 and i%7!=0:
            u.append(i)
    print(grn) 
    print(u)
num=int(input('Enter a limit : '))
p(num)
stop=time() 
t=(stop-start)/1000
ips=(num/t) 
print(red,"Competed in ",t ," seconds","(",ips,"number per second) ") 



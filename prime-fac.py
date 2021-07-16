from time import time
s=time()
red = '\33[91m'
grn= '\33[92m'
def p(a):
    k=[2]
    u=[2,3,5,7]
    for I in range(2,a+1):
        if I%2!=0:
            k.append(I) 
    for i in k:
        if i!=2 and i%3!=0 and i%5!=0 and i%7!=0:
            u.append(i) 
    return u
num=int(input('Enter a number : '))
y=input("1)Min Prime Factor\n2)Max Prime factor\nSelect : ") 
k=p(num)
if y=='1':
    y="Min Prime Factor"
elif y=='2':
    y='Max Prime factor'
    k=k[::-1]
for i in k:
    if num%i==0:
        print(red,y,'of',num,'is',i) 
        print(grn,i,"x",num//i,"=",red, num)
        break
e=time()
t=(e-s)/1000
ips=num/t
print(red) 
print("\n"*3,"Done in",t,"(",ips,"numbers per second) ") 

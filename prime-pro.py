from time import time
red = '\33[91m'
grn= '\33[92m'
s=time()
def p(a):
    k=[2]
    u=[2,3,5,7]
    k=range(1,a,2)
    for i in k:
        print((i/a)*100,"% done",end='\r')
        if i!=2 and i%3!=0 and i%5!=0 and i%7!=0:
            u.append(i) 
    return u
num=int(input('Enter a number : '))
k=p(num)
a=[]
def mul(a):
    b=1
    c=""
    for I in range(len(a)):
        b*=a[I]
        if I==(len(a)-1):
            c+=str(a[I])+" = "
        else:
            c+=str(a[I])+" x "
    return [b,c]
for i in k:
    if num%i==0:
        a.append(i)
h=mul(a) 
print("product of prime factors : ",h[1],h[0]) 
if h[0]==num:
    print(num, " is a Product of prime factors") 
else:
    print("Number has "+str(len(a))+" prime factors")
       

e=time()
t=(e-s)
ips=num/t 
print("\n"*3,"Done in",t,"(",ips,"numbers per second) ")

# this file tests the growth rates of various mathematical functions 

import math 

a = [] 
b = [] 
c = [] 
d = [] 
e = [] 
for n in range (1,12):
    curr1 = n*n*math.log(n)
    a.append(curr1) 
    curr2 = 2**n
    b.append(curr2) 
    curr3 = 2**curr2 
    c.append(curr3) 
    curr4 = n**(math.log(n))
    d.append(curr4) 
    curr5 = n**2 
    e.append(curr5) 

print(a) 
print(b)
print(c) 
print(d) 
print(e) 

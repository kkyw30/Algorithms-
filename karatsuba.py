def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y 
    else: 
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2

        a = x // 10**(nby2)                      # separate into first half of first number (a)
        b = x % 10**(nby2)                      # second half of first number (b) 
        c = y // 10**(nby2)                      # first half of second number (c) 
        d = y % 10**(nby2)                      # second half of second number (d) 

        ac = karatsuba(a, c)
        bd = karatsuba(b, d) 
        ad_plus_bc = karatsuba(a+b, c+d)

        result = ac * 10**(2*nby2) + ((ad_plus_bc - ac - bd) * 10**(nby2)) + bd 

        return result 

#print(karatsuba(8, 7))
#print(karatsuba(10, 11))
#print(karatsuba(19, 73))
#print(karatsuba(5039, 4056))
print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))

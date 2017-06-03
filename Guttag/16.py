x = 8
y = 102
z = 112
if x%2!=0: #x is odd
    if y%2!=0: #y is odd
        if z%2!=0: #z is odd
            if y<=x and z<=x:
                print x
            elif x<=z and y<=z:
                print z
            elif x<=y and z<=y:
                print y
        else: #z is even
            if x>y:
                print x
            else:
                print y
    else: #y is even
        if z%2!=0: #z is odd
            if x>z:
                print x
            else:
                print z
        else: #z is even
            print x
            
else: #x is even
    if y%2==0: #y is even
        if z%2==0: #z is even
            print "All are even!"
        else: #z is odd
            print z
    else: #y is odd
        if z%2!=0: #z is odd
            if y>z:
                print y
            else:
                print z
        else: #z is even
            print y
    

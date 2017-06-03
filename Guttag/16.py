x = 8
y = 102
z = 112
if x%2!=0:
    if y%2==0:
        print x
    elif y%2!=0:
        if z%2==0:
            if x>y:
                print x
            else:
                print y
        else:
            if y<x and z<x:
                print x
            elif x<z and y<z:
                print z
            elif x<y and z<y:
                print y
else:
    if y%2==0:
        if z%2==0:
            print "All are even!"
        else:
            print z
    else:
        if y>z:
            print y
        elif z>y:
            print z
    

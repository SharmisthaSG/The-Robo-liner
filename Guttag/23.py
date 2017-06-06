integer = int(raw_input("Enter a number"))
for root in range(0, integer+1):
    for pwr in range(1,7):
        if root**pwr==integer:
            print root, pwr
            break
    if root**pwr==integer:
        break
if root**pwr!=integer:
    print "No such pair exists" 
    #techincally no favourable condition



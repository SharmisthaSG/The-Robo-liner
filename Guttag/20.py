k=10 #number of inputs
y=0 #initialised to-be final answer
while k!=0:
    x=int(raw_input("Enter an int")) #taking input python 2.7
    if x%2!=0 and x>y: #checking conditions to update y
        y=x
    k=k-1 #loop execution
if y==0:
    print "All even"
else:
    print y #final answer

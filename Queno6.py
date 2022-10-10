# Write a python script to print first N even natural numbers.
a=int(input(" ENTER A NUMBER: "))
r=range(1,a+1)
for x in r:
    if x%2==0:
        print(x)
# Write a python script to print first N odd natural numbers 
a=int(input('Enter a number: '))
r=range(1,a+1)
for x in r:
    if x%2!=0:
        print(x)
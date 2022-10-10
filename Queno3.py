# Write a python script to print first M multiples of N.
m=int(input("Enter a First Multiples: "))
n=int(input("Enter a multiples of: "))
r=range(1,m+1)
for a in r:
    print(n*a)
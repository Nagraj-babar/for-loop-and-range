# Write a python script to print the first 10 multiples of N in reverse order.
a=int(input("Enter a number: "))
r=range(10,0,-1)
for x in r:
    print(x*a)


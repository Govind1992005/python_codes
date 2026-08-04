#natural numbers 
print("Up to which number you want to print natural numbers? ")
n=int(input(""))
print("The first",n,"natural numbers are ")
m=1
while (n>m):
    print(m ,end=", ")
    m=m+1
print(m ,end=".\n")

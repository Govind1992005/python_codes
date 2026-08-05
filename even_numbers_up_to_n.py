# even numbers upto n
count=int(input("Up to which number you want to print even numbers? "))
counter=0
print("The even numbers up to ",count,"are :")
while (counter<count-1):
    print(counter,", ",sep="",end="")
    counter=counter+2
print(counter ,".")

#n even numbers version 2
count=int(input("How many even numbers you want to print? "))
print("The first",count,"even numbers are")
counter=0
while (counter<count*2-2):
    print(counter,", ",sep="",end="")
    counter=counter+2
print(counter,".\n",sep="")

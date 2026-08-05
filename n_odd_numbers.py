# n odd numbers
odd_count=int(input("How many odd numbers do you want to print? "))
print("The first",odd_count,"odd numbers are ")
odd_counter=1
while (odd_counter<odd_count*2-1):
    print(odd_counter,", ",sep="",end="")
    odd_counter=odd_counter+2
print(odd_counter,".\n",sep="")

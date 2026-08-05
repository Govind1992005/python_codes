# odd numbers upto n
odd_count=int(input("Up to which number do you want to print odd numbers? "))
print("The odd numbers up to",odd_count,"are")
odd_counter=1
while (odd_counter<odd_count-1):
    print(odd_counter,", ",sep="",end="")
    odd_counter=odd_counter+2
print(odd_counter,".\n",sep="")

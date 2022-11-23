numbers = [1,2,3,4,5,2,6]
#in the above list find value 2,if it is present replace it with 200,only update the first occurence
#write a program to turn every item of list into its square
#output
list1 = ["x","y","z"]
list2 = [1,2,3]
list3 = list1+list2
for x in list2:
      list1.append(x)
print(list1)
list1.append()
print(list3)



indx = numbers.index(2)
numbers[indx]=200 
print(numbers)
numbers.reverse()
print(numbers)

#x = []
#for i in numbers:
  #  i =i**2
 #   x.append(i)
#print(x)        
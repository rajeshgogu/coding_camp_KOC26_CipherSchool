#create a function to print your name and age

def name(firstname,age):
    print("name :"+firstname)
    print("age :"+age)
name("rajesh","18") 


#write a program to create a function using the following conditions
#it should accept employer name and salary and display both
# if the salary is missing then assign the default value as 10000 to salary
# ben(12000) #mike(15000) #bob() 

def name(name,salary=10000):
    print("name:"+name)
    print("income:"+salary)
name("ben",12000)
name("mike",15000)
name()    

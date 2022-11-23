def factorial(num):
    if num==0:
        return num
        return num*(factorial(num-1))
                   


a = 9
def sum_recursion(num):
    if num==0:
        return num
        return num+sum_recursion(num-1)

    return num+sum_recursion(num-1)
    ans=sum_recursion(5)
    print(ans)



def hello():
    print("hello world")
    hello()
hello()    




a = 10
def func():
    a = 15
    print(a)
func()  
print(a)  






#keyword variable length argument

def details(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
details(name="rajesh",age="16",place="tirupati")        

print("\t *********CALCULATOR********** \t")
print("\n")
print("\tThe functions performed are as follows: ")
print("\t1.Addition")
print("\t2.Substraction")
print("\t3.Multiplication")
print("\t4.Division")
print("\t5.Exponential")
print("\t6.Square")
print("\t7.Cube")
print("\t0. EXIT")

#defining the Addition function
def add():  
    a=int(input("Enter the first number \n"))
    b=int(input("Enter the second number \n"))  
    sum=a+b
    print("The sum of",a,"and",b,"is",sum)
    
#defining the  Substraction function
def sub():
    a=int(input("Enter the first number \n"))
    b=int(input("Enter the second number \n"))
    diff=a-b
    print("The difference of",a,"and",b,"is",diff)
    
#defining the Multiplication function
def mul():    
    a=int(input("Enter the first number \n"))
    b=int(input("Enter the second number \n"))  
    res=a*b
    print("The product of",a,"and",b,"is",res)
    
#defining the Division  function
def div():    
    a=int(input("Enter the first number \n"))
    b=int(input("Enter the second number \n"))  
    res=a/b
    print("The quotient  of",a,"and",b,"is",res)
    
#defining the Exponential function    
def exp():    
    a=int(input("Enter the first number \n"))
    b=int(input("Enter the second number \n"))  
    res=a**b
    print(a,"To the power of",b,"is",res)
    
#defining the Square function    
def square():
    
    a=int(input("Enter the first number \n"))
    b=int(input("Enter the second number \n"))  
    sq1=a**2
    sq2=b**2
    print("The square of",a,"is",sq1)
    print("The product of",b,"is",sq2)

#defining the Cube function
def cube():
    
    a=int(input("Enter the first number \n"))
    b=int(input("Enter the second number \n"))  
    sq1=a**3
    sq2=b**3
    print("The square of",a,"is",sq1)
    print("The product of",b,"is",sq2)   

while(True):
    choice=int(input("Enter the choice : \n"))
  
    
    if(choice == 1):
        add()
    elif(choice == 2):
        sub()
    elif(choice == 3):
        mul()
    elif(choice == 4):
        div()
    elif(choice == 5):
        exp()
    elif(choice == 6):
        square()
    elif(choice ==7):
        cube()
    elif(choice == 0):
        print("***************The calculations ended**************")
        exit(0)
        break
    else:
        print("Error!!!")


    




    
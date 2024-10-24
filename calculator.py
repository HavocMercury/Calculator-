a=int(input("First number: "))
b=int(input("Second number:"))
c=input("The operation you want: ")
resa=isinstance(a,int)
resb=isinstance(b,int)
if resa==True and resb==True or c=='+' or c=='-' or c=='/' or c=='//' or c=='*' or c=='**' or c=='%':
    if c=='+':
        print(a+b)
    elif c=='-':
        print(a-b)
    elif c=='/':
        print(a/b)
    elif c=='//':
        print(a//b)
    elif c=='*':
        print(a*b)
    elif c=='**':
        print(a**b)
    elif c=='%' :   
        print(a%b)  
    else:
        print("Wrong Input")
    


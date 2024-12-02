while True: #this is version 3 of the calculator prog (allows you to run it as many times as you want)
 a=int(input("First number: ")) #For confirming whether the first number is an integer or not
 b=int(input("Second number:")) #For confirming whether the second number is an integer or not
 c=input("The operation you want: ")
 if c=='+' or c=='-' or c=='/' or c=='//' or c=='*' or c=='**' or c=='%':
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
    print("Wrong Operation")

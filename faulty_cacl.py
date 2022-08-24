while(True):
    print("Enter first number")
    print("(Only number pls):")
    num1 = int(input())
    print("Enter second number")
    print("(Only number pls):")
    num2 = int(input())
    print("Select operation '+','-','*','/'")
    op= input()

    if op== "+":
        if num1 == 56 and num2 == 9 and op =="+":
            print("77")
        else:
            print(num1+num2)

    elif op== "-":
        print(num1-num2)
    elif op== "*":
        if num1 == 45 and num2 == 3 and op == "*":
            print("555")
        else:
            print(num1*num2)
    elif op== "/":
        print(num1/num2)

    else:
        print("you choose wrong operator")
    print ("want more calculation 'y'or'n'")
    ur = input()
    if ur == "n":
        break
    elif ur== "y":
        print("ok sure !")
    else:
        print("Wrong Button error ! RESTARTING CALC")

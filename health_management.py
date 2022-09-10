a=int(input("Choose    1) Update exercise  2) Update Food intake 3) Show data\n"))
b= int(input("Select profile 1)Rohan  2)Harry 3) Larry\n"))

q = open("Harry_exe.txt", "w")
q.close()

if a==1 and b==1:
    q = open("Rohan_exe.txt", "w")
    q.close()
    c = input("Please write your data here\n")
    q = open("Rohan_exe.txt","r+")
    q.write(f"{c}\n")


    # print(q.readlines())
    q.close()
elif a==1 and b==2:
    q = open("Harry_exe.txt", "w")
    q.close()
    c = input("Please write your data here\n")
    q = open("Harry_exe.txt", "r+")
    q.write(c)
    q.write("\n")
    # print(q.readlines())
    q.close()
elif a==1 and b==3:
    q = open("Larry_exe.txt", "w")
    q.close()
    c = input("Please write your data here\n")
    q = open("Larry_exe.txt", "r+")
    q.write(c)
    q.write("\n")
    # print(q.readlines())
    q.close()
elif a == 2 and b == 1:
    c = input("Please write your data here\n")
    q = open("Rohan_food.txt", "r+")
    q.write(c)
    q.write("\n")
    # print(q.readlines())
    q.close()
elif a==2 and b==2:
    c = input("Please write your data here\n")
    q = open("Harry_food.txt", "r+")
    q.write(c)
    q.write("\n")
    # for v in q :
    # print(v,end=" ")
    q.close()
elif a==2 and b==3:
    c = input("Please write your data here\n")
    q = open("Larry_food.txt", "r+")
    q.write(c)
    q.write("\n")
    q.close()
elif a == 3 and b == 1:
    # c = input("Please write your data here\n")
    q = open("Rohan_exe.txt", "r+")
    print("----------THIS IS EXERCISE FILE----------")
    for line in q:

        print(line, end=" ")
    q.close()
    V = open("Rohan_food.txt", "r+")
    print("----------THIS IS FOOD FILE----------")
    for line in V:

        print(line, end=" ")
    q.close()
elif a == 3 and b == 2:
    q = open("Harry_exe.txt", "r+")
    # q.write(c)
    # q.write("\n")
    print("----------THIS IS EXERCISE FILE----------")
    for line in q:

        print(line, end=" ")
    q.close()
    V = open("Harry_food.txt", "r+")
    print("----------THIS IS FOOD FILE----------")
    for line in V:
        print(line, end=" ")
    q.close()
elif a == 3 and b == 1:
    q = open("Larry_exe.txt", "r+")
    # q.write(c)
    # q.write("\n")
    print("----------THIS IS EXERCISE FILE----------")
    for line in q:

        print(line, end=" ")
    q.close()
    V = open("Larry_food.txt", "r+")
    print("----------THIS IS FOOD FILE----------")
    for line in V:

        print(line, end=" ")
    q.close()
else:
    print("There is error in choices")


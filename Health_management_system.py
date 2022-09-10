import datetime
import time


def cal(e,f):
    pass
def dat(b):
    if b==1:
        v = input("Please write here (in calories)\n")
        q = open(f"{c}_exe.txt", "r+")
        q.write(f"{time.asctime(time.localtime(time.time()))}:-{v}\n")
        q.close()
    elif b==2:
        v = input("Please write here (in calories)\n")
        q = open(f"{c}_food.txt", "r+")
        q.write(f"{time.asctime(time.localtime(time.time()))}:-{v}\n")
        q.close()

if __name__=="__main__":
    print("-----Welcome__to__Health__Management__system-----")

    a = int(input("1) Create Profile  2) Existing  3) Exit\n"))

    if a ==1:
        c = input("Enter Your Name: ")
        o=open(f"{c}_exe.txt","w")
        z = open(f"{c}_food.txt", "w")
        o.close()
        z.close()
    b= int(input("Choose to add in profile    1) Calories Burn  2) Calories intake 3) Show data\n"))
    dat(b)

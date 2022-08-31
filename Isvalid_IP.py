def isValid(s):
    #code here
    a=s.split(".")
    m=0
    n=s.count(".")
    if n==3:

        for i in a:
            if len(i) >= 4:
                print(len(i))
                m = m + 0
            elif i =="0":
                m = m + 0
            elif i == "00":
                m = m + 0
            elif int(i)<=255:
                m=m+1
            else :
                m=m+0
    else:
        return 0

    if m<4:
        return 0
    else:
        return 1
if __name__=="__main__":
    s=input("Enter Your IP - ")
    print(isValid(s))

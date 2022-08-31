def rev(s):
    m=0
    d=""
    a = s.split(".")[::-1]
    for items in a:
        if m%2==0:
            a.insert(m,".")
            m=m+1
        elif m==0:
            m=m+1
        else :
            m=m+1
    a.pop(0)
    for i in a:
        d=d+i
    return d
if __name__=="__main__":
    s=input("Enter Your Sentence - ")
    print(rev(s))

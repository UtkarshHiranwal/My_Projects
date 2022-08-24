s=int(input("enter number : "))
one = 0
two = 0
five = int((s-4)/5)
print(five)
if ((s-5*five)%2==0):
    one=2
else:
    one=1
two=int((s-5*five-one)/2)
print("Total numbers of coins: ",one+two+five)
print("Total numbers of five coins: ",five)
print("Total numbers of two coins: ",two)
print("Total numbers of one coins: ",one)
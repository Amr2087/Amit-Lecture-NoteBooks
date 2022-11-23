# n=int(input("Enter number:"))
# temp=n
# new_=0
# while n>0:
#     last_d = n%10
#     new_ = new_+last_d*10

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
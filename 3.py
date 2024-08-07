# finding armstromg number
a=153

sum=0
temp=a
while(temp>0):
   
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if(sum==a):
        print("Given number is armstrong number")
else:
        print("Not a armstrong number")

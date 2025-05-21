#sum of first natural numbers
n=int(input("Enter the value of terms:"))

sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1

print("\nSum=",sum)

#infinite loop
#j=0
#while j<=0:
#    print("I WILL RUN FOREVER!")

#armstrong number
num=int(input("Enter a number:"))
sum=0

temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if num==sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
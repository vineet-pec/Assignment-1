#assignment1

#soln1
#calculate average of three numbers
print("question 1")
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
print("average is",(a+b+c)/3)

#soln2
#finding person income tax
grossincome=int(input("gross income"))
taxrate=0.2
standarddeduction=10000
dependentdeduction=3000
noofdependents=int(input("noofdependents"))
taxableincome=(grossincome-standarddeduction-(dependentdeduction*noofdependents))
print(taxableincome)
tax=taxableincome*taxrate
print(tax)

#soln3
#number of seconds
seconds=int(input("seconds"))
print(seconds,"s=",seconds//60,"m & ",seconds%60,"s")

#soln4
#add three numbers
a=25
b='25'
c=25.0

sum=str(a+ int(b)+ int(c))

#Soln 5
import math
while(d<=345):
    r=math.radians(d)
    sine=round(math.sin(r),4)
    cosine=round(math.cos(r),4)
    print(d , sine , cosine)
    d=d+15
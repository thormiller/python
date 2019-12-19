import random 
a = random.randint(0,1000000000000)
b = int(input("What number "))
c = 0
while ( b != a):
 c = c + 1
 if ( b > a):
	 print("big")
 elif( b < a):
	 print("small")
 b = int(input("What number "))


print(str(c)+ " try answer: " + str(a) )

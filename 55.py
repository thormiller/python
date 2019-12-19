import random 
a = random.randint(1,10)
b = random.randint(1,10)
ans = a * b
c = 0
n = int(input("What is" + str(a)+ "*" +str(b)+"?"))
while ( n != ans):
 c = c + 1 
 if ( n > ans):
	 print (" to big")
	 
 elif ( n < ans):
	 print("small")
 n = int(input("What is" + str(a)+ "*" +str(b)+"?")) 
print(str(ans)+" nice try your have "+ str(c) + " try")

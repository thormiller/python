import random
a = input("What is your name? ")
b = input("What is your last name? ")
print("hey " + a + " " + b + ",nice to meet you!")
c = input("So, " + a + " " + b + " are you ready to do some math? yes to continue ")

if( c == "yes"):
 d = random.randint(1,10)
 e = random.randint(1,10)
 ans = d * e
 f = int(input("What is " + str(d) + " * " + str(e) + " equal? "))
 if ( f < ans ):
    print("The answer is too small")
 elif ( f > ans):
    print("The answer is too big")
 else:
    print("correct")
g = int(input("Okay if you don't want, tell me how old are you? "))
if ( g <= 10):
	print("Man, you are still a such young puppy!")
elif ( g <= 20):
	print("well,Do you got a girlfrend yet.")
elif ( g <= 40):
	print("Awesome you got an amazing life")
elif ( g > 40):
	print("great your life is alost over, did you buy your casket, is on sale this month!!!" )		
h = input("did you have a good day today? yes/no ")
if ( h == "yes"):
    print("Is nice to hear that.")
else:
	print("Sorry to hear that")
	

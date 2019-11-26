shane = int(input("Enter today's day numerically:"))
if ( shane == 30 or  shane==15):
	print("It's payday!")


if (not shane ==30 and not shane ==15):
	print("Sorry, not a payday.")

thor = int(input("Enter the  current year: "))

if (thor == 2019):
	print("Anwsome")
	
if (not thor == 2019):
	print("Awful")

import random
a = random.randint(1,10)
b = random.randint(1,10)
print ("What is: " + str(a) + " X " + str(b) + "?")
ans = int(input("Answer: "))
if (a * b == ans):
   print("correct")

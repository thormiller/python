

feet1 = int(input("Enter the Feet for the first piece of fabric: "))
inches1 = int(input("Enter the Inches for the first piece of fabric: "))

feet2 = int(input("Enter the Feet for the second piece of fabric: "))
inches2 = int(input("Enter the Inches for the second piece of fabric: "))

totalinches = inches1 + inches2 + feet1 *12 + feet2 *12
tf = int(totalinches / 12)
ti = int(totalinches % 12)
print("Feet: "+str(tf)+" Inches: "+str(ti))

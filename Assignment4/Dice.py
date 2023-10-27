import random
while True:
    d = random.randint(1,6) 
    if d == 6:
        print ("The result was",d)
        
        a = random.randint(1,6)
        print ("Your first additional roll is",a)
        b = random.randint(1,6)
        print ("Your second additional roll is",b)
    else: print(d,"was the result, you dont have another chance")
    break

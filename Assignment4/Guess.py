import random
pc_number = random.randint(0,10)
count=0
while True:
    user_number = int(input("Enter num: "))
    count+=1
    #count=count+1

    if user_number == pc_number:
        print("ok")
        break

    if user_number < pc_number:
        print("Adad bozorgtari vard kon")

    if user_number > pc_number:
        print("Adad kochektari vard kon")
    
print (pc_number)
print (count)


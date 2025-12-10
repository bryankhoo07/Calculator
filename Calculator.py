First_num=int(input("Enter a number"))
Second_num=int(input("Enter a number"))

print("Press 1 for addition, Press 2 for subtraction, Press 3 for multiplication, Press 4 for division")

function_choice=int(input("Enter a number:"))

if function_choice == 1 :
    print(First_num+Second_num)
elif function_choice == 2 : 
    print(First_num-Second_num)
elif function_choice ==3 :
    print(First_num*Second_num)
elif function_choice == 4 :
    if Second_num == 0 :
        print("Cannot divide by 0")
    else :
        print(First_num/Second_num)
else:
    print("Invalid Choice")




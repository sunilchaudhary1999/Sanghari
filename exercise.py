# Write a program that check weather the number is enter by user is the number is positive, negative or zero.
# Werote a program the number is given by user the number check odd or even.
# Write a program to check if the number is division by 5 not by 3.
# Write a program to check if the number is division by 5 and 7.
# Write a program to check the age group of person on the age.
# Write a program to check the body mass calculation.


# Werote a program the number is given by user the number check odd or even.
# inum =int(input("Enter the number: "))
# if inum%2 ==0:
#     print(inum,"The given number is even ")
# else:
#     print(inum,"The given number is odd")
    

# # Write a program that check weather the number is enter by user is the number is positive, negative or zero.

# pnzNum =int(input("Enter the number: "))
# if pnzNum == 0:
#     print(pnzNum,"You enter the zero number")
# elif pnzNum > 0:
#     print(pnzNum,"You enter the postive number")
# else:
#     print(pnzNum,"You enter the negative number")

# Write a program to check if the number is division by 5 not by 3.

# divNum = int(input("Enter the number: "))
# if (divNum%5 ==0 and divNum%3==0):
#     print("the number is divisible by 5 and 3")
# else:
#     print("not divisible")
    

# Write a program to check if the number is division by 5 and 7.
# dNum = int(input("Enter the number: "))
# if (dNum%5 ==0 and dNum%7==0):
#     print("the number is divisible by 5 and 7")
# else:
#     print("not divisible")
    
    
# Write a program to check the body mass calculation.
# bodyWeight = int(input("The the weight"))
# bodyHeight = int(input("The the height"))
# bmi = bodyWeight/bodyHeight*bodyHeight
# if (bmi>17.5 and bmi <28):
#     print("You have good health condition")
# else:
#     print("You have not good height and wight")


# Write a program to check the age group of person on the age.
ageGroup =int (input("Enter your age:"))
if ageGroup<5:
    print("Baby")
elif ageGroup>5 and ageGroup<13:
    print("Child")
elif ageGroup>13 and ageGroup<16:
    print("Teenage")
elif ageGroup>16 and ageGroup<30:
    print("Young")
elif ageGroup>30 and ageGroup<50:
    print("Man")
else:
    print("Old")

#Student grade short list 
marks =int(input("Enter your marks :"))
if marks>=90 and marks<=100:
    print("Grade A+")
elif marks>=80 and marks<90:
    print("Grade A")
elif marks>=70 and marks<80:
    print("Grade B+")
elif marks>=60 and marks<70:
    print("Grade B")
elif marks>=50 and marks<60:
    print("Grade c+")
elif marks>=40 and marks<50:
    print("Grade c")
elif marks>=30 and marks<40:
    print("Grade D")
elif marks>=20 and marks<30:
    print("Grade E")
else:
    print("Fail")
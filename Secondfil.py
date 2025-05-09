a= int(input("Enter your mark:"))
if a < 33:
    print("Your have failed in the exam")
elif 33<=a<40:
    print("You have obtained D grade ")  
elif 40<=a<50:
    print("You have obtained C grade")
elif 50<=a<60:
    print("You have obtained B grade")
elif 60<=a<70:
    print("You have obtained A-")
elif 70<=a<80:
    print("You have obtained A grade ")
elif 80<=a<=100:
    print("You have obtained A+")
else:
    print("Your result is not valid")

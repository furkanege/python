import time
import sys

while True:
    height = float(input("Your Height: "))
    weight = float(input("Your Weight: "))
    bmi = (weight/(height**2))
    print("Your BMI is Calculating...")
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    print("\n")
    time.sleep(0.5)
    if bmi <= 18.50:
        print("Your Status: Underweight",'\n',"Your BMI:",'',round(bmi, 2),'\n')
    elif bmi >= 18.60 and bmi <= 24.99:
        print("Your Status: Normal",'\n',"Your BMI:",'',round(bmi, 2),'\n')
    elif bmi >= 25.00 and bmi <= 29.99:
        print("Your Status: Overweight",'\n',"Your BMI:",'',round(bmi, 2),'\n')
    elif bmi >= 30.00 and bmi <= 34.99:
        print("Your Status: Obese",'\n',"Your BMI:",'',round(bmi, 2),'\n')
    elif bmi >= 35.00 and bmi <= 39.99:
        print("Your Status: Obese II",'\n',"Your BMI:",'',round(bmi, 2),'\n')
    else:
        print("Your Status: Obese III",'\n',"Your BMI:",'',round(bmi, 2),'\n')
        break
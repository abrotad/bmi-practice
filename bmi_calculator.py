
print("Welcome to BMI calculator!")

weight = 80
height = 1.8

bmi = float(weight) / (float(height) ** 2)
# bmi = weight / height * height
bmi = round(bmi, 1)  # return the result into the nearest round number
print(bmi)

if bmi <= 18.5:
    print(f"your BMI is {bmi}. You are Underweight. ")
    # another way to print( string formatting)
    print("Your BMI is {}. You are Underweight. ".format(bmi))
elif 18.5 < bmi <= 25:
    print(f"Your BMI is {bmi}. You are Normal. ")
elif 25 < bmi <= 30:
    print(f"Your BMI is {bmi}. You are Overweight. ")
else:
    print(f"Your BMI is {bmi}. You are Obese. ")
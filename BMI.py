weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", (bmi))

if bmi > 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif 18 <= bmi <= 25:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")

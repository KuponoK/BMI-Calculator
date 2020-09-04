print("Welcome to Po's BMI Calculator!")

#get height and weight of user
weight = float( input("What is your weight in pounds? ") )
height = float( input("What is your height in inches? ") )

#calculate BMI
weight_in_kg = weight * 0.45359237
height_in_meters = height * 0.0254
bmi = (weight_in_kg) / (height_in_meters**2)
print("Your BMI is "+ str(bmi) )
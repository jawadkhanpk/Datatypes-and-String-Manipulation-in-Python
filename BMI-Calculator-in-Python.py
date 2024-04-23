# BMI Body Mass Index Calculator in Python
# BMI Formula: weight / height^2

weight = input("Enter Your Weight: ")
height = input("Enter Your Height: ")

bmi = int(weight) / float(height) ** 2

bmi_as_string = str(bmi)

print("Your BMI is: "+bmi_as_string)
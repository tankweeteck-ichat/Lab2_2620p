def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    #Add code here to calculate BMI
    bmi = weight / (height * height)
    #Add code here to display calculate BMI
    print("BMI = ", f"{bmi:.2f}")
    if bmi<18.5:
        print("Under Weight")
    elif bmi>25.0:
        print("Over Weight")
    else:
        print("Normal Weight")


print("=====================")
calculate_bmi(weight=27, height=1.73)
print("=====================")
calculate_bmi(weight=57, height=1.73)
print("=====================")
calculate_bmi(weight=97, height=1.73)
print("=====================")

print("""I will tell you the number of chocolate bars you need to eat to maintain
your basal metabolic rate.""")

height = input("Please enter your height in inches: ")
height = int(height)

weight = input("Please enter your weight in pounds: ")
weight = int(weight)

age = input("Please enter your age in years: ")
age = int(age)

BMR_Female = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age) #BMR equation for female

BMR_Male = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age) #BMR equation for male

Num_choco_F = BMR_Female//214 #Number of chocolate bars for female

Num_choco_M = BMR_Male//214 #Number of chocolate bars for male

print("""If you are a male, the number of chocolate bars you must
eat to maintain your basal metabolic rate is:""", Num_choco_M,
"""
If you are female, the number of chocolate bars you must eat
to maintain your metabolic rate is:""", Num_choco_F)

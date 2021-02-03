# bmi
# author:paulmcgrath
# calculates someones body mass index
# note convert str to int using int()
height = int(input ('what is your height in cm?: '))
weight = int(input ('what is your weight in kg: '))
BMI = weight / height
print ('your BMI is {}' .format(BMI))
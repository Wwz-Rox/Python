# age = int(input("input your age:"))
# if age >= 18:
#     print("your age is", age,"\nadult")
# else:
#     print('''your age is %d
# teenager''' %age)

weight = float(input("input your weight:"))
height = float(input("input your height:"))
bmi = weight/(height*height)
if bmi < 18.5:
    print("过轻")
elif bmi >= 18.5 and bmi <= 25:
    print("正常")
elif bmi > 28 and bmi <= 32:
    print("肥胖")
else:
    print("过度肥胖")
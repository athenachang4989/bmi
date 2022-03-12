height = input('請輸入尼的身高(cm)：')
weight = input('再輸入尼的體重(kg)：')
height = float(height)
weight = float(weight)
height = height / 100
bmi = weight / ( height * height )
print('尼的BMI是：', bmi)
if bmi < 18.5:
    print('尼的BMI是：', bmi, '你的體重過輕哦！')
elif bmi >= 18.5 and bmi < 24:
    print('尼的BMI是：', bmi, '你的體重正常拉～～')
elif bmi >= 24 and bmi < 27:
    print('尼的BMI是：', bmi, '你過重耶')
elif bmi >= 27 and bmi < 30:
    print('尼的BMI是：', bmi, '輕度肥胖！')
elif bmi >= 30 and bmi < 35:
    print('尼的BMI是：', bmi, '中度肥胖！！')
else:
    print('尼的BMI是：', bmi, '重度肥胖！！！')
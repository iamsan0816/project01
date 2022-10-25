height = float(input('請輸入身高(公分)\n'))  # 1
weight = float(input('請輸入體重(公斤)\n'))  # 2

# bmi的計算公式中,身高使用的是公尺,但我們用公分
height /= 100  # 4

bmi = weight / height**2  # 3 bmi的計算公式
bmi = round(bmi, 1)  # 4 計算到小數點第一位
print(f'您的BMI是:{bmi}')

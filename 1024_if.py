
'''
if 今天下雨:
    我就搭捷運上班
else:
    我就騎車上班

今天下雨電腦會看不懂,所以要創建一個變數

is_rainy = False
if is_rainy:
    print('我就搭捷運上班')
else:
    print('我就騎車上班')


score = 50

if score >= 60:  # 你考試分數大於60分
    print('請你吃大餐')
else:
    print('回家跪算盤')


name = '林鮭魚'

if name != '賈斯汀':
    print('鮭魚免費吃到飽')
else:
    print('付錢')
'''

A1 = int(input('請輸入一個整數\n'))

if A1 % 2 == 0:  # 一個數字除以2沒有餘數,相等於0,就代表是偶數
    print('偶數')
else:
    print('奇數')

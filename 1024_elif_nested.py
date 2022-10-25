# elif(否則如果) .nested if(巢狀 if)
'''
如果  你的分數>90:
      我就給你100元
否則如果  你的分數>80:
      我就給你50元
否則如果  你的分數>70:
      我就給你30元
否則:
    你給我100元
'''
score = 80
if score > 90:
    print('給你100元')
elif score > 80:
    print('給你50元')
elif score > 70:
    print('給你30元')
else:
    print('給我100元')

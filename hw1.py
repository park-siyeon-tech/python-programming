def get_radius(prompt):
    r = int(input(prompt))
    return r


def get_circle_area(radius):
    s=radius*radius*3.14
    answer='반지름이 '+ str(radius)+'인 원의 넓이 = '+str(radius)+" X "+str(radius)+" X 3.14 = "+str(s)
    return  answer

#==================================================================
print('시작합니다')
input_radius ="넓이를 구하고자 하는 원의 반지름은?"
Rresult= get_radius(input_radius)
Sresult=get_circle_area(Rresult)
print(Sresult)
print('종료합니다')

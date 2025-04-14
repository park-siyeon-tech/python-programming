num= input('세자리 정수 입력: ')

def read_single_digit(n):
    if n == '1' :
        return '일'
    elif n == '2' :
        return '이'
    elif n == '3' :
        return '삼'
    elif n == '4' :
        return '사'
    elif n == '5' :
        return '오'
    elif n == '6' :
        return '육'
    elif n == '7' :
        return '칠'
    elif n == '8' :
        return '팔'
    elif n == '9' :
        return '구'
    elif n == '0' :
        return '영'
    
def read_number(number):
    print(read_single_digit(number[0]), read_single_digit(number[1]), read_single_digit(number[2]))
    


read_number(num)

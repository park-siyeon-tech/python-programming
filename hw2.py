
def get_integer(prompt):
    res=int(input(prompt))
    return res

def exchange(won):

    c500=won // 500  
    won %= 500

    c100=won // 100  
    won %= 100

    c50=won // 50    
    won %= 50

    c10=won // 10   
    won %= 10

    print("500원 동전의 개수:",c500)
    print("100원 동전의 개수:",c100)
    print("50원 동전의 개수:",c50)
    print("10원 동전의 개수:",c10)
    



money=get_integer("동전으로 교환하고자 하는 금액은?:")
exchange(money)

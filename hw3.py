
def get_fixed_price(discount,discount_price):
    regular_price=discount_price/(1-discount/100)
    return regular_price
    
discount_rate=int(input('할인율은?:'))
A_discount_price=int(input('A 상품의 할인된 가격은?:'))
B_discount_price=int(input('B 상품의 할인된 가격은?:'))


A_regular_price=get_fixed_price(discount_rate,A_discount_price)
B_regular_price=get_fixed_price(discount_rate,B_discount_price)

print('A 상품의 정가는?:',A_regular_price,'원')
print('B 상품의 정가는?:',B_regular_price,'원')

shopping_bag = {}
print('[구입]')
while True:
    item = input("\n상품명? ")
    if item == "":
        break

    quantity = int(input("수량은? "))
    
    if item in shopping_bag:
        shopping_bag[item] += quantity 
    else:
        shopping_bag[item] = quantity 
    
    print(f"장바구니에 {item} {quantity}개가 담겼습니다.")


print("\n>>> 장바구니 보기:", shopping_bag)


search_item = input("\n[검색]\n장바구니에서 확인하고자 하는 상품은? ")

if search_item in shopping_bag:
    print(f"{search_item}은(는) {shopping_bag[search_item]}개 담겨 있습니다.")
else:
    print(f"{search_item}은 장바구니에 없습니다.")

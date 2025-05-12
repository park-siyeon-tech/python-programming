def buy(shopping_bag):
    print("[구입]")
    product = input("상품명? ").strip()


    if product == "":
        return False

    try:
        quantity = int(input("수량은? ").strip())
    except ValueError:
        print("⚠ 수량은 숫자로 입력되어야 합니다.")
        return True

    if product in shopping_bag:
        shopping_bag[product] += quantity
    else:
        shopping_bag[product] = quantity

    print(f"장바구니에 {product} {quantity}개가 담겼습니다.")
    return True


def show(shopping_bag):
    print(f">>> 장바구니 보기: {shopping_bag}")


def find(shopping_bag):
    print("[검색]")
    product = input("장바구니에서 확인하고자 하는 상품은? ").strip()

    if product in shopping_bag:
        print(f"{product}(는) {shopping_bag[product]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {product}은(는) 없습니다.")



shopping_bag = {}


while True:
    if buy(shopping_bag) == False:
        break


show(shopping_bag)


find(shopping_bag)
find(shopping_bag)

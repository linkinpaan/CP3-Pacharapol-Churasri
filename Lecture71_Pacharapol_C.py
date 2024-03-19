menuList = []
menuprice = []
def showBill():
    print("---My Food---")
    for number in range(len(menuList)):
        print(menuList[number],menuprice[number])
    print("Total Price >>>",sum(menuprice))
while True:
    menuname = input("Menu : ")
    if menuname.lower() == "exit":
        break
    else:
        price = int(input("Price : "))
    menuList.append(menuname)
    menuprice.append(price)
showBill()




systemMenu = {"ต้มยำ":150,"แกงส้มกุ้ง":200,"ปลาทอด":400,"กุ้งอบวุ้นเส้น":450}
menuList = []
def showBill():
    totalprice = 0
    print("---My Food---")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalprice += menuList[number][1]
    print("Total Price :",totalprice)

while True:
    menuname = input("Menu : ")
    if menuname.lower() == "exit":
        break
    else:
        menuList.append([menuname,systemMenu[menuname]])
showBill()
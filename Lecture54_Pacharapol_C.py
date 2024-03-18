def login():
    usernameinput = ""
    pwinput = ""
    while usernameinput != "linkinpaan" or pwinput != "123456":
        usernameinput = input("username : ")
        pwinput = input("password : ")
    selectMenu()
def selectMenu():
    print("----My Shop---")
    print("1. Vat calculator")
    print("2. Price calculator")
    menuList()
def menuList():
    userselect = 0
    while userselect !=1 and userselect !=2 :
        userselect = int(input("Select Menu : "))
        if userselect == 1 :
            print("Vat >>>",vatcal(int(input("Price : "))),"THB")
        elif userselect == 2:
            print("Total Price >>>",pricecal(),"THB")
        else :
            print("Out of menu selection Try Again!!")
def vatcal(totalprice):
    return totalprice*7/100
def pricecal():
    price1 = int(input("Price 1 : "))
    price2 = int(input("Price 2 : "))
    result = price1+price2+vatcal(price1+price2)
    return result
login()
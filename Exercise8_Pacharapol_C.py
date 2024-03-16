username = input("Username : ")
pw = input("Password : ")
potato = 5
coconut = 20
mangosteen = 25
durian = 100
price = 0
if username == "admin" and pw == "123456" :
    print("Hello Admin")
    print("-------------------")
    print("Product list")
    print("1.Potato",5,"THB")
    print("2.Coconut", 20, "THB")
    print("3.Mangosteen", 25, "THB")
    print("4.Durian", 100, "THB")
    print("-------------------")
    inputproduct = int(input("Select Product : "))
    if inputproduct == 1 :
       inputqty = int(input("Quantity ? : "))
       price += potato*inputqty
    elif inputproduct == 2 :
        inputqty = int(input("Quantity ? : "))
        price += coconut * inputqty
    elif inputproduct == 3 :
        inputqty = int(input("Quantity ? : "))
        price += mangosteen * inputqty
    elif inputproduct == 4 :
        inputqty = int(input("Quantity ? : "))
        price += durian * inputqty
    else :
        print ("Product not found")
    print (">Total :",price,"THB")
else :
    print("Check your Username & Password")

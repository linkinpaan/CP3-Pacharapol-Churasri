def vatcalculate():
    total = int(input("Total price (THB) : "))
    result = total+(total*7/100)
    return result
print(vatcalculate())
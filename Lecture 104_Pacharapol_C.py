class customer:
    name =""
    lastname =""
    age =0

    def addCart(self):
        print("Added Product to",self.name,self.lastname,"'s cart")

c01 = customer()
c01.name = "Paan"
c01.lastname = "Jackson"
c01.age = 28
c01.addCart()

c02 = customer()
c02.name = "Mind"
c02.lastname = "Rose"
c02.age = 30
c02.addCart()

c03 = customer()
c03.name = "Yoker"
c03.lastname = "Hunt"
c03.age = 33
c03.addCart()

c04 = customer()
c04.name = "Peem"
c04.lastname = "Joy"
c04.age = 25
c04.addCart()
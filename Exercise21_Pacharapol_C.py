from tkinter import *

def leftClick(event):
    Result = round(float(textBOxWeight.get())/(float(textBoxHeight.get())/100)**2,2) #หาร100 : แปลงเซนเป็นเมตร
    print(Result)
    labelResult.configure(text=Result) #แสดงค่า BMI ที่คำนวณในโปรแกรม

    if Result >= 30 :
        labelDescript.configure(text="อ้วนมาก ลดน้ำหนักด่วนน!!")
    elif 25 <= Result <= 29.9 :
        labelDescript.configure(text="อ้วนระยะเริ่มต้น")
    elif 23 <= Result <= 24.9 :
        labelDescript.configure(text="เริ่มมีน้ำมีนวล")
    elif 18.6 <= Result <= 22.9 :
        labelDescript.configure(text="หุ่นดีสมส่วน")
    else :
        labelDescript.configure(text="ผอมเกิ๊นน กินเยอะๆหน่อย")


mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(mainWindow,text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBOxWeight = Entry(mainWindow)
textBOxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text="คำนวณ BMI")
calculateButton.grid(row=2,column=0)
calculateButton.bind("<Button-1>",leftClick)
labelResult = Label(mainWindow,text="Key your Weight & Height",font=("Kanit",20),fg="red")
labelResult.grid(row=2,column=1)
labelDescript = Label(mainWindow,text="",font=("Kanit",20),fg="red")
labelDescript.grid(row=3,column=1)

mainWindow.mainloop()


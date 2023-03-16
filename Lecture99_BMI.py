from tkinter import *
import math


def leftClickButton(event):
    print(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100,2))
    labelResult.configure(text=float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))

    bmi = format(float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2))
    bmiShow = ""

    if float(bmi) <= 18.5:
        bmiShow = "ผอมเกินไป(น้อยกว่า 18.5) : น้ำหนักน้อยกว่าปกติก็ไม่ค่อยดี หากคุณสูงมากแต่น้ำหนักน้อยเกินไป อาจเสี่ยงต่อการได้รับสารอาหารไม่เพียงพอหรือได้รับพลังงานไม่เพียงพอ ส่งผลให้ร่างกายอ่อนเพลียง่าย การรับประทานอาหารให้เพียงพอและออกกำลังกายแบบเวทเทรนนิ่งเพื่อเสริมสร้างกล้ามเนื้อ สามารถช่วยเพิ่มค่า BMI ให้อยู่ในเกณฑ์ปกติได้"

    elif float(bmi) > 18.5 and float(bmi) <= 22.9:
        bmiShow = "ปกติ(18.6 - 22.9) : น้ำหนักที่เหมาะสมสำหรับคนไทยคือค่า BMI ระหว่าง 18.5-22.9 จัดอยู่ในเกณฑ์ปกติ ห่างไกลโรคที่เกิดจากความอ้วน และมีความเสี่ยงต่อการเกิดโรคต่าง ๆ น้อยที่สุด ควรพยายามรักษาระดับค่า BMI ให้อยู่ในระดับนี้ให้นานที่สุด"

    elif float(bmi) >= 23 and float(bmi) <= 24.9:
        bmiShow = "ท้วม(23.0 - 24.9) : พยายามอีกนิดเพื่อลดน้ำหนักให้เข้าสู่ค่ามาตรฐาน เพราะค่า BMI ในช่วงนี้ยังถือว่าเป็นกลุ่มผู้ที่มีความอ้วนอยู่บ้าง แม้จะไม่ถือว่าอ้วน แต่หากประวัติคนในครอบครัวเคยเป็นโรคเบาหวานและความดันโลหิตสูง ก็ถือว่ายังมีความเสี่ยงมากกว่าคนปกติ"

    elif float(bmi) >= 25 and float(bmi) <= 29.9:
        bmiShow = "อ้วน(25.0 - 29.9) : คุณอ้วนในระดับหนึ่ง ถึงแม้จะไม่ถึงเกณฑ์ที่ถือว่าอ้วนมาก ๆ แต่ก็ยังมีความเสี่ยงต่อการเกิดโรคที่มากับความอ้วนได้เช่นกัน ทั้งโรคเบาหวาน และความดันโลหิตสูง"

    elif float(bmi) >= 30:
        bmiShow = "อ้วนมาก(30.0 ขึ้นไป) : ค่อนข้างอันตราย เพราะเข้าเกณฑ์อ้วนมาก เสี่ยงต่อการเกิดโรคร้ายแรงที่แฝงมากับความอ้วน หากค่า BMI อยู่ในระดับนี้ จะต้องระวังการรับประทานไขมัน และควรออกกำลังกายอย่างสม่ำเสมอ และหากเลขยิ่งสูงกว่า 40.0 ยิ่งแสดงถึงความอ้วนที่มากขึ้น"

    labelResult.configure(text=bmiShow)


MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง(cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow, text="น้ำหนัก(kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="ผลลัพธ์")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ดัชนีมวลกาย(BMI)")
labelResult.grid(row=2, column=1)

MainWindow.mainloop()
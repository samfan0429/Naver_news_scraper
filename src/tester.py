from tkinter import *
from PIL import ImageTk,Image
import os
import newscraper

# class searchInfo():
#     def __init__(self, keys,):
        


def main():
    root = Tk()
    root.title('Naver News-craper')
    root.geometry('700x400')
    root.configure(borderwidth="1")

    testVar = StringVar(value='2020.8.2')
    font_set = ('Arial',12)
    font_title = ('Arial',26)

    title = Label(root, text = "네이버 뉴스-크래이퍼",font=font_title)
    title.pack(pady=30)

    inputs = Frame(root,padx=10,pady=10,borderwidth = 2,relief="groove")

    searchFrame = Frame(inputs,padx=10,pady=5)
    label1 = Label(searchFrame, text = "검색창 키워드를 입력해주세요: ",font=font_set)
    search_keys = Entry(searchFrame, width=20,borderwidth=5,font=font_set)


    dateFrame = Frame(inputs,padx=10,pady=5)
    label2 = Label(dateFrame, text = "날짜 범위를 입력해주세요: ",font=font_set)
    dateStart = Entry(dateFrame, textvariable=testVar,width=8,borderwidth=5,font=font_set)
    dateEnd = Entry(dateFrame, textvariable=testVar,width=8,borderwidth=5,font=font_set)
    wave = Label(dateFrame, text = "~",width=3,font=font_set)


    searchFrame.grid_columnconfigure((0,3), weight=1)
    label1.grid(row=0, column=0)
    search_keys.grid(row=0, column=1,sticky="ew")

    dateFrame.grid_columnconfigure((0,5), weight=1)
    label2.grid(row=1,column=0,pady=(20,0))
    dateStart.grid(row=1, column=1,pady=(20,0))
    wave.grid(row=1,column=2,pady=(20,0))
    dateEnd.grid(row=1, column=3,pady=(20,0))

    inputs.pack(pady=30)
    searchFrame.pack()
    dateFrame.pack()

    # top = Toplevel()
    # lbl = Label(top,text="Hello World").pack()

    root.mainloop()

if __name__=="__main__":
    main()
'''
    File name: test.py
    Author: Peter Test
    Date created: 4/20/2013
    Date last modified: 4/25/2013
    Python Version: 2.7
'''

from tkinter import *
from PIL import ImageTk,Image
import os
from datetime import date
import time

from newscraper import Scraper 
import format_Checker as fc
from output import UserInput 

def debugDic(dic):
    vals = dic.values()
    for v in vals:
        print(v.get())

def addToday(start_date,end_date):
    start_date.configure(textvariable=StringVar(value=date.today().strftime("%Y.%m.%d")))
    end_date.configure(textvariable=StringVar(value=date.today().strftime("%Y.%m.%d")))

class MainApp(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.parent.title('Naver News-craper')
        self.parent.geometry('700x470')    
        self.parent.configure(borderwidth="1")

        self.scraper = Scraper()
        self.font_set = ('Arial',12)

        self.WarningAdded = False

        self.track={}

        title = Label(self, text = "네이버 뉴스-크래이퍼",font=('Arial',26))
        title.pack(pady=25)

        self.inputs = Frame(self,padx=10,pady=10,borderwidth = 2,relief="groove")

        # Add search keys
        self.Create_one_inputs("검색 URL을 입력해주세요: ", 'keys')

        # Create a section for narrowing dates
        # self.CreateDate("날짜 범위를 입력해주세요: ",'start_date','end_date')

        # Add input for output file name
        self.Create_one_inputs("파일명을 영어로 입력해주세요 (빈칸없음): ", 'name')

        self.inputs.pack(pady=30)

        self.setRun()
        
    def Create_one_inputs(self,title, key):
        new_frame = Frame(self.inputs,padx=10,pady=5)
        label = Label(new_frame, text = title,font=self.font_set)
        value = Entry(new_frame, width=20,borderwidth=5,font=self.font_set)
        self.track[key]=value

        new_frame.grid_columnconfigure((0,3), weight=1)
        label.grid(row=0, column=0,pady=(10,10))
        value.grid(row=0, column=1,sticky="ew",pady=(10,10))
        new_frame.pack()

    def CreateDate(self,title, key1,key2):
        new_frame = Frame(self.inputs,padx=10,pady=5)
        label = Label(new_frame, text = title,font=self.font_set)
        input1 = Entry(new_frame,width=10,borderwidth=5,font=self.font_set)
        input2 = Entry(new_frame,width=10,borderwidth=5,font=self.font_set)
        wave = Label(new_frame, text = "~",width=3,font=self.font_set)

        self.track[key1]=input1
        self.track[key2]=input2

        today = Button(new_frame, text='오늘',command= lambda: addToday(self.track['start_date'],self.track['end_date']))

        new_frame.grid_columnconfigure((0,5), weight=1)
        label.grid(row=0,column=0,pady=(10,10))
        input1.grid(row=0, column=1,pady=(10,10))
        wave.grid(row=0,column=2,pady=(10,10))
        input2.grid(row=0, column=3,pady=(10,10))
        today.grid(row=0, column=4,pady=(10,10))
        new_frame.pack()

    def setRun(self):
        run = Button(self, text='실행하기',command= lambda: self.checkNRun())
        run.pack()

    def checkNRun(self):
        passed = fc.check(self.track)
        if passed == False:
            self.setWarning()
        else:
            self.TurnOffWarning()
            UInput = UserInput(self.track)
            self.winfo_children()[len(self.winfo_children())-1]['state'] = 'disabled'
            # status = Label(self, text = "실행중...",font=self.font_set)
            # status.pack()
            self.scraper.activate(UInput)
            self.winfo_children()[len(self.winfo_children())-1]['state'] = 'normal'
            # self.winfo_children()[len(self.winfo_children())-1].destroy()

    def setWarning(self):
        if self.WarningAdded==False:
            warning = Label(self, text = "입력 양식 문제",font=self.font_set,fg='#f00')
            warning.pack()
            self.WarningAdded = True

    def TurnOffWarning(self):
        if self.WarningAdded == True:
            self.winfo_children()[len(self.winfo_children())-1].destroy()
            self.WarningAdded = False

def main():
    root = Tk()

    MainApp(root).pack(side="top", fill="both", expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    main()
from tkinter import *
from PIL import ImageTk,Image
import os
import newscraper

def debugDic(dic):
    vals = dic.values()
    for v in vals:
        print(v.get())

class output():
    def __init__(self,dic_inputs):
        self.searchKey = dic_inputs['keys']
        self.dateStart = dic_inputs['']

def check(app):
    

class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.parent.title('Naver News-craper')
        self.parent.geometry('700x450')    
        self.parent.configure(borderwidth="1")
        
        self.font_set = ('Arial',12)

        self.track={}

        title = Label(self, text = "네이버 뉴스-크래이퍼",font=('Arial',26))
        title.pack(pady=25)

        self.inputs = Frame(self,padx=10,pady=10,borderwidth = 2,relief="groove")

        # Add search keys
        self.Create_one_inputs("검색창 키워드를 입력해주세요: ", 'keys')

        # Create a section for narrowing dates
        self.CreateDate("날짜 범위를 입력해주세요: ",'start_date','end_date')

        # Add input for output file name
        self.Create_one_inputs("파일명을 입력해주세요 (영어로): ", 'name')

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
        input1 = Entry(new_frame,width=8,borderwidth=5,font=self.font_set)
        input2 = Entry(new_frame,width=8,borderwidth=5,font=self.font_set)
        wave = Label(new_frame, text = "~",width=3,font=self.font_set)

        self.track[key1]=input1
        self.track[key2]=input2
        
        new_frame.grid_columnconfigure((0,5), weight=1)
        label.grid(row=1,column=0,pady=(10,10))
        input1.grid(row=1, column=1,pady=(10,10))
        wave.grid(row=1,column=2,pady=(10,10))
        input2.grid(row=1, column=3,pady=(10,10))
        new_frame.pack()

    def setRun(self):
        run = Button(master=self, text='실행하기',command= lambda: check(self.track))
        run.pack()


def main():
    root = Tk()

    MainApplication(root).pack(side="top", fill="both", expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    main()
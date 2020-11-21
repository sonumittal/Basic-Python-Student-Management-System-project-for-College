from tkinter import *
root=Tk()
root.title("GUI")
root.geometry('400x400')

f=Frame(root,bg='black',height=100,width=300,center).grid(row=1,columnspan=5)
Label(f,text='1',bg='red',fg='yellow').grid(row=0,columnspan=3)
##f.pack(side=TOP,fill=BOTH,expand=YES)
##l1.pack(side=TOP,fill=BOTH)
##
##f1=Frame(root)
##f1.pack(side=TOP,fill=BOTH)
##l2=Label(f1,text='2',bg='blue',fg='yellow')
##l2.pack(side=LEFT,fill=BOTH)
##l3=Label(f1,text='3',bg='black',fg='yellow')
##l3.pack(side=TOP,fill=BOTH)
##l4=Label(f1,text='4',bg='green',fg='yellow')
##l4.pack(side=TOP,fill=BOTH)
##
##f2=Frame(root)
##f2.pack(side=TOP,fill=BOTH)
##f3=Frame(f2)
##f3.pack(side=LEFT,fill=Y)
##l5=Label(f2,text='5',bg='white',fg='yellow')
##l5.pack(side=TOP,fill=BOTH)
##l6=Label(f2,text='6',bg='blue',fg='yellow')
##l6.pack(side=BOTTOM,fill=BOTH)
##
##f4=Frame(f2)
##f4.pack(side=LEFT,fill=BOTH)
##l7=Label(f3,text='7',bg='green',fg='yellow')
##l7.pack(side=RIGHT,fill=Y)
##l8=Label(f3,text='8',bg='red',fg='yellow')
##l8.pack(side=LEFT,fill=X)
##l9=Label(f3,text='9',bg='white',fg='yellow')
##l9.pack(side=LEFT,fill=X)
##root.mainloop()
##

##from tkinter import *
##
##root = Tk()
##root.title('GUI')
##root.resizable(width=FALSE, height=FALSE)
##root.geometry('460x350')
##
##f = Frame(root, width = 450, height=50, pady=3).grid(row=0, columnspan=3)
##Label(f, text = '1').grid(row = 0, columnspan = 3)
##Label(top_frame, text = 'Width:').grid(row = 1, column = 0)
##Label(top_frame, text = 'Length:').grid(row = 1, column = 2)
##entry_W = Entry(top_frame).grid(row = 1, column = 1)
##entry_L = Entry(top_frame).grid(row = 1, column = 3)
###Label(top_frame, text = '').grid(row = 2, column = 2)
##
##center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3).grid(row=1, columnspan=3)
##ctr_left = Frame(center, bg='blue', width=100, height=190).grid(column = 0, row = 1, rowspan = 2)
##ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3).grid(column = 1, row=1, rowspan=2)
##ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3).grid(column = 2, row=1, rowspan=2)
##
##btm_frame = Frame(root, bg='white', width = 450, height = 45, pady=3).grid(row = 3, columnspan = 3)
##btm_frame2 = Frame(root, bg='lavender', width = 450, height = 60, pady=3).grid(row = 4, columnspan = 3)
##
##
##root.mainloop()

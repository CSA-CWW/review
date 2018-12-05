from tkinter import *
from tkinter import ttk
import glob
root = Tk()
def read():         #read command#
    try:
        o = open(str(optvar.get()),'r')
        read = o.read() 
        m.configure(text=read)
    except:
        m.configure(text='File not found!')
    
optvar = StringVar() #option combo box#
option = ttk.Combobox(root,text='', textvariable = optvar, state="readonly",width=15)

val_list = []
for val in glob.glob('*.txt'):
    val_list.append(val) #adds files in folder to combobox#
option['values'] = val_list

l = Label(root, text='Message:')
m = Message(root, text='\nNothing here for now...\n', width=200,borderwidth=2, relief="groove")
b = Button(root, text='Read Text',command=read, width=10, height=1)

b.grid(row=4,column=0,sticky='NSEW')
option.grid(row=3,column=0, sticky='NSEW')
m.grid(row=2,column=0, sticky='NSEW')
l.grid(row=1,column=0, sticky='NSEW')

root.grid_columnconfigure(0, weight=2)
root.grid_rowconfigure(2, weight=1)

#cameron watts#
#comp prog#
#12 4 18#

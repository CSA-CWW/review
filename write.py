from tkinter import *
from tkinter import ttk
import tkinter
import glob
root = Tk()
def read():         #read command#
    try:
        o = open(str(optvar.get()),'r')
        read = o.read()
        m.configure(state=NORMAL)
        m.delete('1.0', END)
        m.insert(INSERT,read)
        m.configure(state=DISABLED)
    except:                    #reads file#
        m.configure(state=NORMAL)
        m.delete('1.0', END)
        m.insert(INSERT,'File not found!')
        m.configure(state=DISABLED)
        
def write():
    try:
        o = open(str(optvar.get()),'w')
        value = t.get('1.0',END)
        o.write(t.get('1.0',END))
        print (t.get(END))
        
        m.configure(state=NORMAL)
        m.delete('1.0', END)
        m.insert(INSERT,'File updated!')            #configures text box when writing#
        m.configure(state=DISABLED)
        o.close()
    except:
        m.configure(state=NORMAL)
        m.delete('1.0', END)
        m.insert(INSERT,'File not found!')
        m.configure(state=DISABLED)
        
optvar = StringVar() #option combo box#
option = ttk.Combobox(root,text='', textvariable = optvar, state="readonly",width=15)

val_list = []
for val in glob.glob('*.txt'):
    val_list.append(val) #adds files in folder to combobox#
option['values'] = val_list


ml = Label(root, text='Read')
wl = Label(root, text='Write')

m = Text(root, width = 25, height = 20)
m.insert(INSERT,'Nothing here right now...')
m.configure(state=DISABLED)

t = Text(root, width = 25, height = 20)
t.insert(INSERT,'Insert text here...')


b = Button(root, text='Read Text',command=read, width=10, height=1)
bw = Button(root, text='Write Text',command=write, width=10, height=1)


b.grid(row=4,column=0,sticky='NSEW')
bw.grid(row=4,column=1,sticky='NSEW')
option.grid(row=3,column=0, sticky='NSEW', columnspan=4)

ml.grid(row=1,column=0)
wl.grid(row=1,column=1)
m.grid(row=2,column=0, sticky='NSEW')
t.grid(row=2,column=1,sticky='NSEW')

root.grid_columnconfigure(0, weight=2)
root.grid_rowconfigure(2, weight=1)

#cameron watts#
#comp prog#
#12 4 18#

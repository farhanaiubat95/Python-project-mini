from tkinter import *

# Function for command


def click(symbol):
    if symbol == 'C':
        val = entryField.get()
        val = val[0:len(val)-1]
        entryField.delete(0, END)
        entryField.insert(0, val)


# GUI Design
root = Tk()
root.title('Scientific Calculator')
root.config(bg='gray1', padx=10, pady=20)
root.geometry('430x580+100+100')

# Entry field
entryField = Entry(root, font=('arial', 20, 'bold'),
                   width=10, bg='gray9', fg='white', bd=10, relief='raised')
entryField.grid(row=0, column=0, sticky='n'+'s'+'e'+'w', columnspan=4)

# Mic Image
micImg = PhotoImage(file='mic1.png')
micBtn = Button(root, image=micImg,
                activebackground="gray19", bd=0, bg='gray1')
micBtn.grid(row=0, column=4, columnspan=1)

# Button Text List
button_text_list1 = ["C", "CE", ".", "=", ","]
button_text_list2 = ["7", "8", "9",
                     "4", "5", "6",
                     "1", "2", "3",
                     "0", "√", "%",
                     " cosθ", "tanθ", "sinθ",
                     " cosh", "tanh", "sinh",
                     "x\u02b8", "x\u00B3", "x\u00B2"]
button_text_list3 = ["+", "π",
                     "-", "2π",
                     "*", "(",
                     "/", ")",
                     "ln", "deg",
                     "log10", "rad",
                     "x!", "e"]
# Button
rowVal1 = 1
columnVal1 = 0
for i in button_text_list1:
    btn = Button(root, text=i, font=('arial', 12, 'bold'), width=6, height=1,
                 bd=2, relief='groove', bg='dark goldenrod', fg='black', activebackground='gray14', activeforeground='dark goldenrod',
                 command=lambda btn=i: click(btn))
    btn.grid(row=rowVal1, column=columnVal1, padx=5, pady=10)
    columnVal1 += 1


rowVal2 = 2
columnVal2 = 0
for i in button_text_list2:
    btn = Button(root, text=i, font=('arial', 13, 'bold'), width=6, height=2,
                 bd=3, relief='groove', bg='gray14', fg='SteelBlue3', activebackground='SteelBlue3', activeforeground='gray1',
                 command=lambda btn=i: click(btn))
    btn.grid(row=rowVal2, sticky='n'+'s'+'e'+'w',
             column=columnVal2, padx=5, pady=3)
    columnVal2 += 1
    if columnVal2 > 2:
        rowVal2 += 1
        columnVal2 = 0

rowVal3 = 2
columnVal3 = 3
for i in button_text_list3:
    btn = Button(root, text=i, font=('arial', 13, 'bold'), width=6, height=2,
                 bd=3, relief='groove', bg='DeepSkyBlue4', fg='azure', activebackground='gray19', activeforeground='white',
                 command=lambda btn=i: click(btn))
    btn.grid(row=rowVal3, sticky='n'+'s'+'e'+'w',
             column=columnVal3, padx=5, pady=3)
    columnVal3 += 1
    if columnVal3 > 4:
        rowVal3 += 1
        columnVal3 = 3


root.mainloop()

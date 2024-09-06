from tkinter import *
import math
from pygame import mixer  # mixer module help us to play any sound
import speech_recognition as sr
mixer.init()  # for initialize


# Function for Button command
def click(symbol):
    val = entryField.get()  # input string value
    result = ''

    try:
        if symbol == 'C':
            val = val[0:len(val)-1]
            entryField.delete(0, END)
            entryField.insert(0, val)

        elif symbol == 'CE':
            entryField.delete(0, END)

        elif symbol == 'π':
            result = math.pi

        elif symbol == '2π':
            result = 2 * math.pi

        elif symbol == 'sinθ':
            result = math.sin(math.radians(eval(val)))

        elif symbol == 'tanθ':
            result = math.tan(math.radians(eval(val)))

        elif symbol == 'cosθ':
            result = math.cos(math.radians(eval(val)))

        elif symbol == 'sinh':
            result = math.sinh(eval(val))

        elif symbol == 'tanh':
            result = math.tanh(eval(val))

        elif symbol == 'cosh':
            result = math.cosh(eval(val))

        elif symbol == '√':
            result = math.sqrt(eval(val))

        elif symbol == '∛':
            result = eval(val)**(1/3)

        elif symbol == 'x\u02b8':
            entryField.insert(END, '**')
            return

        elif symbol == 'x\u00B3':
            result = eval(val)**3

        elif symbol == 'x\u00B2':
            result = eval(val)**2

        elif symbol == 'ln':
            result = math.log2(eval(val))

        elif symbol == 'deg':
            result = math.degrees(eval(val))

        elif symbol == 'rad':
            result = math.radians(eval(val))

        elif symbol == 'e':
            result = math.e

        elif symbol == 'log10':
            result = math.log10(eval(val))

        elif symbol == 'rad':
            result = math.factorial(eval(val))

        elif symbol == '/':
            entryField.insert(END, "/")
            return

        elif symbol == '=':
            result = eval(val)

        else:
            entryField.insert(END, symbol)
            return

        entryField.delete(0, END)
        entryField.insert(0, result)

    except SyntaxError:
        pass

# function for mic command calculation


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def mod(a, b):
    return a % b


def lcm(a, b):
    l = math.lcm(a, b)
    return l


def hcf(a, b):
    g = math.gcd(a, b)
    return g


operations_audio = {'ADD': add, 'SUM': add, 'PLUS': add, 'ADDITION': add,
                    'SUBTRACT': sub, 'MINUS': sub, 'SUBTRACTION': sub, 'DIFERENCE': sub,
                    'MULTIPLY': mul, 'MULTIPLICATION': mul, 'PRODUCT': mul,
                    'DIV': div, 'DIVISION': div, 'DIVIDE': div,
                    'MOD': mod, 'MODULUS': mod, 'REMAINDER': mod,
                    'LCM': lcm, 'HCF': hcf}


def findNumber(n):
    l = []
    for num in n:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

# function for mic command


def micAudio():
    mixer.music.load('2-Scientific-calculator/music1.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    m = sr.Microphone()

    with m as mic:
        try:
            audio = r.listen(mic)
            r.adjust_for_ambient_noise(mic, duration=0.2)
            # this duration gap means whatever you speak after 0.2s,it will treat as a next sentence

            # recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            # print(text)
            # print("{}".format(value))

            mixer.music.load('2-Scientific-calculator/music2.mp3')
            mixer.music.play()

            text_split = text.split(' ')
            # print(text_split)
            for word in text_split:
                if word.upper() in operations_audio.keys():
                    n = findNumber(text_split)
                    print(n)
                    result = operations_audio[word.upper()](n[0], n[1])
                    entryField.delete(0, END)
                    entryField.insert(END, result)
                else:
                    pass

        except:
            pass


# GUI Design
root = Tk()
root.title('Scientific Calculator')
root.config(bg='gray1', padx=10, pady=20)
root.geometry('430x580+100+100')

# Entry field
entryField = Entry(root, font=('arial', 20, 'bold'),
                   width=10, bg='gray9', fg='white', bd=10, relief='raised', justify=RIGHT)
entryField.grid(row=0, column=0, sticky='n'+'s'+'e'+'w', columnspan=4)

# Mic Image
micImg = PhotoImage(file='2-Scientific-calculator/mic.png')
micBtn = Button(root, image=micImg,
                activebackground="gray19", bd=0, bg='gray1', command=micAudio)
micBtn.grid(row=0, column=4, columnspan=1)

# Button Text List
button_text_list1 = ["C", "CE", ".", "+", "="]
button_text_list2 = ["7", "8", "9",
                     "4", "5", "6",
                     "1", "2", "3",
                     "0", "√", "∛",
                     " cosθ", "tanθ", "sinθ",
                     " cosh", "tanh", "sinh",
                     "x\u02b8", "x\u00B3", "x\u00B2"]
button_text_list3 = ["-", "π",
                     "*", "2π",
                     "/", "(",
                     "%", ")",
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

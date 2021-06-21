import sys
import tkinter as tk

a = ("-------------------------------------------------------------------------------------------------------------")
instr = ("キーボードで1～3の中から正解だと思う番号を1つ入力してください")
ans = ("正解!!")
diff = ("!入力が間違っています!")

def func1():
    import tkinter as tk
    window2 = tk.Tk()
    window2.title("No.1 answer")
    window2.geometry("400x200")
    
    b = text1.get()
    if b == "1":
        atext1_1 = tk.Label(window2, text='''不正解
答えは2のライオン。ねこはロシア語で"кот(または"кошка")"といいます''')
        atext1_1.pack()
    elif b == "2":
        atext1_2 = tk.Label(window2, text=ans)
        atext1_2.pack()
    elif b == "3":
        atext1_3 = tk.Label(window2, text='''不正解
答えは2のライオン。トラはロシア語で"тигр"といいます''')
        atext1_3.pack()
    else:
        atext1_4 = tk.Label(window2, text=diff)
        atext1_4.pack()
    window2.mainloop()

def func2():
    import tkinter as tk
    window2 = tk.Tk()
    window2.title("No.2 answer")
    window2.geometry("400x200")
    
    b = text2.get()
    if b == "1":
        atext2_1 = tk.Label(window2, text='''不正解
答えは3の心臓。パソコンはロシア語で""といいます''')
        atext2_1.pack()
    elif b == "2":
        atext2_2 = tk.Label(window2, text='''不正解
答えは3の心臓。ロシアはロシア語で"Россия"といいます''')
        atext2_2.pack()
    elif b == "3":
        atext2_3 = tk.Label(window2, text=ans)
        atext2_3.pack()
    else:
        atext2_4 = tk.Label(window2, text=diff)
        atext2_4.pack()
    window2.mainloop()

def func3():
    import tkinter as tk
    window2 = tk.Tk()
    window2.title("No.3 answer")
    window2.geometry("400x200")
    
    b = text3.get()
    if b == "1":
        atext3_1 = tk.Label(window2, text='''不正解
答えは2の駆逐艦。戦艦はロシア語で"линкор"といいます''')
        atext3_1.pack()
    elif b == "2":
        atext3_2 = tk.Label(window2, text=ans)
        atext3_2.pack()
    elif b == "3":
        atext3_3 = tk.Label(window2, text='''不正解
答えは2の駆逐艦。空母はロシア語で""といいます''')
        atext3_3.pack()
    else:
        atext3_4 = tk.Label(window2, text=diff)
        atext3_4.pack()
    window2.mainloop()

def func4():
    import tkinter as tk
    window2 = tk.Tk()
    window2.title("No.4 answer")
    window2.geometry("400x200")
    
    b = text4.get()
    if b == '''ソビエト社会主義共和国連邦''':
        atext4_1 = tk.Label(window2, text=ans)
        atext4_1.pack()
    elif b == '''Union of Soviet Socialist Republics''':
        atext4_2 = tk.Label(window2, text=ans)
        atext4_2.pack()
    elif b == '''union of soviet socialist republics''':
        atext4_3 = tk.Label(window2, text=ans)
        atext4_3.pack()
    elif b == '''Союз Советских Социалистических Республик''':
        atext4_4 = tk.Label(window2, text=ans)
        atext4_4.pack()
    elif b == '''союз советских социалистических республик''':
        atext4_5 = tk.Label(window2, text=ans)
        atext4_5.pack()
    else:
        atext4_6 = tk.Label(window2, text="不正解、または入力が違います")
        atext4_6.pack()
    window2.mainloop()


window1 = tk.Tk()
window1.title("question")
window1.geometry("800x900")

labeltext1_1 = tk.Label(window1, text='''問題1:ロシア語の"лев"とは日本語でどういう意味でしょう?
１:ねこ
2：ライオン
3：トラ''', font=("System", 10))
labeltext1_2 = tk.Label(window1, text=instr, font=("System", 5))
labeltext1_1.pack()
labeltext1_2.pack()

text1 = tk.Entry(window1)
text1.insert(tk.END, 'Plz answer')
text1.pack()

button1 = tk.Button(window1, text="ok", command=func1)
button1.pack()


space1 = tk.Label(window1, text="\n")
line1 = tk.Label(window1, text=a)
space1.pack()
line1.pack()


labeltext2_1 = tk.Label(window1, text='''\n問題2:ロシア語の"сердце"とは日本語でどういう意味でしょう?
1：パソコン
2：ロシア
3：心臓''', font=("System", 10))
labeltext2_2 = tk.Label(window1, text=instr, font=("System", 5))
labeltext2_1.pack()
labeltext2_2.pack()

text2 = tk.Entry(window1)
text2.insert(tk.END, 'Plz answer')
text2.pack()

button2 = tk.Button(window1, text="ok", command=func2)
button2.pack()


space2 = tk.Label(window1, text="\n")
line2 = tk.Label(window1, text=a)
space2.pack()
line2.pack()

labeltext3_1 = tk.Label(window1, text='''\n問題3：ロシア語の"эсминец"とは日本語でどういう意味でしょう?
1：戦艦
2：駆逐艦
3：空母''', font=("System", 10))
labeltext3_2 = tk.Label(window1, text=instr, font=("System", 5))
labeltext3_1.pack()
labeltext3_2.pack()

text3 = tk.Entry(window1)
text3.insert(tk.END, 'Plz answer')
text3.pack()

button3 = tk.Button(window1, text="ok", command=func3)
button3.pack()


space3 = tk.Label(window1, text="\n")
line3 = tk.Label(window1, text=a)
space3.pack()
line3.pack()

labeltext4 = tk.Label(window1, text='''\n問題4:ソ連の正式名称を日本語、英語、ロシア語のいずれかで答えなさい
キーボードで入力しなさい''', font=("System", 10))
labeltext4.pack()

text4 = tk.Entry(window1)
text4.insert(tk.END, 'Plz answer')
text4.pack()

button4 = tk.Button(window1, text="ok", command=func4)
button4.pack()


window1.mainloop()

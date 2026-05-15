import tkinter as tk
import tkinter.font as tkFont

def definice_komponent():
    velky_font = tkFont.Font(family="Arail", size=30)

    label = tk.Label(text="Číslo 1:",font=velky_font)
    label.grid(row=0, column=0)

    ent_1=tk.Entry(font=velky_font,textvariable=edit1_hodn)
    ent_1.grid(row=0,column=1)

    label2 = tk.Label(text="Číslo 2:",font=velky_font)
    label2.grid(row=1, column=0)

    ent_2=tk.Entry(font=velky_font,textvariable=edit2_hodn)
    ent_2.grid(row=1,column=1)

    bt1 = tk.Button(text="Výpočet",font=velky_font,command=pocitani)
    bt1.grid(row=2,column=0)

    label3 = tk.Label(text="Oo=",font=velky_font)
    label3.grid(row=3, column=0)

    labell = tk.Label(text="S=", font=velky_font)
    labell.grid(row=4, column=0)

    lbl_vysl = tk.Label(text="xxxxxxx",font=velky_font,textvariable=vysl_hodn)
    lbl_vysl.grid(row=3, column=1)

    lbl_vysl = tk.Label(text="xxxxxxx", font=velky_font, textvariable=vysl_hodnn)
    lbl_vysl.grid(row=4, column=1)

def pocitani():
    cs1 = int(edit1_hodn.get())
    cs2 = int(edit2_hodn.get())
    global Ss
    global O
    Ss = 0
    O = 0
    Ss = cs1 * cs2
    O = 2*cs1 + 2*cs2
    vysl_hodn.set(O)
    vysl_hodnn.set(Ss)

okno= tk.Tk()
okno.geometry("600x500")
vysl_hodn=tk.StringVar(value="xxxx")
vysl_hodnn=tk.StringVar(value="xxxxp")
edit1_hodn=tk.StringVar(value="2")
edit2_hodn=tk.StringVar(value="2")

definice_komponent()
okno.mainloop()

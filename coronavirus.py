from tkinter import *
import tkinter as tk

program = tk.Tk()

program.title("Coronavirus Tespit Programı")
program.geometry("500x500+580+200")

baslik = Label(text="Coronavirus Tespit", fg="red", bg="#000000", font=("Fixedsys", 25, "bold"))
baslik.pack()
bosluk = Label(text="\n")
bosluk2 = Label(text="\n")

bosluk.pack()
bosluk2.pack()


def sonucAt():
    i = -0.5

    if (tik1_tf.get() == 1):
        i = i + 0.5
    if (tik1_tf.get() == 0):
        i = i - 0.5
    if (tik2_tf.get() == 1):
        i = i + 0.5
    if (tik2_tf.get() == 0):
        i = i - 0.5
    if (tik3_tf.get() == 1):
        i = i + 0.5
    if (tik3_tf.get() == 0):
        i = i - 0.5
    if (tik4_tf.get() == 1):
        i = i + 0.5
    if (tik4_tf.get() == 0):
        i = i - 0.5
    if (tik5_tf.get() == 1):
        i = i + 0.5
    if (tik5_tf.get() == 0):
        i = i - 0.5
    if (tik6_tf.get() == 1):
        i = i + 0.5
    if (tik6_tf.get() == 0):
        i = i - 0.5
    if (tik7_tf.get() == 1):
        i = i + 0.5
    if (tik7_tf.get() == 0):
        i = i - 0.5
    if (tik8_tf.get() == 1):
        i = i + 0.5
    if (tik8_tf.get() == 0):
        i = i - 0.5
    if (tik9_tf.get() == 1):
        i = i + 0.5
    if (tik9_tf.get() == 0):
        i = i - 0.5

    if (i <= -2):
        sonuc.config(text="Nesin sen ?\n 2058 yılından gelen covid-19 aşılı bir zaman yolcusu mu ?",
                     font=("Times", 10, "italic bold"), bg="green")
    if ((i > -2) & (i <= 2)):
        sonuc.config(text="Coronavirus bile bu kadar kararsız değil. \n Git bi doktora görün ne varmış öğren",
                     font=("Times", 10), bg="orange")
    if (i > 2):
        sonuc.config(text="Yakında beyaz bir ışık görünecek.\n Sonra çok sıcak bir yere gideceksin haberin olsun :D",
                     font=("Arial Black", 10, "bold"), bg="red")


tik1_tf = tk.IntVar()
tik2_tf = tk.IntVar()
tik3_tf = tk.IntVar()
tik4_tf = tk.IntVar()
tik5_tf = tk.IntVar()
tik6_tf = tk.IntVar()
tik7_tf = tk.IntVar()
tik8_tf = tk.IntVar()
tik9_tf = tk.IntVar()
i = 0
tik1 = Checkbutton(text="Ateşiniz var mı ?", variable=tik1_tf, onvalue=1, offvalue=0, command=sonucAt)
tik2 = Checkbutton(text="Yorgunluğunuz var mı ?", variable=tik2_tf, onvalue=1, offvalue=0, command=sonucAt)
tik3 = Checkbutton(text="Kuru öksürüğünüz var mı ?", variable=tik3_tf, onvalue=1, offvalue=0, command=sonucAt)
tik4 = Checkbutton(text="Solunum zorluğunuz var mı ?", variable=tik4_tf, onvalue=1, offvalue=0, command=sonucAt)
tik5 = Checkbutton(text="Öksürüğünüz var mı?", variable=tik5_tf, onvalue=1, offvalue=0, command=sonucAt)
tik6 = Checkbutton(text="Ağrınız var mı ?", variable=tik6_tf, onvalue=1, offvalue=0, command=sonucAt)
tik7 = Checkbutton(text="Burun akıntınız var mı ?", variable=tik7_tf, onvalue=1, offvalue=0, command=sonucAt)
tik8 = Checkbutton(text="Boğaz ağrınız var mı ?", variable=tik8_tf, onvalue=1, offvalue=0, command=sonucAt)
tik9 = Checkbutton(text="İshaliniz var mı ?", variable=tik9_tf, onvalue=1, offvalue=0, command=sonucAt)
sonuc = Label(program, text="Durmunuz Burada Yazacaktır", padx=250, pady=230, font=("Helvetica", 16))

tik1.pack()
tik2.pack()
tik3.pack()
tik4.pack()
tik5.pack()
tik6.pack()
tik7.pack()
tik8.pack()
tik9.pack()
sonuc.pack()

program.mainloop()
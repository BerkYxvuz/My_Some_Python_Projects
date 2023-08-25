import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.rcParams['figure.facecolor'] = '#1A120B'

df = pd.read_csv('csv/athletes.csv')

figure = plt.figure()

axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
x = []
y = []
axes.plot(x, y)
axes.patch.set_facecolor('#1A120B')
axes.tick_params(axis='both', labelcolor='white')
axes.spines['left'].set_color('white')
axes.spines['bottom'].set_color('white')
axes.spines['right'].set_color('white')
axes.spines['top'].set_color('white')
axes.set_xlabel("Tarih", color='white')

axes.set_ylabel("Süre", color='white')

wid = tk.Tk()
wid.configure(background="#1A120B")
wid.geometry("1280x720")

lis = df.columns[df.columns.str.endswith('M')]

liste = tk.Listbox(wid)
liste.place(x=10, y=100)

def Yukleyici():
    global x, y, axes
    df = pd.read_csv('athletes.csv')
    selection = liste.get(liste.curselection())
    x = df[f'{selection}'].dropna()
    y = df[f'{selection}-Tarih'].dropna()
    axes.clear()
    axes.patch.set_facecolor('#1A120B')
    axes.plot(y, x)
    figure.canvas.draw()

yukle = tk.Button(wid, text="Yükle", command=Yukleyici)
yukle.place(x=50, y=270)

def yeniyaris():
    popup = tk.Tk()
    popup.configure(background="#1A120B")
    popup.geometry("550x460")

    yarislar = tk.Listbox(popup)
    yarislar.place(x=190, y=10)
    for item in lis:
        yarislar.insert(tk.END, item)

    derecelabel = tk.Label(popup, text="Derece Örn( 11.20 )", background="#1A120B", fg="white")
    derecelabel.place(x=199, y=190)
    derece = tk.Entry(popup, width=15)
    derece.place(x=205, y=220)

    tarihlabel = tk.Label(popup, text="Tarih Örn( 25.05.2022 )", background="#1A120B", fg="white")
    tarihlabel.place(x=195, y=240)
    tarh = tk.Entry(popup, width=15)
    tarh.place(x=205, y=270)

    def yenikayit():
        selected = yarislar.get(yarislar.curselection())
        selected = str(selected)
        yeni_kayit = {
            f'{selected}': [f'{derece.get()}'],
            f'{selected}-Tarih': [f'{tarh.get()}']
        }

        df = pd.read_csv('athletes.csv')

        df = pd.concat([df, pd.DataFrame(yeni_kayit)])

        df.to_csv('athletes.csv', index=False)
        print("Kayıt Edildi")
        popup.destroy()


    kayitbuton = tk.Button(popup, text="Kayıt Et", command=yenikayit)
    kayitbuton.place(x=225, y=320)

    popup.mainloop()

yenikayitbt = tk.Button(wid, text="Yeni Derece Ekle", command=yeniyaris)
yenikayitbt.place(x=25, y=20)

def yeniatlet():
    popup = tk.Tk()
    popup.configure(background="#1A120B")
    popup.geometry("550x460")

    derecelabel = tk.Label(popup, text="Atlet Örn(İsim-100M)", background="#1A120B", fg="white")
    derecelabel.place(x=199, y=190)

    derece = tk.Entry(popup, width=15)
    derece.place(x=205, y=220)

    def yenieklesutun():
        global lis, liste
        input = pd.read_csv('athletes.csv')
        input[f'{derece.get()}'] = ''
        input[f'{derece.get()}-Tarih'] = ''
        input.to_csv('athletes.csv')
        popup.destroy()
        liste.delete(0, tk.END)
        df = pd.read_csv("athletes.csv")
        lisz = df.columns[df.columns.str.endswith('M')]
        for y in lisz:
            liste.insert(tk.END, y)
        liste.update()

    gonder = tk.Button(popup, text="Ekle", command=yenieklesutun)
    gonder.place(x=235, y=250)

yenisutun = tk.Button(wid, text="Yeni Atlet", command=yeniatlet)
yenisutun.place(x=40, y=50)

for x in lis:
    liste.insert(tk.END, x)

canvas = FigureCanvasTkAgg(figure, master=wid)
canvas.draw()
canvas.get_tk_widget().configure(width=800, height=600)
canvas.get_tk_widget().pack(side=tk.TOP)

wid.mainloop()
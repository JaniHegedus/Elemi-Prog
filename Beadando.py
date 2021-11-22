from tkinter import *
import tkinter as tk
root =Tk()
root.title("Freddys Fazbear Pizza")
x=30
y=10
Text_color="blue"
Bg_color="white"
class Étterem():
    def __init__(self, nev="Freddy's Fazbear Pizza"):
        self.nev = nev
    def print_nev(self):
        print("Az étterem neve: {0}" .format(self.nev))


class Menü(Étterem):
    def __init__(self, nev= "Freddy"):
        self.nev = nev
        self.pizza="Pizzája"
        self.hambi="Hamburgere"
        self.calzone="Calzonéja"
        self.gyros="Gyros-a"
    def foetel(self, foetel):
        self.foetel=foetel
        return self.foetel
    def koret(self, koret):
        self.koret=koret
        return self.koret
    def ital(self, ital):
        self.ital=ital
        return self.ital
    def print_nev(self):
        print("A menü: ", self.nev, "!")
    def Menu_1(self):
        print("Az első menü: ", self.nev, self.pizza,"!")
        return self.nev,self.pizza
    def Menu_2(self):
        print("Az Második menü: ", self.nev, self.hambi, "!")
        return self.nev,self.hambi
    def Menu_3(self):
        print("Az Harmadik menü: ", self.nev, self.calzone, "!")
        return self.nev,self.calzone
    def Menu_4(self):
        print("Az Negyedik menü: ", self.nev, self.gyros, "!")
        return self.nev,self.gyros

class Nyitvatartás(Étterem):
    def __init__(self, ido= "8-22", ido0= "10-20"):
        self.hetkoznap = ido
        self.hetvege = ido0
    def Hétköznap(self):
        #print("A nyitvatartás hétköznap: ", self.hetkoznap, "!")
        return self.hetkoznap
    def Hétvége(self):
        #print("A nyitvatartás hétvégén: ", self.hetvege, "!")
        return self.hetvege
def set_text(text):
    e.delete(0,END)
    e.insert(0,text)
    return
def kepernyo():
    #freddyspizza = Label(root, text="Freddys Fazbear Pizza").grid(row=0,column=0)
    entry0 = tk.StringVar()
    entry1 = tk.StringVar()
    entry2 = tk.StringVar()

    Menu0 = Label(root, text="Menü:").grid(row=1,column=0)
    Menu1 = Label(root, text=Menü().Menu_1()).grid(row=2,column=0)
    Menu1_1 = Label(root, text="Sültkrumpli").grid(row=2,column=1)
    Menu1_2 = Label(root, text="Kóla").grid(row=2,column=2)
    Menu1_3 = Label(root, text="1200Ft").grid(row=2,column=3)
    Menu2 = Label(root, text=Menü().Menu_2()).grid(row=3,column=0)
    Menu2_1 = Label(root, text="Sültkrumpli").grid(row=3,column=1)
    Menu2_2 = Label(root, text="Kóla").grid(row=3,column=2)
    Menu2_3 = Label(root, text="1400Ft").grid(row=3,column=3)
    Menu3 = Label(root, text=Menü().Menu_3()).grid(row=4,column=0)
    Menu3_1 = Label(root, text="Sültkrumpli").grid(row=4,column=1)
    Menu3_2 = Label(root, text="Kóla").grid(row=4,column=2)
    Menu3_3 = Label(root, text="1500Ft").grid(row=4,column=3)
    #Menu4 = Label(root, text=Menü().Menu_4()).grid(row=5,column=0)
    #Menu4_1 = Label(root, text="Sültkrumpli").grid(row=5,column=1)
    #Menu4_2 = Label(root, text="Kóla").grid(row=5,column=2)
    #Menu4_3 = Label(root, text="1600Ft").grid(row=5,column=3)
    #Menu5 = Label(root, text="Saját:").grid(row=6,column=0)
    global Menu5_1
    Menu5_1 = Entry(root)
    Menu5_1.grid(row=6, column=0)
    Menu5_1.insert(0,"Főétel")
    #entry0.set("Főétel")
    global Menu5_2
    Menu5_2 = Entry(root)
    Menu5_2.grid(row=6, column=1)
    Menu5_2.insert(0,"Köret")
    global Menu5_3
    Menu5_3 = Entry(root)
    Menu5_3.grid(row=6, column=2)
    Menu5_3.insert(0,"Innivaló")
    Menu5_4 = Button(root, text="Számít", padx=x, pady=y, command=Calculate, fg=Text_color,bg=Bg_color).grid(row=6,column=4)
    Menu_1_Button=Button(root, text="1. Menü", padx=x, pady=y, command=Menu01, fg=Text_color,bg=Bg_color).grid(row=7,column=0)
    Menu_2_Button=Button(root, text="2. Menü", padx=x, pady=y, command=Menu02, fg=Text_color,bg=Bg_color).grid(row=7,column=1)
    Menu_3_Button=Button(root, text="3. Menü", padx=x, pady=y, command=Menu03, fg=Text_color,bg=Bg_color).grid(row=7,column=2)
    #Menu_4_Button=Button(root, text="4. Menü", padx=x, pady=y, command=Menu04, fg=Text_color,bg=Bg_color).grid(row=7,column=3)
    Menu_5_Button = Button(root, text="Saját Menü", padx=x, pady=y, command=sajatmenu, fg=Text_color, bg=Bg_color).grid(row=7, column=3)

    Menu_6_Button = Button(root, text="Hétközbeni nyitvatartás", padx=x, pady=y, command=Menu05, fg=Text_color,bg=Bg_color).grid(row=8, column=1)
    Menu_7_Button = Button(root, text="Hétvégi nyitvatartás", padx=x, pady=y, command=Menu06, fg=Text_color,bg=Bg_color).grid(row=8, column=2)
    Menu_8_Button = Button(root, text="Kilépés", padx=x, pady=y, command=root.quit, fg=Text_color,bg=Bg_color).grid(row=10, column=5)
    Menu_8_Button = Button(root, text="Ételek, Italok", padx=x, pady=y, command=Ételek_Italok, fg=Text_color,bg=Bg_color).grid(row=10, column=0)
    #myLabel.pack()
def Calculate():
    entry0=Menu5_1.get()
    entry1=Menu5_2.get()
    entry2=Menu5_3.get()
    Ár=0
    if entry0.lower() ==Menü().foetel("pizza"):
        Ár += 950
    #if entry0.lower()=="pizza":
        #Ár+=950
    if entry1.lower()==Menü().koret("sültkrumpli"):
        Ár+=150
    if entry2.lower()==Menü().ital("kóla"):
        Ár+=100
    if entry0.lower()==Menü().foetel("calzone"):
        Ár+=950
    if entry1.lower()==Menü().koret("rízs"):
        Ár+=100
    if entry2.lower()==Menü().ital("sprite"):
        Ár+=120
    if entry0.lower()==Menü().foetel("gyros"):
        Ár+=1000
    if entry1.lower()==Menü().koret("krumplipüré"):
        Ár+=150
    if entry2.lower()==Menü().ital("tea"):
        Ár+=90
    if entry0.lower()==Menü().foetel("hamburger"):
        Ár+=650
    if entry1.lower()==Menü().koret("krokett"):
        Ár+=200
    if entry2.lower()==Menü().ital("fanta"):
        Ár+=110
    Válasz=("Rendelés: "+entry0+" "+entry1+" "+entry2+"\n Ár: "+str(Ár)+"Ft")

    Menu5_4 = Label(root, text=Válasz).grid(row=6, column=3)
    return
def Menu01():
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=0)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=1)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=2)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=3)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=4)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=5)


    Kattintas0 = Label(root, text="Az első menüt választotta!").grid(row=9, columnspan=5)
def Menu02():
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=0)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=1)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=2)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=3)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=4)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=5)


    Kattintas0 = Label(root, text="A második menüt választotta!").grid(row=9, columnspan=5)
def Menu03():
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=0)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=1)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=2)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=3)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=4)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=5)


    Kattintas0 = Label(root, text="A harmadik menüt választotta!").grid(row=9, columnspan=5)
def Menu04():
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=0)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=1)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=2)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=3)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=4)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=5)


    Kattintas0 = Label(root, text="A negyedik menüt választotta!").grid(row=9, columnspan=5)
def Menu05():
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=0)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=1)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=2)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=3)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=4)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=5)

    Kattintas0 = Label(root, text="A nyitvatartás hétköznap: {0}" .format(Nyitvatartás().Hétköznap())).grid(row=9, columnspan=5)
def Menu06():
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=0)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=1)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=2)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=3)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=4)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=5)


    Kattintas0 = Label(root, text="A nyitvatartás hétvégén: {0}" .format(Nyitvatartás().Hétvége())).grid(row=9, columnspan=5)
def sajatmenu():
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=0)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=1)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=2)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=3)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=4)
    Kattintas0 = Label(root,
                       text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(
        row=9, column=5)

    Válasz=""
    db=0
    if Menu5_1.get()=="Főétel":
        Válasz += "Főétel"
        db+=1
    if Menu5_2.get() == "Köret":
        Válasz += " Köret"
        db+=1
    if Menu5_3.get() == "Innivaló":
        Válasz+=" Innivaló"
        db+=1
    if db>0:
        Kattintas0 = Label(root, text=Válasz+" nincs kiválasztva").grid(row=9, columnspan=5)
        db=0
    else:
        Kattintas0 = Label(root, text="A rendelés elfogadva").grid(row=9, columnspan=5)

    print(Menü().foetel(Menu5_1.get()))
    print(Menü().koret(Menu5_2.get()))
    print(Menü().ital(Menu5_3.get()))
def saját():
    Étterem().print_nev()
    Menü().Menu_1()
    Menü().Menu_2()
    Menü().Menu_3()
    Menü().Menu_4()
    Nyitvatartás().Hétköznap()
def Ételek_Italok():
    Kattintas0 = Label(root, text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(row=9, column=0)
    Kattintas0 = Label(root, text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(row=9, column=1)
    Kattintas0 = Label(root, text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(row=9, column=2)
    Kattintas0 = Label(root, text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(row=9, column=3)
    Kattintas0 = Label(root, text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(row=9, column=4)
    Kattintas0 = Label(root, text="                                                                           \n                                                                           \n                                                                           \n                                                                           ").grid(row=9, column=5)
    Kattintas1 = Label(root, text="Pizza\n Calzone,\n Gyros \n Hamburger").grid(row=9 ,column=0)
    Kattintas1 = Label(root, text="Sültkrumpli\n Krumplipüré,\n Rízs \n Krokett").grid(row=9,column=1)
    Kattintas1 = Label(root, text="Kóla\n Fanta,\n Sprite \n Tea").grid(row=9,column=2)

#saját()
kepernyo()
root.mainloop()

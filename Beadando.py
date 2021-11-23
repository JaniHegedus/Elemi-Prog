from tkinter import *
import tkinter as tk
root = Tk()
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
    def foetel(self, foetel):
        self.foetel=foetel
        if foetel==1:
            self.foetel="pizza"
        if foetel==2:
            self.foetel="rántotthús"
        if foetel==3:
            self.foetel="gyros"
        if foetel==4:
            self.foetel="hamburger"
        return self.foetel
    def koret(self, koret):
        self.koret=koret
        if koret==1:
            self.koret="sültkrumpli"
        if koret==2:
            self.koret="rízs"
        if koret==3:
            self.koret="krumplipüré"
        if koret==4:
            self.koret="krokett"
        return self.koret
    def ital(self, ital):
        self.ital=ital
        if ital == 1:
            self.ital = "kóla"
        if ital == 2:
            self.ital = "sprite"
        if ital == 3:
            self.ital = "tea"
        if ital == 4:
            self.ital = "fanta"

        return self.ital
    def ar(self, ar):
        self.ar=ar
        if ar == 1:
            self.ar = "1200Ft"
        if ar == 2:
            self.ar = "1400Ft"
        if ar == 3:
            self.ar = "1500Ft"
        if ar == 4:
            self.ar = "1600Ft"

        return self.ar
    def print_nev(self):
        print("A menü: ", self.nev, "!")
    def Menu_1(self):
        print("Az első menü: ", self.nev, Menü().foetel(1),"!")
        return  Menü().foetel(1),Menü().koret(1),Menü().ital(1),Menü().ar(1)
    def Menu_2(self):
        print("Az Második menü: ", self.nev, Menü().foetel(2), "!")
        return Menü().foetel(2),Menü().koret(2),Menü().ital(2),Menü().ar(2)
    def Menu_3(self):
        print("Az Harmadik menü: ", self.nev, Menü().foetel(3), "!")
        return Menü().foetel(3),Menü().koret(3),Menü().ital(3),Menü().ar(3)
    def Menu_4(self):
        print("Az Negyedik menü: ", self.nev, Menü().foetel(4), "!")
        return Menü().foetel(4),Menü().koret(4),Menü().ital(4),Menü().ar(4)
def sajatmenu():
    sajatmenu.foetel=""
    sajatmenu.koret=""
    sajatmenu.ital=""
    sajatmenu.ar=""
def kiir():
    return sajatmenu.foetel,sajatmenu.koret,sajatmenu.ital,sajatmenu.ar
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
    a=1
    Menu0 = Label(root, text="Menü:").grid(row=a,column=0)
    a+=1
    Menu1 = Label(root, text=Menü().foetel(1)).grid(row=a,column=0)
    Menu1_1 = Label(root, text=Menü().koret(1)).grid(row=a,column=1)
    Menu1_2 = Label(root, text=Menü().ital(1)).grid(row=a,column=2)
    Menu1_3 = Label(root, text=Menü().ar(1)).grid(row=a,column=3)
    a+=1
    Menu2 = Label(root, text=Menü().foetel(2)).grid(row=a,column=0)
    Menu2_1 = Label(root, text=Menü().koret(2)).grid(row=a,column=1)
    Menu2_2 = Label(root, text=Menü().ital(2)).grid(row=a,column=2)
    Menu2_3 = Label(root, text=Menü().ar(2)).grid(row=a,column=3)
    a+=1
    Menu3 = Label(root, text=Menü().foetel(3)).grid(row=a,column=0)
    Menu3_1 = Label(root, text=Menü().koret(3)).grid(row=a,column=1)
    Menu3_2 = Label(root, text=Menü().ital(3)).grid(row=a,column=2)
    Menu3_3 = Label(root, text=Menü().ar(3)).grid(row=a,column=3)
    a+=1
    Menu4 = Label(root, text=Menü().foetel(4)).grid(row=a,column=0)
    Menu4_1 = Label(root, text=Menü().koret(4)).grid(row=a,column=1)
    Menu4_2 = Label(root, text=Menü().ital(4)).grid(row=a,column=2)
    Menu4_3 = Label(root, text=Menü().ar(4)).grid(row=a,column=3)
    a+=1
    Menu5 = Label(root, text="Saját:").grid(row=a,column=0)
    Menu5_4 = Button(root, text="Számít", padx=x, pady=y, command=Calculate, fg=Text_color, bg=Bg_color).grid(row=a,
                                                                                                              column=4)

    a+=1
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
    Menu_1_Button=Button(root, text="1. Menü", padx=x, pady=y, command=Menu01, fg=Text_color,bg=Bg_color).grid(row=a,column=0)
    Menu_2_Button=Button(root, text="2. Menü", padx=x, pady=y, command=Menu02, fg=Text_color,bg=Bg_color).grid(row=a,column=1)
    Menu_3_Button=Button(root, text="3. Menü", padx=x, pady=y, command=Menu03, fg=Text_color,bg=Bg_color).grid(row=a,column=2)
    Menu_4_Button=Button(root, text="4. Menü", padx=x, pady=y, command=Menu04, fg=Text_color,bg=Bg_color).grid(row=a,column=3)
    Menu_5_Button = Button(root, text="Saját Menü", padx=x, pady=y, command=sajatmenu, fg=Text_color, bg=Bg_color).grid(row=a, column=4)
    a+=1

    Menu_6_Button = Button(root, text="Hétközbeni nyitvatartás", padx=x, pady=y, command=Menu05, fg=Text_color,bg=Bg_color).grid(row=8, column=1)
    Menu_7_Button = Button(root, text="Hétvégi nyitvatartás", padx=x, pady=y, command=Menu06, fg=Text_color,bg=Bg_color).grid(row=8, column=2)
    Menu_8_Button = Button(root, text="Kilépés", padx=x, pady=y, command=root.quit, fg=Text_color,bg=Bg_color).grid(row=10, column=5)
    Menu_8_Button = Button(root, text="Ételek, Italok", padx=x, pady=y, command=Ételek_Italok, fg=Text_color,bg=Bg_color).grid(row=10, column=0)
    #myLabel.pack()
def Calculate():
    entry0=Menu5_1.get()
    entry1=Menu5_2.get()
    entry2=Menu5_3.get()
    global Ár
    Ár=0
    if entry0.lower() ==Menü().foetel(1):
        Ár += 950
    #if entry0.lower()=="pizza":
        #Ár+=950
    if entry1.lower()==Menü().koret(1):
        Ár+=150
    if entry2.lower()==Menü().ital(1):
        Ár+=100
    if entry0.lower()==Menü().foetel(2):
        Ár+=950
    if entry1.lower()==Menü().koret(2):
        Ár+=100
    if entry2.lower()==Menü().ital(2):
        Ár+=120
    if entry0.lower()==Menü().foetel(3):
        Ár+=1000
    if entry1.lower()==Menü().koret(3):
        Ár+=150
    if entry2.lower()==Menü().ital(3):
        Ár+=90
    if entry0.lower()==Menü().foetel(4):
        Ár+=650
    if entry1.lower()==Menü().koret(4):
        Ár+=200
    if entry2.lower()==Menü().ital(4):
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
    print( Menü().Menu_1())
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


    print( Menü().Menu_2())
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


    print(Menü().Menu_3())
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


    print(Menü().Menu_4())
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
    if Menu5_1.get().lower()=="főétel":
        Válasz += "Főétel"
        db+=1
    if Menu5_2.get().lower() == "köret":
        Válasz += " Köret"
        db+=1
    if Menu5_3.get().lower() == "innivaló":
        Válasz+=" Innivaló"
        db+=1
    if db>0:
        Kattintas0 = Label(root, text=Válasz+" nincs kiválasztva").grid(row=9, columnspan=5)
        db=0
    else:
        Kattintas0 = Label(root, text="A rendelés elfogadva").grid(row=9, columnspan=5)
    Calculate()
    sajatmenu.foetel=Menu5_1.get()
    sajatmenu.koret=Menu5_2.get()
    sajatmenu.ital=Menu5_3.get()
    sajatmenu.ar=str(Ár)+"Ft"
    print(kiir())
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

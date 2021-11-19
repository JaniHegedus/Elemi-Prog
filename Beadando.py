from tkinter import *
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
    def __init__(self, ido= "6-22", ido0= "10-20"):
        self.hetkoznap = ido
        self.hetvege = ido0
    def Hétköznap(self):
        print("A nyitvatartás hétköznap: ", self.hetkoznap, "!")
        return self.hetkoznap
    def Hétvége(self):
        print("A nyitvatartás hétvégén: ", self.hetvege, "!")
        return self.hetvege
def kepernyo():
    #freddyspizza = Label(root, text="Freddys Fazbear Pizza").grid(row=0,column=0)
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
    Menu4 = Label(root, text=Menü().Menu_4()).grid(row=5,column=0)
    Menu4_1 = Label(root, text="Sültkrumpli").grid(row=5,column=1)
    Menu4_2 = Label(root, text="Kóla").grid(row=5,column=2)
    Menu4_3 = Label(root, text="1600Ft").grid(row=5,column=3)
    Menu_1_Button=Button(root, text="1. Menü", padx=x, pady=y, command=Menu01, fg=Text_color,bg=Bg_color).grid(row=6,column=0)
    Menu_2_Button=Button(root, text="2. Menü", padx=x, pady=y, command=Menu02, fg=Text_color,bg=Bg_color).grid(row=6,column=1)
    Menu_3_Button=Button(root, text="3. Menü", padx=x, pady=y, command=Menu03, fg=Text_color,bg=Bg_color).grid(row=6,column=2)
    Menu_4_Button=Button(root, text="4. Menü", padx=x, pady=y, command=Menu04, fg=Text_color,bg=Bg_color).grid(row=6,column=3)
    Menu_5_Button = Button(root, text="Hétközbeni nyitvatartás", padx=x, pady=y, command=Menu05, fg=Text_color,bg=Bg_color).grid(row=7, column=1)
    Menu_6_Button = Button(root, text="Hétvégi nyitvatartás", padx=x, pady=y, command=Menu06, fg=Text_color,bg=Bg_color).grid(row=7, column=2)
    Menu_7_Button = Button(root, text="Kilépés", padx=x, pady=y, command=root.quit, fg=Text_color,bg=Bg_color).grid(row=8, column=4)
    #myLabel.pack()
def Menu01():
    Kattintas0 = Label(root, text="Az első menüt választotta!").grid(row=9)
def Menu02():
    Kattintas1 = Label(root, text="A második menüt választotta!").grid(row=9)
def Menu03():
    Kattintas2 = Label(root, text="A harmadik menüt választotta!").grid(row=9)
def Menu04():
    Kattintas4 = Label(root, text="A negyedik menüt választotta!").grid(row=9)
def Menu05():
    Kattintas5 = Label(root, text="A nyitvatartás hétköznap: {0}" .format(Nyitvatartás().Hétköznap())).grid(row=9)
def Menu06():
    Kattintas6 = Label(root, text=("A nyitvatartás hétvégén: {0}" .format(Nyitvatartás().Hétvége()))).grid(row=9)
def saját():
    Étterem().print_nev()
    Menü().Menu_1()
    Menü().Menu_2()
    Menü().Menu_3()
    Menü().Menu_4()
    Nyitvatartás().Hétköznap()
#saját()
kepernyo()
root.mainloop()

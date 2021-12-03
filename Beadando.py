import time
from tkinter import *
import tkinter as tk
import io
global Ettermek
Ettermek=[]
global Foetelek
Foetelek=[]
global Koretek
Koretek=[]
global Italok
Italok=[]
global AR
AR=[]

root = Tk()
root.title("Ételkiszállítás")

matrix=[]
with io.open("Ettermek.txt", "r", encoding="utf-8") as fbee:
    for sor in fbee:
        kis_lista=[]
        sor=sor.strip().split()
        for elem in sor:
            kis_lista.append(elem)
        matrix.append(kis_lista)
    print(matrix)

for j in range(len(matrix)):
    kis_lista=[]
    for i in range(len(matrix[j])):
        if matrix[j][i] == '-':
            kis_lista.append(matrix[j-1][len(matrix[j])-1])
            kis_lista.append(matrix[j-1][len(matrix[j])])
    if kis_lista:
        Ettermek.append(kis_lista)
for k in range(len(matrix)):
    for l in range(len(matrix[k])):
        kis_lista = []
        kis_lista0 = []
        kis_lista1 = []
        kis_lista2 = []
        if matrix[k][l] == '-':
            kis_lista.append(matrix[k+1][0])
            kis_lista.append(matrix[k+1][1])
            kis_lista.append(matrix[k + 2][0])
            kis_lista.append(matrix[k + 2][1])
            kis_lista.append(matrix[k + 3][0])
            kis_lista.append(matrix[k + 3][1])
            kis_lista.append(matrix[k + 4][0])
            kis_lista.append(matrix[k + 4][1])
            kis_lista0.append(matrix[k + 1][2])
            kis_lista0.append(matrix[k + 2][2])
            kis_lista0.append(matrix[k + 3][2])
            kis_lista0.append(matrix[k + 4][2])
            kis_lista1.append(matrix[k + 1][3])
            kis_lista1.append(matrix[k + 2][3])
            kis_lista1.append(matrix[k + 3][3])
            kis_lista1.append(matrix[k + 4][3])
            kis_lista2.append(matrix[k + 1][4])
            kis_lista2.append(matrix[k + 2][4])
            kis_lista2.append(matrix[k + 3][4])
            kis_lista2.append(matrix[k + 4][4])
        if kis_lista:
            Foetelek.append(kis_lista)
        if kis_lista0:
            Koretek.append(kis_lista0)
        if kis_lista1:
            Italok.append(kis_lista1)
        if kis_lista2:
            AR.append(kis_lista2)

#print(Ettermek)
#print(Foetelek)
#print(Koretek)
#print(Italok)
#print(AR)

x=30
y=10
Text_color="blue"
Bg_color="white"
global b
b = 1


class Étterem():
    def __init__(self, et="Éttermek: "):
        self.et = et
    def nev(self, et):
        self.et=et
        if et == 1:
            self.et = ""
            self.et+=Ettermek[0][0]
            self.et+=" "
            self.et+=Ettermek[0][1]
        if et == 2:
            self.et = ""
            self.et+=Ettermek[1][0]
            self.et+=" "
            self.et+=Ettermek[1][1]
        if et == 3:
            self.et = ""
            self.et+=Ettermek[2][0]
            self.et+=" "
            self.et+=Ettermek[2][1]
        if et == 4:
            self.et = ""
            self.et+=Ettermek[3][0]
            self.et+=" "
            self.et+=Ettermek[3][1]
        return self.et
class Menü(Étterem):
    def __init__(self, nev="Freddy"):
        self.nev = nev

    def __init__(self, et=1):
        self.et = et

    def foetel(self, et, foetel):
        self.foetel = foetel
        for i in range(len(Foetelek)):
            if et == i:
                if foetel == 1:
                    self.foetel = ""
                    self.foetel += Foetelek[i][0]
                    self.foetel += " "
                    self.foetel += Foetelek[i][1]
                elif foetel == 2:
                    self.foetel = ""
                    self.foetel += Foetelek[i][2]
                    self.foetel += " "
                    self.foetel += Foetelek[i][3]
                elif foetel == 3:
                    self.foetel = ""
                    self.foetel += Foetelek[i][4]
                    self.foetel += " "
                    self.foetel += Foetelek[i][5]
                elif foetel == 4:
                    self.foetel = ""
                    self.foetel += Foetelek[i][6]
                    self.foetel += " "
                    self.foetel += Foetelek[i][7]
        return self.foetel

    def koret(self, et, koret):
        koret -= 1
        self.koret = koret
        if et <= 4 and et >= 1:
            for i in range(len(Koretek)):
                for j in range(len(Koretek[i])):
                    if et == i:
                        if koret == j:
                            self.koret = ""
                            self.koret = Koretek[i][j]
        return self.koret

    def ital(self, et, ital):
        ital -= 1
        self.ital = ital
        if et <= 4 and et >= 1:
            for i in range(len(Italok)):
                for j in range(len(Italok[i])):
                    if et == i:
                        if ital == j:
                            self.ital = ""
                            self.ital = Italok[i][j]
        return self.ital

    def ar(self, et, ar):
        self.ar = ar
        ar -= 1
        if et <= 4 and et >= 1:
            for i in range(len(AR)):
                for j in range(len(AR[i])):
                    if et == i:
                        if ar == j:
                            self.ar = ""
                            self.ar = AR[i][j]
        return self.ar

    def print_nev(self):
        print("A menü: ", self.nev, "!")

    def Menu_1(self):
        return Menü().foetel(b, 1) + " " + Menü().koret(b, 1) + " " + Menü().ital(b, 1)

    def Menu_2(self):
        return Menü().foetel(b, 2) + " " + Menü().koret(b, 2) + " " + Menü().ital(b, 2)

    def Menu_3(self):
        return Menü().foetel(b, 3) + " " + Menü().koret(b, 3) + " " + Menü().ital(b, 3)

    def Menu_4(self):
        return Menü().foetel(b, 4) + " " + Menü().koret(b, 4) + " " + Menü().ital(b, 4)

def clear_screen():
    a = 2
    g = 1
    Menu1 = Label(root, text="                                                                          ").grid(row=a, column=0)
    Menu1_1 = Label(root, text="                                                                          ").grid(row=a, column=1)
    Menu1_2 = Label(root, text="                                                                          ").grid(row=a, column=2)
    Menu1_3 = Label(root, text="                                                                          ").grid(row=a, column=3)
    a += 1
    g += 1
    Menu2 = Label(root, text="                                                                          ").grid(row=a, column=0)
    Menu2_1 = Label(root, text="                                                                          ").grid(row=a, column=1)
    Menu2_2 = Label(root, text="                                                                          ").grid(row=a, column=2)
    Menu2_3 = Label(root, text="                                                                          ").grid(row=a, column=3)
    a += 1
    g += 1
    Menu3 = Label(root, text="                                                                          ").grid(row=a, column=0)
    Menu3_1 = Label(root, text="                                                                          ").grid(row=a, column=1)
    Menu3_2 = Label(root, text="                                                                          ").grid(row=a, column=2)
    Menu3_3 = Label(root, text="                                                                          ").grid(row=a, column=3)
    a += 1
    g += 1
    Menu4 = Label(root, text="                                                                          ").grid(row=a, column=0)
    Menu4_1 = Label(root, text="                                                                          ").grid(row=a, column=1)
    Menu4_2 = Label(root, text="                                                                          ").grid(row=a, column=2)
    Menu4_3 = Label(root, text="                                                                          ").grid(row=a, column=3)
def clear_screen_lower():
    global c
    Kattintas0 = Label(root,
                       text="                                                  \n                                                  \n                                                  \n                                                  ").grid(
        row=c, column=0)
    Kattintas0 = Label(root,
                       text="                                                  \n                                                  \n                                                  \n                                                  ").grid(
        row=c, column=1)
    Kattintas0 = Label(root,
                       text="                                                  \n                                                  \n                                                  \n                                                  ").grid(
        row=c, column=2)
    Kattintas0 = Label(root,
                       text="                                                  \n                                                  \n                                                  \n                                                  ").grid(
        row=c, column=3)
    Kattintas0 = Label(root,
                       text="                                                  \n                                                  \n                                                  \n                                                  ").grid(
        row=c, column=4)
    Kattintas0 = Label(root,
                       text="                                                  \n                                                  \n                                                  \n                                                  ").grid(
        row=c, column=5)
def etlap_frissit():
    global b
    a = 2
    g = 1
    Menu1 = Label(root, text=Menü().foetel(b, g)).grid(row=a, column=0)
    Menu1_1 = Label(root, text=Menü().koret(b, g)).grid(row=a, column=1)
    Menu1_2 = Label(root, text=Menü().ital(b, g)).grid(row=a, column=2)
    Menu1_3 = Label(root, text=Menü().ar(b, g)).grid(row=a, column=3)
    a += 1
    g += 1
    Menu2 = Label(root, text=Menü().foetel(b, g)).grid(row=a, column=0)
    Menu2_1 = Label(root, text=Menü().koret(b, g)).grid(row=a, column=1)
    Menu2_2 = Label(root, text=Menü().ital(b, g)).grid(row=a, column=2)
    Menu2_3 = Label(root, text=Menü().ar(b, g)).grid(row=a, column=3)
    a += 1
    g += 1
    Menu3 = Label(root, text=Menü().foetel(b, g)).grid(row=a, column=0)
    Menu3_1 = Label(root, text=Menü().koret(b, g)).grid(row=a, column=1)
    Menu3_2 = Label(root, text=Menü().ital(b, g)).grid(row=a, column=2)
    Menu3_3 = Label(root, text=Menü().ar(b, g)).grid(row=a, column=3)
    a += 1
    g += 1
    Menu4 = Label(root, text=Menü().foetel(b, g)).grid(row=a, column=0)
    Menu4_1 = Label(root, text=Menü().koret(b, g)).grid(row=a, column=1)
    Menu4_2 = Label(root, text=Menü().ital(b, g)).grid(row=a, column=2)
    Menu4_3 = Label(root, text=Menü().ar(b, g)).grid(row=a, column=3)
    Kattintas0 = Label(root, text="                                                  ").grid(row=0, column=2)
    Menu_0 = Label(root, text=Étterem().nev(b)).grid(row=0, column=2)


with io.open("Rendelés.txt", "w", encoding="utf-8") as fki:
    fki.write(Étterem().nev(b)+"\n")

def sajatmenu():
    sajatmenu.foetel=""
    sajatmenu.koret=""
    sajatmenu.ital=""
    sajatmenu.ar=""

def kiir():
    with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
        fki.write(sajatmenu.foetel+" "+sajatmenu.koret+" "+sajatmenu.ital+" "+sajatmenu.ar+"\n")
    #fki.write()
    return sajatmenu.foetel, sajatmenu.koret, sajatmenu.ital, sajatmenu.ar

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

def kepernyo():
    global c
    #freddyspizza = Label(root, text="Freddys Fazbear Pizza").grid(row=0,column=0)
    entry0 = tk.StringVar()
    entry1 = tk.StringVar()
    entry2 = tk.StringVar()
    a=0

    Menu00_Button = Button(root, text="Fizetés", padx=x, pady=y, command=grandtotal, fg=Text_color, bg=Bg_color).grid(row=a,column=5)

    Menu0_Button = Button(root, text="<", padx=x, pady=y, command=b_csokkento, fg=Text_color, bg=Bg_color).grid(row=a, column=0)
    Menu_0 = Label(root, text=Étterem().nev(b)).grid(row=a, column=2)
    Menu1_Button = Button(root, text=">", padx=x, pady=y, command=b_novelo, fg=Text_color, bg=Bg_color).grid(row=a, column=4)
    a+=1
    Menu0 = Label(root, text="Menü:").grid(row=a,column=0)
    a+=1
    g=1
    Menu1 = Label(root, text=Menü().foetel(b,g)).grid(row=a,column=0)
    Menu1_1 = Label(root, text=Menü().koret(b,g)).grid(row=a,column=1)
    Menu1_2 = Label(root, text=Menü().ital(b,g)).grid(row=a,column=2)
    Menu1_3 = Label(root, text=Menü().ar(b,g)).grid(row=a,column=3)
    a+=1
    g+=1
    Menu2 = Label(root, text=Menü().foetel(b,g)).grid(row=a,column=0)
    Menu2_1 = Label(root, text=Menü().koret(b,g)).grid(row=a,column=1)
    Menu2_2 = Label(root, text=Menü().ital(b,g)).grid(row=a,column=2)
    Menu2_3 = Label(root, text=Menü().ar(b,g)).grid(row=a,column=3)
    a+=1
    g+=1
    Menu3 = Label(root, text=Menü().foetel(b,g)).grid(row=a,column=0)
    Menu3_1 = Label(root, text=Menü().koret(b,g)).grid(row=a,column=1)
    Menu3_2 = Label(root, text=Menü().ital(b,g)).grid(row=a,column=2)
    Menu3_3 = Label(root, text=Menü().ar(b,g)).grid(row=a,column=3)
    a+=1
    g+=1
    Menu4 = Label(root, text=Menü().foetel(b,g)).grid(row=a,column=0)
    Menu4_1 = Label(root, text=Menü().koret(b,g)).grid(row=a,column=1)
    Menu4_2 = Label(root, text=Menü().ital(b,g)).grid(row=a,column=2)
    Menu4_3 = Label(root, text=Menü().ar(b,g)).grid(row=a,column=3)
    a+=1
    Menu5 = Label(root, text="Saját:").grid(row=a,column=0)


    a+=1
    global Menu5_1
    Menu5_1 = Entry(root)
    Menu5_1.grid(row=a, column=0)
    Menu5_1.insert(0,"Fő étel")
    #entry0.set("Főétel")
    global Menu5_2
    Menu5_2 = Entry(root)
    Menu5_2.grid(row=a, column=1)
    Menu5_2.insert(0,"Köret")
    global Menu5_3
    Menu5_3 = Entry(root)
    Menu5_3.grid(row=a, column=2)
    Menu5_3.insert(0,"Innivaló")
    Menu5_4 = Button(root, text="Számít", padx=x, pady=y, command=Calculate, fg=Text_color, bg=Bg_color).grid(row=a,
                                                                                                              column=4)
    a += 1
    Menu_1_Button=Button(root, text="1. Menü", padx=x, pady=y, command=Menu01, fg=Text_color,bg=Bg_color).grid(row=a,column=0)
    Menu_2_Button=Button(root, text="2. Menü", padx=x, pady=y, command=Menu02, fg=Text_color,bg=Bg_color).grid(row=a,column=1)
    Menu_3_Button=Button(root, text="3. Menü", padx=x, pady=y, command=Menu03, fg=Text_color,bg=Bg_color).grid(row=a,column=2)
    Menu_4_Button=Button(root, text="4. Menü", padx=x, pady=y, command=Menu04, fg=Text_color,bg=Bg_color).grid(row=a,column=3)
    Menu_5_Button = Button(root, text="Saját Menü", padx=x, pady=y, command=sajatmenu, fg=Text_color, bg=Bg_color).grid(row=a, column=4)
    a+=1

    Menu_6_Button = Button(root, text="Hétközbeni nyitvatartás", padx=x, pady=y, command=Menu05, fg=Text_color,bg=Bg_color).grid(row=a, column=1)
    Menu_7_Button = Button(root, text="Hétvégi nyitvatartás", padx=x, pady=y, command=Menu06, fg=Text_color,bg=Bg_color).grid(row=a, column=2)
    a+=1
    c=a
    a+=1
    Menu_8_Button = Button(root, text="Kilépés", padx=x, pady=y, command=root.quit, fg=Text_color,bg=Bg_color).grid(row=a, column=5)
    Menu_8_Button = Button(root, text="Ételek, Italok", padx=x, pady=y, command=Ételek_Italok, fg=Text_color,bg=Bg_color).grid(row=a, column=0)
    #myLabel.pack()

def b_csokkento():
    global b
    if b==1:
        b=4
    else:
        b=b-1
    clear_screen()
    etlap_frissit()

    with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
        fki.write("\n"+Étterem().nev(b) + "\n")
def b_novelo():
    global b
    if b==4:
        b=1
    else:
        b=b+1
    clear_screen()
    etlap_frissit()

    Kattintas0 = Label(root, text="                                                  ").grid(row=0, column=2)
    Menu_0 = Label(root, text=Étterem().nev(b)).grid(row=0, column=2)
    with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
        fki.write("\n"+Étterem().nev(b) + "\n")

def Calculate():
    entry0=Menu5_1.get()
    entry1=Menu5_2.get()
    entry2=Menu5_3.get()
    global Ár
    Ár=0
    for j in range(4):
        if entry0.lower() == Menü().foetel(j,1):
            Ár += 950
        if entry1.lower()==Menü().koret(j,1):
            Ár+=150
        if entry2.lower()==Menü().ital(j,1):
            Ár+=100
        if entry0.lower()==Menü().foetel(j,2):
            Ár+=950
        if entry1.lower()==Menü().koret(j,2):
            Ár+=100
        if entry2.lower()==Menü().ital(j,2):
            Ár+=120
        if entry0.lower()==Menü().foetel(j,3):
            Ár+=1000
        if entry1.lower()==Menü().koret(j,3):
            Ár+=150
        if entry2.lower()==Menü().ital(j,3):
            Ár+=90
        if entry0.lower()==Menü().foetel(j,4):
            Ár+=650
        if entry1.lower()==Menü().koret(j,4):
            Ár+=200
        if entry2.lower()==Menü().ital(j,4):
            Ár+=110
    Válasz=("Rendelés: "+entry0+" "+entry1+" "+entry2+"\n Ár: "+str(Ár)+"Ft")

    Menu5_4 = Label(root, text=Válasz).grid(row=6, column=3)
    return

def Menu01():
    clear_screen_lower()
    for sor in Menü().Menu_1():
        with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
            fki.write(sor)
    with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
        fki.write("\n")
    Kattintas0 = Label(root, text="Az első menüt választotta!").grid(row=c, columnspan=5)
    print(Menü().Menu_3())
def Menu02():
    clear_screen_lower()
    print( Menü().Menu_2())
    for sor in Menü().Menu_2():
        with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
            fki.write(sor )
    with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
        fki.write("\n")
    Kattintas0 = Label(root, text="A második menüt választotta!").grid(row=c, columnspan=5)
def Menu03():
    clear_screen_lower()
    for sor in Menü().Menu_3():
        with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
            fki.write(sor)
    with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
        fki.write("\n")


    print(Menü().Menu_3())
    Kattintas0 = Label(root, text="A harmadik menüt választotta!").grid(row=c, columnspan=5)
def Menu04():
    clear_screen_lower()
    for sor in Menü().Menu_4():
        with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
            fki.write(sor)
    with io.open("Rendelés.txt", "a", encoding="utf-8") as fki:
        fki.write("\n")
    print(Menü().Menu_4())
    Kattintas0 = Label(root, text="A negyedik menüt választotta!").grid(row=c, columnspan=5)
def Menu05():
    clear_screen_lower()
    Kattintas0 = Label(root, text="A nyitvatartás hétköznap: {0}" .format(Nyitvatartás().Hétköznap())).grid(row=c, columnspan=5)
def Menu06():
    clear_screen_lower()
    Kattintas0 = Label(root, text="A nyitvatartás hétvégén: {0}" .format(Nyitvatartás().Hétvége())).grid(row=c, columnspan=5)

def sajatmenu():
    global c
    clear_screen_lower()
    Válasz=""
    dbf=0
    dbk=0
    dbi=0
    i=1
    while i==4:
        j=0
        while j==4:
            if Menu5_1.get().lower()==Foetelek[i][j]:
                dbf+=1
            if Menu5_2.get().lower() == Koretek[i][j]:
                dbk+=1
            if Menu5_3.get().lower() == Italok[i][j]:
                dbi+=1
            j+=1
        i+=1
    if dbf<=1:
        Válasz+="Főétel "
    if dbk<=1:
        Válasz+="Köret "
    if dbi<=1:
        Válasz+="Innivaló "
    if Válasz!="":
        Kattintas0 = Label(root, text=Válasz + " nincs kiválasztva").grid(row=c, columnspan=5)
    else:
        Kattintas0 = Label(root, text="A rendelés elfogadva").grid(row=c, columnspan=5)

    Calculate()
    sajatmenu.foetel=Menu5_1.get()
    sajatmenu.koret=Menu5_2.get()
    sajatmenu.ital=Menu5_3.get()
    sajatmenu.ar=str(Ár)+"Ft"
    print(kiir())

def Ételek_Italok():
    global c
    clear_screen_lower()
    Kattintas1 = Label(root, text=Menü().Menu_1()).grid(row=c ,column=0)
    Kattintas1 = Label(root, text=Menü().Menu_2()).grid(row=c,column=1)
    Kattintas1 = Label(root, text=Menü().Menu_3()).grid(row=c,column=2)
    Kattintas1 = Label(root, text=Menü().Menu_4()).grid(row=c,column=3)
    fki.close()

def grandtotal():
    lista=[]
    fbe=open("Rendelés.txt","r")
    for sor in fbe:
        kis_lista=[]
        sor=sor.strip().split()
        for elem in sor:
            kis_lista.append(elem)
        lista.append(kis_lista)
    global grand_total
    grand_total=0
    for sor in lista:
        if len(sor)>4:
            if sor[4]!="0Ft":
                if len(sor[4])>5:
                    print(int(sor[4][:4]))
                    grand_total+=int(sor[4][:4])
                else:
                    print(int(sor[4][:3]))
                    grand_total+=int(sor[4][:3])
    clear_screen_lower()
    Kattintas0 = Label(root, text=str(grand_total)+ "Ft fizetendő a kasszánál").grid(row=c, columnspan=5)
kepernyo()
root.mainloop()


import math
import random


def hello():
    print("Hello world")
    variable = "Hello 'world'!"
    variable = 'Hello "there"!'
    print(variable, type(variable))
    variable = 3
    print(variable, type(variable))
    print(3)
    print(3.6, type(3.6))
    print(True, type(True))
    a = 1
    b = 2
    print(a * b)
    a, b = 3, 4
    print(a * b)
    a = b = 3
    print(a * b)
    b = 5
    print(a * b)

def alma():
    students = 34
    apples = 124
    apple_per_person = apples // students
    leftovers = apples % students
    print("Each student gets", apple_per_person, "apple(s) and", leftovers, "apple(s) will not be handed out")
def sűrűség():
    density_lead = 11.34  # cm^3
    density_copper = 8.69
    volume_lead = 18
    volume_copper = 23
    mass_lead = density_lead * volume_lead
    mass_copper = density_copper * volume_copper
    print(mass_lead > mass_copper)

def műveletek():
    a, b, c = 3, 4, 5
    print(a + b * c)
    print((a + b) * c)
    print("3^4 =", a ** b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(b / 2)
    print(b // 2)
    print(b % 2)
def percek_a_héten():
    hours_in_a_day = 24
    days_in_a_week = 7
    minutes_in_an_hour = 60
    minutes_in_a_week = hours_in_a_day * days_in_a_week * minutes_in_an_hour
    print("Ha", hours_in_a_day, "óra van egy napban, akkor", minutes_in_a_week, "perc van egy héten")
    hours_in_a_day = 26
    minutes_in_a_week = hours_in_a_day * days_in_a_week * minutes_in_an_hour
    print("Ha", hours_in_a_day, "óra van egy napban, akkor", minutes_in_a_week, "perc van egy héten")
def kör():
    diameter = 24  # cm
    radius = diameter / 2
    perimeter = 2 * radius * math.pi
    area = radius ** 2 * math.pi
    print("Perimeter = ", perimeter)
    print("Area = ", area)
def speciális_karakterek():
    print(
        "Speciális karakter a backspace (\b), a sortörés (\n), de van tabulátor (\t), visszaperjel (\\), aposztróf (\')"
        " és idézőjel (\") is. Az aposztrófot visszaperjel nélkül is megadhatom ('), mert idézőjellel jelöltem a stringet.")

    print("A kocsi visszat ki ne hagyjuk (\r)")
def String():
    python = "pythonban programozok"
    print("A python szó első karaktere: ", python[0])
    print("A python szó utolsó karaktere:", python[5])
    print("A python szó utolsó karaktere:", python[-1])
    print("A python szó utolsó karaktere:", python[len(python) - 1])

    print("A python változó 5-ször egymás után:", python * 5)

    str2 = "hallgató"
    str3 = "Hiába a hegynyi anyag, a hallgató gyorsan halad."
    print(str2 in str3)
    print(python in str3)
    print(python not in str3)

    print(str3[0:5])  # balról zárt, jobbról nyitott intervallum
    print(python + str2 + str3)
    print(python, str2, str3, sep=" alma ")

    str4 = "HALLGATÓ"
    print(str4 in str3)
    print(str4 > str2)
    str1 = "Az almafán almák teremnek."
    #print(type(len(str1)))
    str2 = "terem"
    print(str1.find(str2))
    lower_str1=str1.lower()
    print(lower_str1)
    print(str1.upper())
    print(str1.isupper())
    print(str2.isalpha())
    print(str1.isalpha())
    print(str2.isalnum())
    str3 = "user123"
    print(str2.isalpha())
    print(str2.isalnum())

def elágazások():
    number=35
    if number >100:
        print("A szám nagyobb mint száz!")
    else:
        print("A szám kissebb mint száz!")
    if number%2==0:
        print("a szám páros")
    else:
        print("Páratlan")
    number1=3
    number2=9
    if number1 % number2 == 0:
        print("Az egyik szám osztható a másikkal")
    elif number2 % number1 == 0:
        print("A másik szám osztható az elsővel.")
    else:
        print("A számok nem oszthatóak.")
    radar="radar2"
    if radar[0] == radar[-1]:
        print("Az első és az utolsó betű megegyezik")
    else:
        print("Az első és az utolsó betű különböző")
    a=input()
    if a>0:
        print("A szám pozitív")
    elif a<0:
        print("A szám negatív")
    else:
        print("A szám 0")
def ciklusok():
    is_number = False
    number = 0
    while not is_number:
        try:
            number = int(input("Kérek egy egész számot: "))
            is_number = True
        except ValueError:
            print("Nem egész szám.")

    if number % 2 == 0:
        print("Páros")
    else:
        print("Páratlan")

    print()

    i = 1
    while i <= 5:
        print(i)
        i += 1

    print()

    for j in [1, 2, 3, 4, 5]:
        print(j)

    print()

    for k in range(50, 60):
        print(k, end=" ")

    print()

    for l in range(1, 100):
        if l % 2 != 0:
            print(l, end=" ")
def lista():
    is_number = False
    number = 0
    while not is_number:
        try:
            number = int(input("Kérek egy egész számot: "))
            is_number = True
        except ValueError:
            print("Nem egész szám.")

    if number % 2 == 0:
        print("Páros")
    else:
        print("Páratlan")

    print()

    i = 1
    while i <= 5:
        print(i)
        i += 1

    print()

    for j in [1, 2, 3, 4, 5]:
        print(j)

    print()

    for k in range(50, 60):
        print(k, end=" ")

    print()

    for l in range(1, 100):
        if l % 2 != 0:
            print(l, end=" ")
def feltételek():
    number = 101
    if number > 100:
        print("Nagyobb, mint száz.")
    else:
        print("Nem nagyobb, mint száz.")

    if number % 2 == 0:
        print("Páros.")
    else:
        print("Páratlan.")

    number1 = 5
    number2 = 25
    if number1 % number2:
        print("Egyik szám osztható a másikkal.")
    else:
        if number2 % number1 == 0:
            print("A másik szám is osztható az elsővel.")
        else:
            print("Nem.")

    radar = "szöves"
    if radar[0] == radar[-1]:
        print("Megegyezik az első és az utolsó betű.")
    else:
        print("Nem egyezik meg.")

    num = 3
    if num > 0:
        print("Pozitív.")
    else:
        if num == 0:
            print("Nulla.")
        else:
            print("Negatív")

    num1 = 7
    num2 = 6
    num3 = 5
    if num1 > num2:
        if num1 > num3:
            print("Az első szám a legnagyobb.")
        elif num3 > num1:
            print("A harmadik szám a legnagyobb.")

    elif num2 > num1:
        if num2 > num3:
            print("A második szám a legnagyobb.")
        else:
            print("A harmadik szám a legnagyobb.")

    elif num1 == num2:
        if num1 == num3:
            print("Egyenlőek.")
        elif num1 > num3:
            print("Az első két szám a legnagyobb.")
        else:
            print("A harmadik szám a legnagyobb.")

    numero = 4
    if numero >= 3 and numero < 17:
        print("Beleesik.")
    else:
        print("Nem esik bele.")

    a = 3
    b = 1
    c = 5

    if (a + b > c and b + c > a and a + c > b):
        print("A háromszög szerkeszthető.")
    else:
        print("Nem szerkesztehtő.")

    try:
        jegy = 3
        # jegy = int(input("Jegy: "))
        if jegy == 5:
            print("Kíváló.")
        elif jegy == 4:
            print("Jó.")
        elif jegy == 3:
            print("Közepes.")
        elif jegy == 2:
            print("Elégéséges.")
        elif jegy == 1:
            print("Elégtelen.")
        else:
            print("Nem jó érték.")
    except ValueError:
        print("Nem számjegy.")

    try:
        print(type(float(input("Kérek egy valós számot: "))))
    except ValueError:
        print("Hibás bemenet.")

    print(type(str(9)))
    print(type(str(-37.54)))

    try:
        szam = input()
        szam = float(szam)
        print(szam * 3)
    except ValueError:
        print("Nem szám.")
def random_szamok():
    print(random.randint(2, 400))
    print(random.random())

    r = random.randint(-100, 100)
    print(r)
    if r > 0:
        print("Pozitív.")
    else:
        if r == 0:
            print("Nulla.")
        else:
            print("Negatív")
def string2():
    str1 = "Az almafán almák teremnek."
    print("A szöveg hossza:", len(str1))
    print(type(len(str1)))

    str2 = "terem"
    print(str1.find(str2))

    lower_str1 = str1.lower()
    print(str1)
    print(lower_str1)
    print(str1.upper())
    print(lower_str1.islower())
    print(lower_str1.isupper())
    print(str1.isupper())

    print(str1.isalpha())
    print(str2.isalpha())
    print(str2.isalnum())
    str3 = "user12"
    print(str3.isalpha())
    print(str3.isalnum())
def lista_gyak():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus', 'szeptember',
             'október', 'november', 'december']

    month_and_days = []

    for i in range(12):
        month_and_days.append(month[i])
        month_and_days.append(days_in_month[i])

    print(month_and_days)

    print(' '.join(str(month_and_days)))

    # -------------------------------------------

    numbers = [3, 2, 6, 8, 1, 5]

    max = numbers[0]

    for i in range(len(numbers)):
        if max < numbers[i]:
            max = numbers[i]

    print(max)

    min = numbers[0]

    hely = 0

    for i in range(len(numbers)):
        if min > numbers[i]:
            min = numbers[i]
            hely = i
    for i in range(len(numbers)):
        if numbers[i] == min:
            print(i)
    print(hely)
def file():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = ['január', 'február', 'március', 'április', 'május', 'június', 'július', 'augusztus', 'szeptember',
             'október', 'november', 'december']

    month_and_days = []

    for i in range(12):
        month_and_days.append(month[i])
        month_and_days.append(days_in_month[i])

    print(month_and_days)

    print(' '.join(str(month_and_days)))

    # -------------------------------------------

    numbers = [3, 2, 6, 8, 1, 5]

    max = numbers[0]

    for i in range(len(numbers)):
        if max < numbers[i]:
            max = numbers[i]

    print(max)

    min = numbers[0]

    hely = 0

    for i in range(len(numbers)):
        if min > numbers[i]:
            min = numbers[i]
            hely = i
    for i in range(len(numbers)):
        if numbers[i] == min:
            print(i)
    print(hely)
def feladat1():
    matrix=[]
    matrix1=[]
    fbe=open("Adatok.txt","r")
    for sor in fbe:
        lista=[]
        sor=sor.strip().split()
        for elem in sor:
            lista.append(elem)
        matrix.append(lista)
    fbe1 = open("Adatok1.txt", "r")
    for sor in fbe1:
        lista=[]
        sor=sor.strip().split()
        for elem in sor:
            lista.append(elem)
        matrix1.append(lista)
    listaa=[]

    fki=open("Másolt.txt","w")
    lista=[]
    for i in range(len(matrix)):
        kis_lista=[]
        for j in range(len(matrix[i])):
            #print(matrix[i][j-1]+matrix1[i][j-1])
            try:
                kis_lista.append(matrix[i][j])
                kis_lista.append(matrix1[i][j])
            except IndexError:
                break
        lista.append(kis_lista)
    for sor in lista:
        for elem in sor:
            fki.write(elem+" ")
        fki.write("\n")
    print(lista)
    #print(matrix)
    #print(matrix1)
    #print(listaa)
#hello()
#alma()
#sűrűség()
#percek_a_héten()
#kör()
#speciális_karakterek()
#String()
#elágazások()
#ciklusok()
#lista()
#feltételek()
#random_számok()
feladat1()
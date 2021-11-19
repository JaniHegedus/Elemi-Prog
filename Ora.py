import math

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

def main():
    #hello()
    #alma()
    #sűrűség()
    #percek_a_héten()
    #kör()
    #speciális_karakterek()
    #String()
    #elágazások()

main()
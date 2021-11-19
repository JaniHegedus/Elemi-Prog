from turtle import Turtle
'''
class metódusok
(s: self, o: más)
__init__(s,argumentumok)   objektum installálása
__del__(s)   meghívódik az objektum megszünésekor (értéke 0 lesz)
__repr__(s)     repr() és ´...´ konverziók
__str__(s)     str() és 'print' kifejezések
__cmp__(s, o)     <, ==, >, <=, <>, !=, >=, is [not] implementálásakor
__hash__(s)     hash() és dictionary operátorok
__getattr__(s, név)     meghívódik, ha az attribútum keresés nem találja <nev>- et.
__setattr__(s, név, érték)     meghívódik, ha attribútumnak adunk értéket.
(benne ne használjuk a "self.név = érték" kifejezést,használjuk a "self.__dict__[név] = érték")
__delattr__(s, név)     meghívódik, hogy töröljük a <név> attribútumot.
__call__(self, *argumentumok)     meghívódi, amikor egy példányt függvényként hívunk meg.

isinstance(ob1, ob2), ahol az első argumentum egy példányobjektum, a második pedig egy osztályobjektum vagy típusobjektum. Azt vizsgálja, hogy az ob1 az ob2 osztály egy példánya-e, vagy, hogy az ob1 típusa megegyezik-e az ob2 típusával.

issubclass(osztály1, osztály2): megvizsgálja, hogy az osztály1 az osztály2 alosztálya-e. Egy osztály a saját alosztályának tekinthető.

hasattr(obj, attr), ahol az első argumentum egy objektum, a második pedig egy karakterlánc. A függvény azt vizsgálja, hogy van-e az objektumnak egy vagy több olyan attribútuma, amelynek a neve azonos az átadott karakterlánccal.
hash(s) = __hash__(s) - dictionary típusra hívatkozás hash értéke
s[k]=v = __setitem__(s,k,v)
del s[k] = __delitem__(s,k)

Numerikusra vonatkozó speciális
(s: self, o: más)
s+o = __add__(s,o)
s-o = __sub__(s,o)
s*o = __mul__(s,o)
s/o = __div__(s,o)
s%o = __mod__(s,o)
divmod(s,o) = __divmod__(s,o)
pow(s,o) = __pow__(s,o)
s&o = __and__(s,o)
s^o = __xor__(s,o)
s|o = __or__(s,o)
s<<o = __lshift__(s,o)
s>>o = __rshift__(s,o)
nonzero(s) = __nonzero__(s) (logikai teszteléskor használjuk)
-s = __neg__(s)
+s = __pos__(s)
abs(s) = __abs__(s)
~s = __invert__(s) (bit szerint)
int(s) = __int__(s)
long(s) = __long__(s)
float(s) = __float__(s)
oct(s) = __oct__(s)
hex(s) = __hex__(s)
coerce(s,o) = __coerce__(s,o)
A jobb oldali egyenlõségek minden bináris operátorra léteznek; azokat akkor hívjuk meg, amikor az osztály példánya az operátor jobb oldalán szerepel.
a + 3 hívása __add__(a, 3)
3 + a hívása __radd__(a, 3)
Értéktáblák:
(s: self, i: index vagy kulcs )

len(s) = __len__(s) objektum hossza, >= 0.  0 hosszúság == false
s[i] = __getitem__(s,i) i indexû/kulcsú elem, 0-tól számítjuk.
Szekvenciák, általános metódusok, kiegészítés:
s[i]=v = __setitem__(s,i,v)
del s[i] = __delitem__(s,i)
s[i:j] = __getslice__(s,i,j)
s[i:j]=szekv. = __setslice__(s,i,j,szekv.)
del s[i:j] = __delslice__(s,i,j) == s[i:j] = []
'''
class MyClass:
	"Egy egyszerű példa osztály"
	i = 42
	def f(x):
		return 'hello world!'
class a:
    def __init__(self):
        print
        "hello"

    def __del__(self):
        print
        "bye"
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
class Pont:
    """A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására. """

    def __init__(self, x=0, y=0):
        """ Egy új, origóban álló pont létrehozása. """
        self.x = x
        self.y = y

    def origotol_mert_tavolsag(self):
        """ Az origótól mért távolság számítása. """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):    # A metódus átnevezése az egyetlen feladatunk
        return "({0}, {1})".format(self.x, self.y)

    def sulypont_szamitas(self, masik_pont):
        """ A súlypontom a másik ponttal. """
        mx = (self.x + masik_pont.x) / 2
        my = (self.y + masik_pont.y) / 2
        return Pont(mx, my)
class Dolgozo:
    pass  # ez egy űres osztálydefiníció
class os:
    def __init__(self, nev="os"):
        self.nev = nev
    def print_nev(self):
        print("En", self.nev, "vagyok.")
class osbol_szarmaztatott(os):
    def __init__(self, nev):
        self.nev = nev
    def print_nev(self):
        print("Te", self.nev, "vagy.")
    def os_meghivasa(self): os.print_nev(self)
def Turtle():
    Eszti = Turtle()  # Teknőc objektumok példányosítása
    Sanyi = Turtle()
def pont_kiiras(pt):
    print("({0}, {1})".format(pt.x, pt.y))
def üresosztály():
    # Üres osztály feltöltése
    John = Dolgozo()
    John.nev = 'John Cosinus'
    John.osztaly = 'Matematikai reszleg'
    John.fizetes = 4200
    print("Teljes név: {0} Fizetés: {1} Dolgozó osztálya: {2})".format(John.nev,John.fizetes,John.osztaly))
def Alapvaltozok():
    p = Pont()  # A Pont osztály egy objektumának létrehozása (példányosítás)
    q = Pont()  # Egy második Pont objektum készítése
    # Minden Pont objektum saját x és y attribútumokkal rendelkezik
    p.x =3
    p.y=4
    q.x = 7
    q.y = 6
    print(p.x, p.y, q.x, q.y)

    p = Pont(4,2)
    q = Pont(6,3)
    r = Pont()       # r az origót (0, 0) reprezentálja
    print(p.x, q.y, r.x)
    print("(x={0}, y={1})".format(p.x, p.y))
    origotol_mert_tavolsag_negyzete = p.x * p.x + p.y * p.y

    p = Pont(3, 4)
    print(p.x)
    print(p.y)
    print(p.origotol_mert_tavolsag())

    p = Pont(3, 4)
    p = Pont(3, 4)
    print(str(p))
    print(p)

    pont_kiiras(p)

    p = Pont(3, 4)
    q = Pont(5, 12)
    r = p.sulypont_szamitas(q)
    print(r)

    print(Pont(3, 4).sulypont_szamitas(Pont(5, 12)))
def Sajátváltozók():
    b = a()
    b = None
def Adatattributumok():
    x = MyClass
    x.counter = 1
    while x.counter < 10:
        x.counter = x.counter * 2
        print(x.counter)
    del x.counter
    x = Complex(3.0, -4.5)
    print("({0}, {1})".format(x.r, x.i))
def peldamegoldas():

    nev_nelkul = os()
    nev_nelkul.print_nev()
    nevvel = os("leszarmazott")
    nevvel.print_nev()

    orokolt = osbol_szarmaztatott("masodik leszarmazott")
    orokolt.print_nev()

    orokolt.os_meghivasa()

def main():
    #Alapvaltozok()
    #Sajátváltozók()
    #Adatattributumok()
    #üresosztály()
    #peldamegoldas()
main()
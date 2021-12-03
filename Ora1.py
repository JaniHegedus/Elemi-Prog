def megtalal(c: str,s: str )->int:
    if c in s:
        #print("benne van")
        return s.index(c)
    else:
        return -1
mese=["Jack", "Kack","Lack","Mack","Nack","Oack", "Pack","Quack"]
def nevek(prefixes="JKLMNOP", suffix="ack", kisl=[]):
    for elem in prefixes:
        kisl.append(elem+suffix)
    print(kisl)
megtalal('a', "asd")

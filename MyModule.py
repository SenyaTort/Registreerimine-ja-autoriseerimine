




k=['Mari','Juku','Kati']
s=['1234','5678','abcd']

def registreerimine(k:list,s:list)->any:
    while True:
        try:
            kasutaja=input("Sisesta nimi: ")
            if kasutaja in[k]:
                print("See login on juba olemas")
            else: 
                k.append([kasutaja])
            parool = input("Sisesta parool: ")
            if (parool.isupper(), parool.isdigit(), parool.islower()):
                s.append([parool])
                print("Parooli on sobib")
            else:
                print("parool ei sobi")
        except:
            ValueError
def Autoriseerimine(k:list,s:list)->any:
    pass
def paroolivahetus(k:list,s:list)->any:
    pass
def paroolitaastamine(k:list,s:list)->any:
    pass
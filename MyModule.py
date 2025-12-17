
k=['Mari','Juku','Kati']
s=['1234','5678','abcd']

def registreerimine(k:list,s:list)->any:
    while True:
        try:
            kasutaja=input("Sisesta kasutaja nimi: ")
            if k.count(kasutaja)==1:
                print("See login on olemas")
            elif k.count(kasutaja)==0:
                k.append(kasutaja)
                parool=input("Sisesta parool: ")
                s.append(parool)
                print("parool on loodunud")
                break
        except:
            ValueError
def Autoriseerimine(k:list,s:list)->any:
    while True:
        try:
            login=input("Sisesta kasutaja nimi: ")
            if k.count(login)==1:
               parool2=input("Login on olemas, Sisesta parool: ")
               if s.count(parool2)==1:
                  print("olete sisse logitud")
               else:
                   print("Vale parool")
            else:
                print("See login ei ole")
            break
        except:
            ValueError
def paroolivahetus(k:list,s:list)->any:
    while True:
        try:
            kasutaja=input("Sisesta kasutaja nimi: ")
            if k.count(kasutaja)==1:
               vana_parool=input("Sisesta vana parool: ")
               if s.count(vana_parool)==1:
                   uus_parool=input("Sisesta uus parool: ")
                   s.remove(vana_parool)
                   s.append(uus_parool)
                   print("Parool on vahetatud")
               else:
                   print("Vale parool")
            else:
                print("See login ei ole")
            break
        except:
            ValueError
def paroolitaastamine(k:list,s:list)->any:
    while True:
        try:
            kasutaja=input("Sisesta kasutaja nimi: ")
            if k.count(kasutaja)==1:
               uus_parool=input("Sisesta uus parool: ")
               s.append(uus_parool)
               print("Parool on taastatud")
            else:
                print("See login ei ole")
            break
        except:
            ValueError
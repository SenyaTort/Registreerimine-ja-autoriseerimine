from random import  *
import string
from random import choice
k=['Mari','Juku','Kati']
s=['1234','5678','abcd']

def registreerimine(k:list,s:list)->any:
    while True:
        try:
            kasutaja=input("Sisesta kasutaja nimi: ")
            if k.count(kasutaja)==1:
                print("See login on juba olemas")
            elif k.count(kasutaja)==0:
                k.append(kasutaja)
                print("Kasutaja on registreeritud")
                gener=input("kas te soovite genereerida parooli? (y/n): ")
                if gener=="n":
                    parool=input("Sisesta parool: ") #Parool peab olema tugev(sisaldama suuri ja v�ikseid t�hti, numbreid ja s�mboleid)
                    on_num = any(char.isdigit() for char in parool)
                    on_suur = any(char.isupper() for char in parool)
                    on_vaike = any(char.islower() for char in parool)
                    on_sumbol = any(not char.isalnum() for char in parool)
                    if on_num and on_suur and on_vaike and on_sumbol and len(parool) >= 8:
                        s.append(parool)
                        print("Kasutaja on registreeritud")
                        break
                    else:
                        print("Parool ei ole piisavalt tugev") #kui parool ei �nnestunud, peaks see parooli sisestamise juurde tagasi p��rduma
                elif gener=="y":
                        import random
                        import string
                        pikkus = 12
                        tahed = string.ascii_letters
                        numbrid = string.digits
                        sumbolid = string.punctuation
                        koik = tahed + numbrid + sumbolid
                        genereeritud_parool = ''.join(random.choice(koik) for i in range(pikkus))
                        s.append(genereeritud_parool)
                        print("Genereeritud parool on: ", genereeritud_parool)
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
                print("See kasutaja ei ole")
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
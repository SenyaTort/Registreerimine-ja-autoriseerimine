from random import  *
import string
from random import choice

k=[]
s=[]

def registreerimine(k:list,s:list)->any:
    print("1-Jah")
    print("2-Ei")
    Gener=input("Kas sa tahad parooli generereida(1/2)? ")
    if Gener== "1":
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
    if Gener== "2":
        while True:
            try:
                import random
                str0 = ".,:;!_*-+()/#¤%&"
                str1 = '0123456789'
                str2 = 'qwertyuiopasdfghjklzxcvbnm'
                str3 = str2.upper()
                str4 = str0 + str1 + str2 + str3
                ls = list(str4)
                random.shuffle(ls)
                psword = ''.join([random.choice(ls) for x in range(12)])
                print(psword)
            except:
                ValueError
    else:
        print("Sisesta numbriga")
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
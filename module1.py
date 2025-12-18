from MyModule import *
k=[]
s=[]

while True:
    print("Vali tegevus: ")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Paroolivahetus")
    print("4 - Paroolitaastamine")
    print("5 - Valju")
    valik = input("Sisesta valik (1-5): ")
    if valik == '1':
        registreerimine(k, s)
    elif valik =='2':
        Autoriseerimine(k, s)
    elif valik =='3':
        paroolivahetus(k, s)
    elif valik =='4':
        paroolitaastamine(k, s)
    elif valik =='5':
        print("Valjun programmist.")
        break
    else:
        print("Vigane valik, proovi uuesti.")
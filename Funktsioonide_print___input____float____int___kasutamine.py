
#1.
#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.


#from cmath import pi


#print("Puu läbimõõdu arvutamine")
#try:
#    С=float(input("Määrake puu ümbermõõt -> "))
#    if С>0:
#        d=round(С/pi,2)
#        print(f"Puu läbimõõt on {d}")
#    else:
#        print("C peab olema suurem kui 0")
#except:
#    print("Andmetüüd on vale")


#2.
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

#from math import *
#import math

#print("ristküliku omadused")
#try:
#    M=float(input("ristküliku esimene külg -> "))
#    N=float(input("ristküliku teine külg -> "))
#    if M>0 and N>0:
#        d=math.sqrt(N**2+M**2)
#        print("ristküliku pikkus on", round(d,2))
#    else:
#        print("M ja N peab olema suurem kui 0")
#except: 
#    print("Andmetüüd on vale")

#3.
#Найдите семантическую ошибку в следующем примере программы:

#try: 
#    aeg = float(input("Mitu tundi kulus sõiduks? "))
#    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#    if aeg>0 and teepikkus>0:
#        kiirus = teepikkus / aeg
#        print("Sinu kiirus oli " + str(kiirus) + " km/h")
#    else:
#        print("aeg ja teepikkus peab olema suurem kui 0")
#except:
#    print("Andmetüüd on vale")

#4.
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvustprint

#try:
#    print("määrake mis tahes viis täisarvu")
#    a=float(input("Sisestage mis tahes täisarv -> "))
#    b=float(input("Sisestage mis tahes täisarv -> "))
#    c=float(input("Sisestage mis tahes täisarv -> "))
#    d=float(input("Sisestage mis tahes täisarv -> "))
#    e=float(input("Sisestage mis tahes täisarv -> "))
#    if a>0 and b>0 and c>0 and d>0 and e>0:
#        h=(a+b+c+d+e)/5
#        print("aritmeetiline keskmine on", h)
#    else:
#        print("a, b, c, d, e peab olema suurem kui 0")
#except:
#    print("Andmetüüd on vale")


#5.
#Joonista samasugune konn

#print("    @..@")
#print("   (----)")
#print("   ( \_/ )")
#print("^^  "" ^^ ")

#6.
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)

#from random import *

#try:
#    a=randint(0,100)
#    b=randint(0,100)
#    c=randint(0,100)
#    if a>0 and b>0 and c>0:
#        print(f"a={a}\n,b={b}\n,c={c}")
#        P=a+b+c
#        print(f"Ümbermõõt on {P}")
#    else:
#        print("a, b, c peab olema suurem kui 0")
#except:
#    print("Andmetüüd on vale")


#7.
#Pitsa
    #Võtsite P sõbraga suure pitsa hinnaga 12,90€
    #Jätate teenindajale 10% jootraha
    #Koosta programm, mis leiab kui palju peab igaüks maksma

    #from random import *

#try: 
#    P=randint(1,6)
#    summa=(12.9*1.1)/P 
#    print(f"{P}-st, Igaüks maksab {summa} ")
#except:
#    print("Andmetüüd on vale")

#8.
#Kütusekulu arvutamine

#    Kasutaja sisestab tangitud kütuse liitrid
#    Kasutaja sisestab läbitud kilomeetrid
#    Programm leiab kütusekulu 100km kohta keskmiselt

#try:
#    print("kütsusekulu arvutamine")
#    l=float(input("Kütuse liitride kogus -> "))
#    km=float(input("Läbitud kilomeetrid -> "))
#    if l>0 and km>0:
#        kulu=l/km*100
#        print(f"kütusekulu arvutamine 100 kilomeetri kohta on võrdne {kulu}")
#    else:
#        print("l ja km peab olema suurem kui 0")
#except:
#    print("Andmetüüd on vale")



#9.
#Rulluisutajad

#    Rulluisutaja keskmine kiirus on 29,9km/h
#    Kui kaugele jõuab M minutiga

#try:
#    print("Rulluisutajad")
#    M=int(input("Minutid -> "))
#    if M>0:
#        M=M/60
#        tee=M*29.9
#        print(f"Jõuab {tee} km")
#    else:
#        print("M peab olema suurem kui 0")
#except:
#    print("Andmetüüd on vale")


#10.
#Ajateisendus

#    Kasutaja sisestab aja minutites
#    Sinu valem leiab ja väljastab tunnid ja minutid
#    Näiteks: sisestus 72, vastus 1:12

#try:
#    print("Ajateisendus")
#    M=int(input("Sisesta aja minutites -> "))
#    if M>0:
#        H=M//60 #h
#        M=M%60 #min
#        print(f"{H}:{M}")
#    else:
#        print("M peab olema suurem kui 0")
#except:
#    print("Andmetüüd on vale")





#print("Ema roobot")
#a=input("Sisesta: ")
#print(a.isalpha(), a.isdigit())
#if a.isdigit() and int(a)>0 and int(a)==5:
#    a=int(a)
#    if a==5:
#        print("Hea")
#    elif a==4:
#        print("Hästi")
#    elif a==3:
#        print("Keskmine")
#    elif a==2 and a==1:
#        print("Halvasti")
#else:
#    print("Sa valesti vastas")


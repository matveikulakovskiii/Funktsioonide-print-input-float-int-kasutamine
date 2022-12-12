
#1.
#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.


#from cmath import pi


#print("Puu läbimõõdu arvutamine")
#С=float(input("Määrake puu ümbermõõt -> "))
#d=С/pi
#print("Puu läbimõõt on", round(d,2))
#print()


#2.
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

#from math import *
#import math

#print("ristküliku omadused")
#M=float(input("ristküliku esimene külg -> "))
#N=float(input("ristküliku teine külg -> "))
#c=math.sqrt(N**2+M**2)
#print("ristküliku pikkus on", round(c,2))
#print()

#3.
#Найдите семантическую ошибку в следующем примере программы:

#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = teepikkus / aeg

#print("Sinu kiirus oli " + str(kiirus) + " km/h")
#print()

#4.
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvustprint

#print("määrake mis tahes viis täisarvu")
#a=float(input("Sisestage mis tahes täisarv -> "))
#b=float(input("Sisestage mis tahes täisarv -> "))
#c=float(input("Sisestage mis tahes täisarv -> "))
#d=float(input("Sisestage mis tahes täisarv -> "))
#e=float(input("Sisestage mis tahes täisarv -> "))
#h=(a+b+c+d+e)/5
#print("aritmeetiline keskmine on", h)

#5.
#Joonista samasugune konn

#print("    @..@")
#print("   (----)")
#print("   ( \_/ )")
#print("^^  "" ^^ ")

#6.
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)

#from random import *

#a=randint(0,100)
#b=randint(0,100)
#c=randint(0,100)
#print(f"a={a}\n,b={b}\n,c={c}")
#P=a+b+c
#print(f"Ümbermõõt on {P}")


#7.
#Pitsa
#    Võtsite P sõbraga suure pitsa hinnaga 12,90€
#    Jätate teenindajale 10% jootraha
#    Koosta programm, mis leiab kui palju peab igaüks maksma

#P=randint(1,6)
#summa=(12.9*1.1)/P 
#print(f"{P}-st, Igaüks maksab {summa} ")


#8.
#Kütusekulu arvutamine

#    Kasutaja sisestab tangitud kütuse liitrid
#    Kasutaja sisestab läbitud kilomeetrid
#    Programm leiab kütusekulu 100km kohta keskmiselt

#print("kütsusekulu arvutamine")
#l=float(input("Kütuse liitride kogus -> "))
#km=float(input("Läbitud kilomeetrid -> "))
#kulu=l/km*100
#print(f"kütusekulu arvutamine 100 kilomeetri kohta on võrdne {kulu}")



#9.
#Rulluisutajad

#    Rulluisutaja keskmine kiirus on 29,9km/h
#    Kui kaugele jõuab M minutiga

#print("Rulluisutajad")
#M=int(input("Minutid -> "))
#M=M/60
#tee=M*29.9
#print(f"Jõuab {tee} km")


#10.
#Ajateisendus

#    Kasutaja sisestab aja minutites
#    Sinu valem leiab ja väljastab tunnid ja minutid
#    Näiteks: sisestus 72, vastus 1:12

#print("Ajateisendus")
#M=int(input("Sisesta aja minutites -> "))
#H=M//60 #h
#M=M%60 #min
#print(f"{H}:{M}")

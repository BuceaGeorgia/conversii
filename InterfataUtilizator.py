'''
Created on Feb 17, 2019

@author: Georgia
BUCEA GEORGIA-IOANA
GRUPA: 211
'''
from Optiuni import *
from teste import *
class UI:
    def __init__(self):
        self.__op=optiuni()
    
    def menu(self):
        print("~"*40,"MENIU","~"*40)
        print("Autor: BUCEA GEORGIA-IOANA")
        print("1.Calculeaza suma a doua numere intr-o baza b, numerele sunt in baze diferite")
        print("2.Calculeaza diferenta a doua numere intr-o baza b, numerele sunt in baze diferite")
        print("3.Calculeaza produsul dintre un numar intr-o baza data si o cifra")
        print("4.Calculeaza rezultatul impartirii unui numar intr-o baza data la o cifra")
        print("5.Efectueaza conversia rapida a unui numar din baza 2 intr-o baza  putere a lui 2")
        print("6.Efectueaza conversia rapida a unui numar dintr-o baza putere a lui 2 in baza 2")
        print("~"*87)
    
    def optiuni(self):
        while True:
            self.menu() 
            try:
                optiune=input("Da optiunea")
                if optiune=='1':
                    numar1=input("da primul numar")
                    baza1=int(input("da baza numarului"))
                    numar2=input("da al-doilea numar")
                    baza2=int(input("da baza numarului"))
                    baza3=int(input("da baza sumei"))
                    suma=self.__op.Optiunea1(numar1,baza1,numar2,baza2,baza3)
                    print("Suma celor doua numere este:",suma)
                elif optiune=='2':
                    numar1=input("da primul numar(primul numar trebuie sa fie mai mare decat cel de-al doilea numar)")
                    baza1=int(input("da baza numarului"))
                    numar2=input("da al-doilea numar")
                    baza2=int(input("da baza numarului"))
                    baza3=int(input("da baza diferentei"))
                    diferenta=self.__op.Optiunea2(numar1,baza1,numar2,baza2,baza3)
                    print("Diferenta celor doua numere este:",diferenta)
                    
                elif optiune=='3':
                    numar1=input("da numarul")
                    baza=int(input("da baza numarului"))
                    cifra=int(input("da cifra"))
                    produs=self.__op.Optiunea3(numar1, baza, cifra)
                    print("produsul dintre",numar1,"si",baza,"este",produs)
                elif optiune=='4':
                    numar1=input("da numarul")
                    baza=int(input("da baza numarului"))
                    cifra=int(input("da cifra"))
                    cat,rest=self.__op.Optiunea4(numar1, baza, cifra)
                    cat=cat.NumarulCaString(cat.getnumar())
                    print("Catul impartirii este",cat,"Restul impartirii este",rest)
                elif optiune=='5':
                    numar1=input("da numarul in baza doi")
                    baza=int(input("da baza in care se va converti"))
                    rez=self.__op.Optiunea5(numar1, baza)
                    print("Numarul convertit in baza",baza,"este:",rez)
                elif optiune=='6':
                    numar1=input("da numarul intr-o baza multiplu de doi")
                    baza=int(input("da baza numarului"))
                    rez=self.__op.Optiunea6(numar1, baza)
                    print("Numarul convertit in doi",baza,"este:",rez)
                else:
                    raise ValueError
            except ValueError:
                print("Valori introduse gresit")
    def run(self):
        self.optiuni()
                
teste()     
ui= UI()
ui.run()


'''
Created on Feb 17, 2019

@author: Georgia
BUCEA GEORGIA-IOANA
GRUPA: 211
'''
from Operatii import *


class optiuni:
    def __init__(self):
        pass
    
    
    def Optiunea1(self,numar1,baza1,numar2,baza2,baza3):
        '''
        numar1-intreg
        baza1-intreg
        numar2-intreg
        baza2-intreg
        baza3-intreg
        Returneaza un sir de caractere ce reprezinta cifrele numarului obtinut in urma operatiilor
        de adunare si conversie 
        
         '''
        numar1=numar(numar1, baza1)
        numar2=numar(numar2,baza2)
        if baza1>=baza3:
            numar1=numar1.ConversieImpartiri(baza3)
            '''convertim numarul din baza mai mare in cea 
            mica prin impartiri succesive '''
        else:
            numar1=numar1.ConversieSubstitutie(baza3)
        
        if baza2>=baza3:
            numar2=numar2.ConversieImpartiri(baza3)
        else:
            numar2=numar2.ConversieSubstitutie(baza3)
            '''convertim numarul din baza mai mica in cea mare
            prin substitutie '''
        rezultat=numar1.adunare(numar2)# adunam numerele in baza data
        rezultat=rezultat.NumarulCaString(rezultat.getnumar())
        return rezultat
    
    def Optiunea2(self,numar1,baza1,numar2,baza2,baza3):
        '''
        numar1-intreg
        baza1-intreg
        numar2-intreg
        baza2-intreg
        baza3-intreg
        Returneaza un sir de caractere ce reprezinta cifrele numarului obtinut in urma operatiilor
        de scadere si conversie 
         '''
        numar1=numar(numar1, baza1)
        numar2=numar(numar2,baza2)
        if baza1>=baza3:
            numar1=numar1.ConversieImpartiri(baza3)
            '''convertim numarul din baza mai mare in cea 
            mica prin impartiri succesive '''
        else:
            numar1=numar1.ConversieSubstitutie(baza3)
        
        if baza2>=baza3:
            numar2=numar2.ConversieImpartiri(baza3)
        else:
            numar2=numar2.ConversieSubstitutie(baza3)
            '''convertim numarul din baza mai mica in cea mare
            prin substitutie '''
        
        rezultat=numar1.scadere(numar2)#scadem numerele in baza data
        rezultat=rezultat.NumarulCaString(rezultat.getnumar())
        return rezultat
    
    def Optiunea3(self,numar1,baza,cifra):
        '''numar1-intreg
            baza-intreg
            cifra-intreg
            Returneaza un string, cifrele numarului rezultat dupa inmultire
         '''
        numar1=numar(numar1, baza)
        rezultat=numar1.inmultire(cifra)
        rezultat=rezultat.NumarulCaString(rezultat.getnumar())
        return rezultat
    
    def Optiunea4(self,numar1,baza,cifra):
        '''numar1-intreg
            baza-intreg
            cifra-intreg
            Returneaza un string, cifrele numarului rezultat dupa impartire
         '''
        numar1=numar(numar1, baza)
        rezultat=numar1.impartire(cifra)
        return rezultat
    
    def Optiunea5(self,numar1,baza):
        '''numar1-int
           baza-int
           Returneaza un string, cifrele numarului rezultat dupa conversie '''
        numar1=numar(numar1,2)
        rezultat="Date incorecte"
        if baza==4:
            rezultat=numar1.conversierapida4(4)
        if baza==8:
            rezultat=numar1.conversierapida8(8)
        if baza==16:
            rezultat=numar1.conversierapida16(16) 
        return rezultat 
    
    def Optiunea6(self,numar1,baza):
        '''numar1-int
           baza-int
           Returneaza un string, cifrele numarului rezultat dupa conversie '''
        numar1=numar(numar1, baza)
        rezultat="Date incorecte"
        if baza==4:
            rezultat=numar1.conversierapida4(2)
        if baza==8:
            rezultat=numar1.conversierapida8(2)
        if baza==16:
            rezultat=numar1.conversierapida16(2) 
        return rezultat 
              
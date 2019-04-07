'''
Created on Feb 16, 2019

@author: Georgia
BUCEA GEORGIA-IOANA
GRUPA:211
'''

import copy
class numar:
    def __init__(self,numar,baza):
        #se retine baza ca intreg si numarul ca sirul cifrelor sale
        self.__numar=self.SirCifreNumar(str(numar))
        self.__baza=int(baza)
        
    def getnumar(self):
        #returneaza o copie a numarului
        nm=copy.deepcopy(self.__numar)
        return nm
    
    def getbaza(self):
        #returneaza baza numarului
        return self.__baza
    
    def setnumar(self,nm):
        self.__numar=nm
        
    def setbaza(self,bz):
        self.__baza=bz
        
    def StringToInt(self,element):
        '''element-string
        returneaza un intreg care reprezinta valoarea numerica a simbolului in baza 10
         '''
        if element=='A':
            element=10
        elif element=='B':
            element=11
        elif element=='C':
            element=12
        elif element=='D':
            element=13
        elif element=='E':
            element=14
        elif element=='F':
            element=15
        else:
            element=int(element)
        return element
    
    def SirCifreNumar(self,numar):
        '''
        numar-string
        returneaza un sir cu cifrele numarului scrise in ordine inversa '''
        lista=[]
        for el in numar: 
            el=self.StringToInt(el)
            lista.append(el)
        lista.reverse()
        return lista
            
    def inmultire(self,cifra):
        '''cifra-numar integ cu care va fi inmultit numarul dat
           returneaza un obiect de tip numar care retine numarul obtinut dupa inmultire
           si baza acestuia
          '''
        cifreNumar=self.__numar
        t=0
        final=[]
        for i in range(len(cifreNumar)):
            var=cifreNumar[i]*cifra+t
            final.append(var%self.__baza)
            t=var//self.__baza
        if t!=0:
            final.append(t)
        
        numarul=self.NumarulCaString(final)
        rezultat=numar(numarul,self.getbaza())
        return rezultat
    
    
    def NumarulCaString(self,cifre):
        '''
         cifre-lista ce contine cifrele numarului 
         retuneaza numarul sub forma unui string inlocuind cifrele
         corespunzatoare cu simboluri(A-F)
        '''
        for i in range(len(cifre)):
            if cifre[i]==10:
                cifre[i]='A'
            elif cifre[i]==11:
                cifre[i]='B'
            elif cifre[i]==12:
                cifre[i]='C'
            elif cifre[i]==13:
                cifre[i]='D'
            elif cifre[i]==14:
                cifre[i]='E'
            elif cifre[i]==15:
                cifre[i]='F'
            else:
                cifre[i]=str(cifre[i])
        cifre.reverse()
        rez=''.join(cifre)
        
        return rez
            
        
    def impartire(self,cifra):
        '''cifra-numar integ cu care va fi impartit numarul dat
        returneaza un obiect de tip numar care retine numarul obtinut dupa impartire
        si baza acestuia
         '''
        poz=self.getnumar()
        t=0
        final=[]
        for i in range(len(poz)-1,-1,-1):
            var=self.__baza*t+poz[i]
            final.append(var//cifra)
            t=var%cifra
        
        if final[0]==0 and len(final)>1:
            final=final[1:]
            
        final.reverse()
        nm=self.NumarulCaString(final)
        fin=numar(nm,self.getbaza())
        return fin,t
    
    def adunare(self,numar2):
        '''numar2-obiect de tip numar, numarul cu care se va aduna
        returneaza un obiect de tip numar care retine numarul obtinut in urma adunarii 
        si baza acestuia
         '''
        cifreNumar=self.__numar
        cifreNumar2=numar2.getnumar()
        diferentaDeLungime=abs(len(cifreNumar2)-len(cifreNumar))
        if len(cifreNumar2)>len(cifreNumar):#daca lungimile sunt diferite numerele sunt extinse
            cifreNumar.extend([0]*diferentaDeLungime) 
        else:
            cifreNumar2.extend([0]*diferentaDeLungime)
        transport=0
        rez=[]
        for i in range(len(cifreNumar)): #se parcurg numerele si se realizeaza adunarea
            var=cifreNumar[i]+cifreNumar2[i]+transport
            transport=var//self.__baza
            rez.append(var%self.__baza)
        
        if transport!=0:
            rez.append(transport)
        numarCaString=self.NumarulCaString(rez)
        rezultatulFinal=numar(numarCaString,self.getbaza())
        return rezultatulFinal
    
    
    
    def ConversieImpartiri(self,baza):
        '''
        baza-numar natural format dintr-o cifra reptrezentand baza
        la care trebuie convertit numarul initial
        
        returneaza un obiect care reprezinta numarul initial actualizat in noua baza
        numarul initial poate sa fie in orice baza pana la 16
         '''
        rezultat=[]      #la inceput lista rezultat este vida 
               
        numarulFinal=self         # obiectul numarulFinal ia valorile initiale ale numarului
        
        while numarulFinal.getnumar()!=[0]:   #ca timp numarul mai poate fi impartit la baza rezultat
            
            numarulFinal,rest=numarulFinal.impartire(baza) #numarul curent este impartit cu algoritmul 
                                         # de impartire la o anumita baza 
            rezultat.append(rest)        #restul este adaugat la rezultat
        
        numarCaString=self.NumarulCaString(rezultat)
        numarulFinal=numar(numarCaString, baza)
        return numarulFinal
     
    def ConversieSubstitutie(self,baza):
        '''baza-numar intreg, baza in care se va converti numarul
        Returneaza un obiect de tip numar ce retine valoarea numarului dupa 
        conversie si baza acestuia
         '''
        bazaInitiala=self.getbaza()
        ValoareInitialaNumar=self.getnumar()
        Rezultat=numar(str(ValoareInitialaNumar[0]),baza)
        inter=numar('1', baza)
        for i in range(1,len(self.getnumar())):
              inter=inter.inmultire(bazaInitiala)
              almost=inter.inmultire(ValoareInitialaNumar[i])
              Rezultat=Rezultat.adunare(almost)
        return Rezultat
                   
    
    def scadere(self,numar2):
        '''numar2-obiect de tip numar, scazatorul
        Returneaza un obiect de tip numar ce retine numarul dupa efectuarea
        operatiei si baza acestuia
         '''
        CifrePrimulNumar=self.__numar
        CifreAlDoileaNumar=numar2.getnumar()
        diferentaLungimilor=abs(len(CifreAlDoileaNumar)-len(CifrePrimulNumar))
        
        if len(CifreAlDoileaNumar)>len(CifrePrimulNumar):
            CifrePrimulNumar.extend([0]*diferentaLungimilor)
            
        else:
            CifreAlDoileaNumar.extend([0]*diferentaLungimilor)
            
        imprumut=0
        sirRezultat=[]
        
        for i in range(len(CifrePrimulNumar)):
            
            if CifrePrimulNumar[i]+imprumut>=CifreAlDoileaNumar[i]:
                sirRezultat.append(CifrePrimulNumar[i]-CifreAlDoileaNumar[i]+imprumut)
                imprumut=0
                
            else:
                sirRezultat.append(CifrePrimulNumar[i]+self.getbaza()-CifreAlDoileaNumar[i]+imprumut)
                imprumut=-1
                
        sirnumar=self.NumarulCaString(sirRezultat)
        numarfinal=numar(sirnumar,self.getbaza())
        return numarfinal
    
    def conversierapida16(self,baza):
        '''baza - numar intreg, putere a lui 2
        Returneaza un string cu cifrele numarului de dupa conversie '''
        dictionar={
               "0000":0,
               "0001":1,
               "0010":2,
               "0011":3,
               "0100":4,
               "0101":5,
               "0110":6,
               "0111":7,
               "1000":8,
               "1001":9,
               "1010":10,
               "1011":11,
               "1100":12,
               "1101":13,
               "1110":14,
               "1111":15,
                    }
        dictionar2= {v: k for k, v in dictionar.items()}
        if baza==16:
            numar1=self.getnumar()
            if len(numar1)%4!=0:
                numar1.extend([0]*(4-len(numar1)%4))
            lis=[''.join(str(e) for e in reversed(numar1[i:i + 4])) for i in range(0, len(numar1), 4)]
            for i in range(len(lis)):
                lis[i]=dictionar[lis[i]]
            final=lis
            
        else:
            lis=self.getnumar()
            final=[]
            for i in range(len(lis)):
                lista=list(dictionar2[lis[i]])
                lista.reverse()
                lista=[int(el) for el in lista]
                final.extend(lista)
            while final[-1]==0:
                final.pop(-1)
                
        final=self.NumarulCaString(final)
        return(final)
                    
    def conversierapida8(self,baza):
        '''baza - numar intreg, putere a lui 2
        Returneaza un string cu cifrele numarului de dupa conversie'''
        dictionar={
               "000":0,
               "001":1,
               "010":2,
               "011":3,
               "100":4,
               "101":5,
               "110":6,
               "111":7,
                    }
        dictionar2= {v: k for k, v in dictionar.items()}
        if baza==8:
            numar1=self.getnumar()
            if len(numar1)%3!=0:
                numar1.extend([0]*(3-len(numar1)%3))
            lis=[''.join(str(e) for e in reversed(numar1[i:i + 3])) for i in range(0, len(numar1), 3)]
            for i in range(len(lis)):
                lis[i]=dictionar[lis[i]]
            final=lis
            
        else:
            lis=self.getnumar()
            final=[]
            for i in range(len(lis)):
                lista=list(dictionar2[lis[i]])
                lista.reverse()
                lista=[int(el) for el in lista]
                final.extend(lista)
            while final[-1]==0:
                final.pop(-1)
                
        final=self.NumarulCaString(final)
        return final
    
    def conversierapida4(self,baza):
        '''baza - numar intreg, putere a lui 2
        Returneaza un string cu cifrele numarului de dupa conversie'''
        dictionar={
               "00":0,
               "01":1,
               "10":2,
               "11":3,
                    } 
        dictionar2= {v: k for k, v in dictionar.items()}
        if baza==4:
            numar1=self.getnumar()
            if len(numar1)%2!=0:
                numar1.extend([0]*(2-len(numar1)%2))
            lis=[''.join(str(e) for e in reversed(numar1[i:i + 2])) for i in range(0, len(numar1), 2)]
            for i in range(len(lis)):
                lis[i]=dictionar[lis[i]]
            final=lis
            
        else:
            lis=self.getnumar()
            final=[]
            for i in range(len(lis)):
                lista=list(dictionar2[lis[i]])
                lista.reverse()
                lista=[int(el) for el in lista]
                final.extend(lista)
            while final[-1]==0:
                final.pop(-1)
                
        final=self.NumarulCaString(final)
        return(final)
        
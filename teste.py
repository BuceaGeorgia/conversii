'''
Created on Feb 16, 2019

@author: Georgia
BUCEA GEORGIA-IOANA
GRUPA: 211
'''

from Operatii import *
from _ast import Num

def teste():
    n=numar("1AB2",16)
    m=numar("12",16)
    num=n.SirCifreNumar(n.getnumar())
    assert(len(num)==4)
    p=n.adunare(m)
    p=n.NumarulCaString(p.getnumar())
    assert(p=="1AC4")
    l=numar("12",10).adunare(numar("1234", 10))
    l=n.NumarulCaString(l.getnumar())
    assert(l=="1246")
    
    l=numar("123",4).adunare(numar("1233",4))
    l=n.NumarulCaString(l.getnumar())
    assert(l=="2022")
    
    l=numar("A",16).adunare(numar("12A",16))
    l=n.NumarulCaString(l.getnumar())
    assert(l=="134")
    
    
    l=numar("123A",16).scadere(numar("1A",16))
    l=n.NumarulCaString(l.getnumar())

    assert(l=="1220")
    
    l=numar("123AB",15).scadere(numar("1304",15))
    l=n.NumarulCaString(l.getnumar())

    assert(l=="110A7")
    
    l=numar("120709",11).scadere(numar("12A3",11))
    l=n.NumarulCaString(l.getnumar())

    assert(l=="11A416")
    
    l=numar("5",10).scadere(numar("2",10))
    l=n.NumarulCaString(l.getnumar())

    assert(l=="3")
    
    p=n.ConversieImpartiri(2)
    p=n.NumarulCaString(p.getnumar())
    assert (p=="1101010110010")
    
    p=numar("A123",16).ConversieImpartiri(13)
    p=n.NumarulCaString(p.getnumar())
    assert (p=="15A12")
    
    p=numar("A12332B",16).ConversieImpartiri(5)
    p=n.NumarulCaString(p.getnumar())
    assert (p=="321223334112")
    
    l=numar("123",4).ConversieSubstitutie(16)
    l=l.NumarulCaString(l.getnumar())
    assert(l=="1B") 
    l=numar("11100110",2).ConversieSubstitutie(16)
    l=l.NumarulCaString(l.getnumar())
    assert(l=="E6")
    l=numar("1235465",7).ConversieSubstitutie(13)
    l=l.NumarulCaString(l.getnumar())
    assert(l=="58034")
    l=numar("12354A5",13).ConversieSubstitutie(16)
    l=l.NumarulCaString(l.getnumar())
    assert(l=="56783A")
    nn=numar("213111221",4)
    la=nn.conversierapida4(2)
    assert(la=="100111010101101001")
    nm=numar("AB120A",16)
    la=nm.conversierapida16(2)
    assert(la=="101010110001001000001010")
    nm=numar("101010110001001000001010",2)
    la=nm.conversierapida16(16)
    assert(la=="AB120A")
    nm=numar("123765",8)
    la=nm.conversierapida8(2)
    assert(la=="1010011111110101")
    nm=numar("12123", 4)
    la=nm.conversierapida4(2)
    assert(la=="110011011")
    nm=numar("10100111001001", 2)
    la=nm.conversierapida16(16)
    assert(la=="29C9")
    la=nm.conversierapida4(4)
    assert(la=="2213021")
    la=nm.conversierapida8(8)
    assert(la=="24711")
    

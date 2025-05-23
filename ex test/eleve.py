from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem
e=dict(nom=str,classe=str,num=str,genre=str)
from pickle import load,dump

def verif(ch):
    i=0
    test=True
    while i<len(ch) and test==True:
        if "A"<=ch[i]<="Z" or "a"<=ch[i]<="z":
            i+=1
        else:
            test=False
    return test

def ajout():
    f=open("eleve.dat","ab")
    nom=w.l1.text()
    classe=w.l2.text()
    num=w.l3.text()
    hom=w.rh.ischecked()
    fem=w.rf.ischecked()
    if hom:
        genre=w.rh.text()
    elif fem:
        genre=w.rf.text()
    if not (verif(nom) and nom!="" and "1"<=classe<="4" and "1000"<=num<="9999" and genre!=""):
        QMessageBox.critical(w,"error!","Voud devez saisissez  des donnéés valides !")
    else:
        e["nom"]=nom
        e["classe"]=classe
        e["num"]=num
        e["genre"]=genre
        dump(e,f)
        QMessageBox.information(w,"info","ajout avec succés")
    w.l1.clear()
    w.l2.clear()
    w.l3.clear()
    w.rh.clear()
    w.rf.clear()
    f.close()

def afficher():
    f=open("eleve.dat","rb")
    tbw.setRowCount(20)
    tbw.setColumnCount(4)
    fin=False
    i=0
    while fin==False:
        try:
            e=load(f)
            w.tbw.setItem(i,0,QTableWidgetItem(e["nom"]))
            w.tbw.setItem(i,1,QTableWidgetItem(e["classe"]))
            w.tbw.setItem(i,2,QTableWidgetItem(e["num"]))
            w.tbw.setItem(i,3,QTableWidgetItem(e["genre"]))
            i+=1
        except:
            fin=True
    f.close()
    
def remlplirlist():
    f=open("eleve.dat","rb")
    f2=open("liste.txt","w")
    fin=False
    while fin==False:
        try:
            e=load(f)
            if e["classe"]=="4":
                f2.write(e["nom"]+"\n")
        except:
            fin=True
    f2.close()
    f.close()

def afflist():
    remlplirlist()
    f2=open("liste.txt","r")
    ch=f2.readline()
    ch=ch[:len(ch)-1]
    while ch!="":
        w.lw.addItem(ch)
        ch=f2.readline()
        ch=ch[:len(ch)-1]
    f2.close()
 
 
        
app = QApplication([]) 
w = loadUi("act1.ui") 
w.show() 
w.ajt.clicked.connect (ajout)
w.aff.clicked.connect(afficher)
w.bac.clicked.connect(afflist)
app.exec_()
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from random import *
from pickle import dump,load


def verifid(id):
    '''cette fonction permet de vérifier si l’identifiant saisi
        par l’élève est formé par 8 chiffres '''
    return (id.isdecimal() and len(id)==8 )
        



def generer():
    '''cette fonction permet de générer aléatoirement une expression arithmétique à partir du
        fichier "Expressions.txt".'''
    
    f = open("Expressions.txt","r")
    n = randint(1,20) #20 représente le nombre d'expressions contenues dans le fichier Expressions.txt
    for i in range (n) :
        e = f.readline()   
    f.close()
    return e
    
def afficher ():
    '''ce module permet d'afficher dans le label labExp une expression générée aléatoirement dans le cas
         où l'identifiant saisi est valide'''
    id = fen.txtid.text()
    if not verifid(id) :
        QMessageBox.critical(fen,'Erreur',"Veuillez saisir un identifiant valide composé de 8 chiffres")
    else :
        e = generer()
        fen.labExp.setText(e)



def evaluation_somme(ch):
    symbol = ch.find("+")
    if symbol == len(ch) - 1:
        return int(ch[:symbol])
    else:
        return int(ch[:symbol]) + evaluation_somme(ch[symbol + 1:])
    
def evaluation_sub(ch):
    symbol = ch.find("-")
    if symbol == len(ch) - 1:
        return int(ch[:symbol])
    else:
        return int(ch[:symbol]) - evaluation_sub(ch[symbol + 1:])

def evaluation_multi(ch):
    symbol = ch.find("*")
    if symbol == len(ch) - 1:
        return int(ch[:symbol])
    else:
        return int(ch[:symbol]) * evaluation_multi(ch[symbol + 1:])
    
def recherche(ch):
    i = 0
    test = True
    while (i != len(ch) and test != False ):
        if ch[i].isdecimal() == True:
            i += 1
        else:
            test = False
            res = ch[i]
    return res

def evaluer(ch):
    symbol = recherche(ch)
    if symbol == "+":
        ch += "+"
        return evaluation_somme(ch)
    elif symbol == "-":
        ch += "-"
        return evaluation_sub(ch)
    else:
        ch += "*"
        return evaluation_multi(ch)

def valide():
    id = fen.textid.text()
    rep = fen.txtrep.text()
    exp = fen.labExp.text()
    E = {
        "id": str,
        "exp": str,
        "rep": str,
        "valide":str
    }
    if verifid(id) == False:
        QMessageBox.critical(fen, "erreur", "identifiant non valide")
    elif rep != str(evaluer(exp)):
        QMessageBox.critical(fen, "Conclusion", "Réponse erronée")
        f = open("Evaluation.dat","ab")
        E["id"] = id
        E["exp"] = exp
        E["rep"] = rep
        E["valide"] = "faux"
        dump(E,f)
        f.close()
    else:
        QMessageBox.critical(fen, "Conclusion", "Réponse correcte")
        f = open("Evaluation.dat","ab")
        E["id"] = id
        E["exp"] = exp
        E["rep"] = rep
        E["valide"] = "vrai"
        dump(E,f)
        f.close()






#Programme principal
app=QApplication([])
fen = loadUi ("Interface_Evaluation.ui")
fen.show()
fen.btnExp.clicked.connect(afficher)
fen.btnRes.clicked.connect(valide)
app.exec()

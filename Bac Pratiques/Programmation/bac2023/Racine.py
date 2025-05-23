from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import load, dump


def puissance(x, p):
    r = 1
    for i in range(p):
        r *= x
    return r


def grand_entier(x):
    p = 1
    while not (puissance(p, 2) > x):
        p += 1
    return p - 1


def suite(n, x):
    if  n == 0:
        return grand_entier(x)
    else:
        return (1/2) * (suite(n - 1, x) + (x / suite(n - 1, x)))
    
    
def calcul(eps, x):
    i = 1
    U_initiale = suite(i - 1, x)
    U_finale = suite(i, x)
    while not abs(U_finale - U_initiale) <= eps:
        i += 1
        U_initiale = suite(i - 1, x)
        U_finale = suite(i, x)
    else:
        return U_finale
    
    
def racine():
    approchee = open("approchee.dat", "ab")
    E = {
        "x": int(),
        "RC": int()
    }
    x = w.num.text()
    
    if x.isdecimal() == False:
        QMessageBox.critical(w, "Erreur", "Veuillez saisir une valeur numerique")
    elif x == "":
        QMessageBox.critical(w, "Erreur", "Veuillez saisir une valeur numerique")
    elif not(2 <= int(x) <= 200):
        QMessageBox.critical(w, "Erreur", "Veuillez saisir une valeur entre 2 et 200")
    else:
        i = 1
        E["x"] = int(x)
        E["RC"] = calcul(0.00001, int(x))
        dump(E, approchee)
        approchee.close()
        
        
def afficher():
    approchee = open("approchee.dat", "rb")
    Fin_Ficher = False
    while Fin_Ficher == False:
        try:
            E = load(approchee)
            w.TAB.setItem(i, 0, QTableWidgetItem(E["x"]))
            w.TAB.setItem(i, 1, QTableWidgetItem(E["RC"]))
            i += 1
        except:
            Fin_Ficher == True
    approchee.close()
    
    
app = QApplication([])
w = loadUi("Interface_Racine.ui")
w.show()
w.BtnAj.clicked.connect(racine)
w.BtnAff.clicked.connect(afficher)
app.exec()
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from numpy import array


def suite(H):
    if H == 2 or H == 1:
        return 1
    else:
        return suite(H - 1) + suite(H - 2)

def verif(H):
    if int(H) < 1 or H == "" or H.isdecimal() == False:
        return False
    else:
        return True


def afficherCrois():
    H = w.variableH.Text()
    currentH = 1
    s = 0
    if int(H) < 1:
        QMessageBox.critical(w, "erreur", "H doit etre >= 1")
    elif H == "":
        QMessageBox.critical(w, "erreur", "veuillez saisir la valeur de H")
    elif H.isdecimal() == False:
        QMessageBox.critical(w, "erreur", "H doit etre un nombre")
    else:
        M = array([[int()] * 3] * int(H))
        for i in range(H):
            for j in range(3):
                if j != 2:
                    if i == 0 and j == 0:
                        M[i, j] = 1
                    elif i == 0 and j == 1:
                        M[i, j] = 0
                    else:
                        if j == 0:
                            M[i, j] = M[i - 1, j + 1]
                        elif j == 1:
                            M[i, j] = M[i - 1, j - 1] + M[i - 1, j]
                else:
                    M[i,j] = suite(currentH)
                    currentH += 1
        currentH = 1
        while s != int(H):
            w.TW.setItem(s, 0, QTableWidgetItem("H" + str(currentH)))
            w.TW.setItem(s, 1, QTableWidgetItem(M[s,0]))
            w.TW.setItem(s, 2, QTableWidgetItem(M[s,1]))
            w.TW.setItem(s, 3, QTableWidgetItem(M[s,2]))
            s += 1
            currentH += 1
        
    
    
    
    
    
    
    
    
    
    
app = QApplication([])
w = loadUi("Interface.ui")
w.show()
w.BtnC.clicked.connect(afficherCrois)
app.exec()
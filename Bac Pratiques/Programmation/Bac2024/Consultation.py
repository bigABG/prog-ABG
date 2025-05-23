from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import load
from Evaluation import recherche

def consulter():
    op = fen.cmbOp.currentIndex()
    f = open("Evaluation.dat","rb")
    Fin_Ficher = False
    i = 0
    while Fin_Ficher == False:
        try:
            E = load(f)
            if op == recherche(E["exp"]):
                fen.tw1.insertRow(i)
                fen.tw1.setItem(i, 0, QTableWidgetItem(str(E["id"])))
                fen.tw1.setItem(i, 1, QTableWidgetItem(str(E["exp"])))
                fen.tw1.setItem(i, 1, QTableWidgetItem(str(E["rep"])))
                fen.tw1.setItem(i, 1, QTableWidgetItem(str(E["valide"])))
                i += 1
        except:
            Fin_Ficher == True
            f.close()

# Programme principal à compléter
app=QApplication([])
fen = loadUi ("Interface_Consultation.ui")
fen.show()
fen.btnAff.clicked.connect(consulter)
app.exec()

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from optmizations import (BeltFactory, Bootmaker, Company, ProductFactory,
                          TVProgram)


class Ui_View(object):
    def setupUi(self, View):
        View.setObjectName("View")
        View.resize(753, 431)
        self.centralwidget = QtWidgets.QWidget(View)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 181, 17))
        self.label.setObjectName("label")
        self.cbAlgorithm = QtWidgets.QComboBox(self.centralwidget)
        self.cbAlgorithm.setGeometry(QtCore.QRect(10, 60, 231, 25))
        self.cbAlgorithm.setObjectName("cbAlgorithm")
        self.cbAlgorithm.addItem("")
        self.cbAlgorithm.addItem("")
        self.cbAlgorithm.addItem("")
        self.cbAlgorithm.addItem("")
        self.cbAlgorithm.addItem("")
        self.cbAlgorithm.addItem("")
        self.cbAlgorithm.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 191, 17))
        self.label_2.setObjectName("label_2")
        self.cbProblem = QtWidgets.QComboBox(self.centralwidget)
        self.cbProblem.setGeometry(QtCore.QRect(310, 60, 231, 25))
        self.cbProblem.setObjectName("cbProblem")
        self.cbProblem.addItem("")
        self.cbProblem.addItem("")
        self.cbProblem.addItem("")
        self.cbProblem.addItem("")
        self.cbProblem.addItem("")
        self.solutionPanel = QtWidgets.QTextEdit(self.centralwidget)
        self.solutionPanel.setGeometry(QtCore.QRect(10, 100, 731, 301))
        self.solutionPanel.setObjectName("solutionPanel")
        self.btnSolve = QtWidgets.QPushButton(self.centralwidget)
        self.btnSolve.setGeometry(QtCore.QRect(620, 60, 121, 25))
        self.btnSolve.setObjectName("btnSolve")
        self.btnSolve.clicked.connect(self.run_algorithm)
        View.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(View)
        self.statusbar.setObjectName("statusbar")
        View.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(View)
        self.actionSair.setObjectName("actionSair")

        self.retranslateUi(View)
        QtCore.QMetaObject.connectSlotsByName(View)

    def retranslateUi(self, View):
        _translate = QtCore.QCoreApplication.translate
        View.setWindowTitle(_translate("View", "Otimizações com Gurobi"))
        self.label.setText(_translate("View", "Selecione um algoritmo:"))
        self.cbAlgorithm.setItemText(0, _translate("View", "Automático"))
        self.cbAlgorithm.setItemText(1, _translate("View", "Primal Simplex"))
        self.cbAlgorithm.setItemText(2, _translate("View", "Dual Simplex"))
        self.cbAlgorithm.setItemText(3, _translate("View", "Barrier"))
        self.cbAlgorithm.setItemText(4, _translate("View", "Concurrent"))
        self.cbAlgorithm.setItemText(5, _translate("View", "Deterministic concurrent"))
        self.cbAlgorithm.setItemText(6, _translate("View", "Deterministic concurrent simplex"))
        self.label_2.setText(_translate("View", "Selecione um problema:"))
        self.cbProblem.setItemText(0, _translate("View", "Sapateiro"))
        self.cbProblem.setItemText(1, _translate("View", "Fábrica de produtos"))
        self.cbProblem.setItemText(2, _translate("View", "Rede de TV"))
        self.cbProblem.setItemText(3, _translate("View", "Fábrica de cintos"))
        self.cbProblem.setItemText(4, _translate("View", "Racionalização de recursos"))
        self.btnSolve.setText(_translate("View", "Resolver"))
        self.actionSair.setText(_translate("View", "Sair"))
    
    def run_algorithm(self):
        self.solutionPanel.setText("")
        choice = self.cbProblem.currentIndex()
        algorithm = -1 if self.cbAlgorithm.currentIndex() == 0 else self.cbAlgorithm.currentIndex()
        model = None
        if choice == 0:
            model = Bootmaker("sapateiro", algorithm=algorithm)
            model.message("Quantidade de sapato e cinto que maximizam os lucros")
        elif choice == 1:
            model = ProductFactory("produto", algorithm=algorithm)
            model.message("Quantidade do produto P1 e P2 que maximizam os lucros")
        elif choice ==2:
            model = TVProgram("TV", algorithm=algorithm)
            model.message("Quantidade de exibições semanais dos programas A e B")
        elif choice == 3:
            model = BeltFactory("cinto", algorithm=algorithm)
            model.message("Quantidade de cinto M1 e M2")
        elif choice == 4:
            model = Company("empresa", algorithm=algorithm)
            model.message("Quantidade de P1 e P2 mensal que maximizam os lucros")
        
        json, variables = model.optimize()
        
        response = self._get_formated_response(json)

        text = model.get_message()

        for v in variables:
            text += f"Qtd. {v.varName}: {int(v.x)}\n"
        
        text += response

        self.solutionPanel.setText(text)

    def _get_formated_response(self, json) -> str:
        solution = json["SolutionInfo"]
        text = "\nLucro resultante R$ {:.2f}".format(float(solution['ObjVal']))
        return text

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    View = QtWidgets.QMainWindow()
    ui = Ui_View()
    ui.setupUi(View)
    View.show()
    sys.exit(app.exec_())

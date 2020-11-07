import gurobipy as gb
from gurobipy import GRB
from decimal import Decimal
from abc import ABC
import abc

class Base(ABC):
    """
        This abstract base class to model optimizations
    """

    def __init__(self, name="default"):
        self._message = ""
        self.model = gb.Model(name)
    
    def message(self, message: str):
        """ set a message for min or max objective """
        self._message = message

    @abc.abstractmethod
    def settings(self):
        """ set decision variables and restrictions to optimization problem """
        pass

    def show(self):
        """ show variables that maximize or minimize the objective """
        objective = self.settings()
        print(self._message)
        for v in self.model.getVars():
            print(f"{v.varName}: {int(v.x)}")

        print('\nLucro obtido: R$ {:.2f}'.format(round(objective.getValue(), 2)))
    
    def optimize(self):
        """ run the gurobi optimization"""
        self.show()


class Bootmaker(Base):

    def settings(self):
        # VD
        x = self.model.addVar(name="sapato")   # qtd de sapatos produzidos por hora
        y = self.model.addVar(name="cinto")    # qtd de cintos produzidos por hora

        # FO MAX L
        objective = 5*x + 2*y
        self.model.setObjective(objective, GRB.MAXIMIZE)

        # SA:
        self.model.addConstr(10*x + 12*y <= 60, "sa1")
        self.model.addConstr(2*x + y <= 6, "sa2")

        self.model.optimize()

        return objective


class ProductFactory(Base):

    def settings(self):

        x = self.model.addVar(name="P1")
        y = self.model.addVar(name="P2")

        objective = 100*x + 150*y
        self.model.setObjective(objective, GRB.MAXIMIZE)

        self.model.addConstr(2*x + 3*y <=120)
        self.model.addConstr(x <=40)
        self.model.addConstr(y <=30)

        self.model.optimize()

        return objective

class TVProgram(Base):
    
    def settings(self):

        x = self.model.addVar(name="A")
        y = self.model.addVar(name="B")

        objective = 30000*x + 10000*y
        self.model.setObjective(objective, GRB.MAXIMIZE)

        self.model.addConstr(20*x + 10*y <=80)
        self.model.addConstr(x + y >=5)

        self.model.optimize()

        return objective

class BeltFactory(Base):
    
    def settings(self):
        x = self.model.addVar(name="M1")
        y = self.model.addVar(name="M2")

        objective = 4*x + 3*y
        self.model.setObjective(objective, GRB.MAXIMIZE)

        self.model.addConstr(2*x + y <=1000)
        self.model.addConstr(x + y <=800)
        self.model.addConstr(x <=400)
        self.model.addConstr(y <=700)

        self.model.optimize()

        return objective

class Company(Base):
    
    def settings(self):
        x = self.model.addVar(name="P1")
        y = self.model.addVar(name="P2")

        objective = 120*x + 150*y
        self.model.setObjective(objective, GRB.MAXIMIZE)

        self.model.addConstr(2*x + 4*y <=100)
        self.model.addConstr(3*x + 2*y <=90)
        self.model.addConstr(5*x + 3*y <=120)

        self.model.optimize()

        return objective
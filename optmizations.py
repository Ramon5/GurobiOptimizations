import abc
import json
from decimal import Decimal

import gurobipy as gb
from gurobipy import GRB


class Base(abc.ABC):
    """
        This abstract base class to model optimizations
    """

    def __init__(self, name="default", algorithm=-1):
        self._message = ""
        self.model = gb.Model(name)
        self.model.setParam(GRB.Param.OutputFlag, 0)
        self.model.setParam(GRB.Param.Method, algorithm)
    
    def message(self, message: str):
        """
            set a message for min or max objective
        """
        self._message = message
    
    def get_message(self) -> str:
        return f"{self._message}\n\n"

    @abc.abstractmethod
    def settings(self):
        """ set decision variables and restrictions to optimization problem """
        pass
    
    def optimize(self):
        """ run the gurobi optimization"""
        return self.settings()


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

        return json.loads(self.model.getJSONSolution()), self.model.getVars()


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

        return json.loads(self.model.getJSONSolution()), self.model.getVars()

class TVProgram(Base):
    
    def settings(self):

        x = self.model.addVar(name="A")
        y = self.model.addVar(name="B")

        objective = 30000*x + 10000*y
        self.model.setObjective(objective, GRB.MAXIMIZE)

        self.model.addConstr(20*x + 10*y <=80)
        self.model.addConstr(x + y >=5)

        self.model.optimize()

        return json.loads(self.model.getJSONSolution()), self.model.getVars()

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

        return json.loads(self.model.getJSONSolution()), self.model.getVars()

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

        return json.loads(self.model.getJSONSolution()), self.model.getVars()
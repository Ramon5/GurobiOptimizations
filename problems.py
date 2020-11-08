import json
from decimal import Decimal

from base import GRB, Base


class Bootmaker(Base):
    def settings(self):
        # VD
        x = self.model.addVar(name="sapato")  # qtd de sapatos produzidos por hora
        y = self.model.addVar(name="cinto")  # qtd de cintos produzidos por hora

        # FO MAX L
        self.model.setObjective(5 * x + 2 * y, GRB.MAXIMIZE)

        # SA:
        self.model.addConstr(10 * x + 12 * y <= 60, "sa1")
        self.model.addConstr(2 * x + y <= 6, "sa2")

        self.model.optimize()

        return json.loads(self.model.getJSONSolution())


class ProductFactory(Base):
    def settings(self):

        x = self.model.addVar(name="P1")
        y = self.model.addVar(name="P2")

        self.model.setObjective(100 * x + 150 * y, GRB.MAXIMIZE)

        self.model.addConstr(2 * x + 3 * y <= 120)
        self.model.addConstr(x <= 40)
        self.model.addConstr(y <= 30)

        self.model.optimize()

        return json.loads(self.model.getJSONSolution())


class TVProgram(Base):
    def settings(self):

        x = self.model.addVar(name="A")
        y = self.model.addVar(name="B")

        self.model.setObjective(30000 * x + 10000 * y, GRB.MAXIMIZE)

        self.model.addConstr(20 * x + 10 * y <= 80)
        self.model.addConstr(x + y >= 5)

        self.model.optimize()

        return json.loads(self.model.getJSONSolution())


class BeltFactory(Base):
    def settings(self):
        x = self.model.addVar(name="M1")
        y = self.model.addVar(name="M2")

        self.model.setObjective(4 * x + 3 * y, GRB.MAXIMIZE)

        self.model.addConstr(2 * x + y <= 1000)
        self.model.addConstr(x + y <= 800)
        self.model.addConstr(x <= 400)
        self.model.addConstr(y <= 700)

        self.model.optimize()

        return json.loads(self.model.getJSONSolution())


class Company(Base):
    def settings(self):
        x = self.model.addVar(name="P1")
        y = self.model.addVar(name="P2")

        self.model.setObjective(120 * x + 150 * y, GRB.MAXIMIZE)

        self.model.addConstr(2 * x + 4 * y <= 100)
        self.model.addConstr(3 * x + 2 * y <= 90)
        self.model.addConstr(5 * x + 3 * y <= 120)

        self.model.optimize()

        return json.loads(self.model.getJSONSolution())

import abc
import gurobipy as gb
from gurobipy import GRB


class Base(abc.ABC):
    """
        This abstract base class to model optimizations
    """

    def __init__(self, name="default", algorithm=-1, default_format=float):
        self._message = ""
        self._solution_message = ""
        self.default_format = default_format
        self.model = gb.Model(name)
        self.model.setParam(GRB.Param.OutputFlag, 0)
        self.model.setParam(GRB.Param.Method, algorithm)

    def message(self, message: str):
        """
            set a message for min or max objective
        """
        self._message = message

    def solution_message(self, message: str):
        self._solution_message = message

    def get_message(self) -> str:
        return f"{self._message}\n\n"

    @abc.abstractmethod
    def settings(self):
        """ set decision variables and restrictions to optimization problem """
        pass

    def optimize(self):
        """ run the gurobi optimization"""
        result = self.settings()
        solution = result.get("SolutionInfo", "")
        value = self.default_format(solution.get("ObjVal"))

        message = self.get_message()

        for v in self.model.getVars():
            message += f"Qtd. {v.varName}: {int(v.x)}\n"

        if isinstance(value, float):
            message += "\n{} {:.2f}".format(self._solution_message, value)
            return message

        message += "\n{} {}".format(self._solution_message, value)

        return message

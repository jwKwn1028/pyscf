from _typeshed import Incomplete
from pyscf.pbc.grad import rhf as rhf
from numpy import ndarray

class Gradients(rhf.Gradients):
    grids: Incomplete
    def get_stress(self) -> ndarray: ...

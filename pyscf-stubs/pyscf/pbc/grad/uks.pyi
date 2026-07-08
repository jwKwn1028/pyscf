from _typeshed import Incomplete
from pyscf.pbc.grad import uhf as uhf
from numpy import ndarray

class Gradients(uhf.Gradients):
    grids: Incomplete
    def get_stress(self) -> ndarray: ...

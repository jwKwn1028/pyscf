from _typeshed import Incomplete
from pyscf.pbc.grad import uhf as uhf

class Gradients(uhf.Gradients):
    grids: Incomplete
    def get_stress(self): ...

from _typeshed import Incomplete
from pyscf import gto as gto
from pyscf.data.elements import charge as charge
from pyscf.gto.mole import is_au as is_au
from pyscf.lib import param as param

class Mole(gto.Mole):
    atom: Incomplete
    unit: str
    charge_model: str
    def __init__(self, atoms, charges=None, zeta=None) -> None: ...
    def get_zetas(self): ...

def create_mm_mol(atoms_or_coords, charges=None, radii=None, unit: str = 'Angstrom'): ...

from _typeshed import Incomplete
from pyscf import gto as gto, lib as lib, pbc as pbc, qmmm as qmmm
from pyscf.data.elements import charge as charge
from pyscf.gto.mole import is_au as is_au
from pyscf.lib import logger as logger, param as param
from scipy.special import erf as erf

class Cell(qmmm.mm_mole.Mole, pbc.gto.Cell):
    atom: Incomplete
    unit: str
    charge_model: str
    a: Incomplete
    rcut_ewald: Incomplete
    rcut_hcore: Incomplete
    mesh: Incomplete
    def __init__(self, atoms, a, rcut_ewald=None, rcut_hcore=None, charges=None, zeta=None) -> None: ...
    def get_lattice_Ls(self): ...
    def get_ewald_params(self, precision=None, rcut=None): ...
    def get_ewald_pot(self, coords1, coords2=None, charges2=None): ...

def create_mm_mol(atoms_or_coords, a, charges=None, radii=None, rcut_ewald=None, rcut_hcore=None, unit: str = 'Angstrom'): ...
create_mm_cell = create_mm_mol

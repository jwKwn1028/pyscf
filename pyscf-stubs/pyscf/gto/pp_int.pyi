from pyscf import lib as lib
from pyscf.gto.mole import Mole, ATOM_OF as ATOM_OF, intor_cross as intor_cross
from numpy import ndarray

def get_gth_pp(mol: Mole) -> ndarray: ...

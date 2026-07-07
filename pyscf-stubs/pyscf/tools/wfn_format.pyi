from _typeshed import Incomplete
from pyscf import gto as gto, lib as lib

TYPE_MAP: Incomplete

def write_mo(fout, mol, mo_coeff, mo_energy=None, mo_occ=None) -> None: ...
def write_ci(fout, fcivec, norb, nelec, ncore: int = 0): ...

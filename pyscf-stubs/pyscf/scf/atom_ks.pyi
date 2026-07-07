from _typeshed import Incomplete
from pyscf import gto as gto
from pyscf.data import elements as elements
from pyscf.dft import rks as rks
from pyscf.lib import logger as logger, param as param
from pyscf.scf import ADIIS as ADIIS, atom_hf as atom_hf

def get_atm_nrks(mol, atomic_configuration=..., xc: str = 'slater', grid=(100, 434)): ...

class AtomSphAverageRKS(rks.RKS, atom_hf.AtomSphericAverageRHF):
    init_guess: str
    def __init__(self, mol, *args, **kwargs) -> None: ...
    eig: Incomplete
    get_occ: Incomplete
    get_grad: Incomplete
AtomSphericAverageRKS = AtomSphAverageRKS

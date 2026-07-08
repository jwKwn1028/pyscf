from pyscf import gto as gto
from pyscf.df import incore as incore
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from typing import Optional

def aux_e2(mol: Mole, auxmol: Mole, intor: str = 'int3c2e_spinor', aosym: str = 's1', comp: None=None, hermi: int = 0) -> ndarray: ...
def aux_e1(mol, auxmol, intor: str = 'int3c2e_spinor', aosym: str = 's1', comp: int = 1, hermi: int = 0) -> None: ...
def cholesky_eri(mol: Mole, auxbasis: str = 'weigend+etb', auxmol: Optional[Mole]=None, int3c: str = 'int3c2e_spinor', aosym: str = 's1', int2c: str = 'int2c2e_sph', comp: int = 1, verbose: Logger = 0) -> ndarray: ...

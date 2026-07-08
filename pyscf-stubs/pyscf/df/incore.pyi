from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.df import addons as addons
from pyscf.gto.moleintor import getints as getints
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from typing import Callable, Optional, Union

MAX_MEMORY: Incomplete
LINEAR_DEP_THR: Incomplete
format_aux_basis = addons.make_auxmol

def aux_e2(mol: Mole, auxmol_or_auxbasis: Mole, intor: str = 'int3c2e', aosym: str = 's1', comp: Optional[int]=None, out: None=None, cintopt: None=None, shls_slice: None=None) -> ndarray: ...
def aux_e1(mol: Mole, auxmol_or_auxbasis: Mole, intor: str = 'int3c2e', aosym: str = 's1', comp: None=None, out: None=None) -> ndarray: ...
def fill_2c2e(mol: Mole, auxmol_or_auxbasis: Mole, intor: str = 'int2c2e', comp: None=None, hermi: int = 1, out: None=None) -> ndarray: ...
def cholesky_eri(mol: Mole, auxbasis: str = 'weigend+etb', auxmol: Optional[Mole]=None, int3c: str = 'int3c2e', aosym: str = 's2ij', int2c: str = 'int2c2e', comp: int = 1, max_memory: Union[float, int]=..., decompose_j2c: str = 'cd', lindep: float=..., verbose: Union[int, Logger] = 0, fauxe2: Callable=...) -> ndarray: ...
def cholesky_eri_debug(mol: Mole, auxbasis: str = 'weigend+etb', auxmol: Optional[Mole]=None, int3c: str = 'int3c2e', aosym: str = 's2ij', int2c: str = 'int2c2e', comp: int = 1, verbose: Union[int, Logger] = 0, fauxe2: Callable=...) -> ndarray: ...

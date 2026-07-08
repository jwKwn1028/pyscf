from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, gto as gto, lib as lib
from pyscf.df.addons import make_auxmol as make_auxmol
from pyscf.df.incore import LINEAR_DEP_THR as LINEAR_DEP_THR
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.lib.misc import H5FileWrap
from tempfile import _TemporaryFileWrapper
from typing import List, Optional, Tuple, Union

MAX_MEMORY: Incomplete

def cholesky_eri(mol: Mole, erifile: str, auxbasis: str = 'weigend+etb', dataname: str = 'j3c', tmpdir: None=None, int3c: str = 'int3c2e', aosym: str = 's2ij', int2c: str = 'int2c2e', comp: int = 1, max_memory: Union[float, int]=..., auxmol: Optional[Mole]=None, verbose: int=...) -> str: ...
def cholesky_eri_b(mol: Mole, erifile: Union[_TemporaryFileWrapper, str], auxbasis: str = 'weigend+etb', dataname: str = 'j3c', int3c: str = 'int3c2e', aosym: str = 's2ij', int2c: str = 'int2c2e', comp: int = 1, max_memory: Union[float, int]=..., auxmol: Optional[Mole]=None, decompose_j2c: str = 'CD', lindep: float=..., verbose: Logger=...) -> Union[_TemporaryFileWrapper, str]: ...
def general(mol: Mole, mo_coeffs: Tuple[ndarray, ndarray], erifile: str, auxbasis: str = 'weigend+etb', dataname: str = 'eri_mo', tmpdir: None=None, int3c: str = 'int3c2e', aosym: str = 's2ij', int2c: str = 'int2c2e', comp: int = 1, max_memory: float=..., verbose: int = 0, compact: bool = True) -> str: ...

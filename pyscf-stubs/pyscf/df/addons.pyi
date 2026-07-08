from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, gto as gto
from pyscf.data import elements as elements
from pyscf.df.autoaux import autoabs as autoabs, autoaux as autoaux
from pyscf.lib import logger as logger
from pyscf.lib.exceptions import BasisNotFoundError as BasisNotFoundError
from numpy import float64, int64, ndarray
from pyscf.gto.mole import Mole
from tempfile import _TemporaryFileWrapper
from typing import Dict, List, Optional, Tuple, Union

DFBASIS: Incomplete
ETB_BETA: Incomplete
FIRST_ETB_ELEMENT: Incomplete
USE_VERSION_26_AUXBASIS: bool
DEFAULT_AUXBASIS: Incomplete

class load(ao2mo.load):
    def __init__(self, eri: Union[ndarray, _TemporaryFileWrapper, str], dataname: str = 'j3c') -> None: ...

def aug_etb_for_dfbasis(mol: Mole, dfbasis: str=..., beta: float=..., start_at: int=...) -> Dict[str, List[List[Union[int, List[Union[float64, int]]]]]]: ...
def aug_etb(mol: Mole, beta: float=...) -> Dict[str, List[List[Union[int, List[Union[float64, int]]]]]]: ...
def make_auxbasis(mol: Mole, *, xc: str = 'HF', mp2fit: bool = False) -> Dict[str, Union[List[List[Union[int, List[Union[float64, int]]]]], str]]: ...
def make_auxmol(mol: Mole, auxbasis: Optional[Union[Dict[str, str], str]]=None) -> Mole: ...
def bse_predefined_auxbasis(mol: Mole, basis: str, xc: str = 'HF', mp2fit: bool = False) -> None: ...
def predefined_auxbasis(mol: Mole, basis: str, xc: str = 'HF', mp2fit: bool = False) -> Optional[str]: ...

from _typeshed import Incomplete
from pyscf import gto as gto
from pyscf.lib import logger as logger
from numpy import float64, int64, ndarray
from pyscf.gto.mole import Mole
from typing import Dict, List, Tuple, Union

F_LAUX: Incomplete
BETA_BIG: Incomplete
BETA_SMALL: float

def autoaux(mol: Mole) -> Dict[str, List[List[Union[int, List[Union[float64, int]]]]]]: ...
def autoabs(mol): ...

from _typeshed import Incomplete
from pyscf import lib as lib, scf as scf
from pyscf.lib import logger as logger
from numpy import float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.scf.hf import RHF
from pyscf.scf.rohf import ROHF
from pyscf.scf.uhf import UHF
from typing import List, Tuple, Union

class Chooser:
    log: Incomplete
    orbs: Incomplete
    occ: Incomplete
    entropies: Incomplete
    max_size: Incomplete
    verbose: Incomplete
    fixed: Incomplete
    def __init__(self, orbs: ndarray, occ: Union[ndarray, NPArrayWithTag], entropies: ndarray, max_size: Union[int, Tuple[int, int]]=(8, 8), fixed: bool = False, verbose: int = 4) -> None: ...
    def kernel(self) -> Union[Tuple[int, Tuple[int, int], ndarray, List[int]], Tuple[int, Tuple[int, int], ndarray, ndarray]]: ...

class APC:
    log: Incomplete
    mf: Incomplete
    n: Incomplete
    eps: Incomplete
    max_size: Incomplete
    verbose: Incomplete
    fixed: Incomplete
    def __init__(self, mf: Union[RHF, ROHF, UHF], max_size: Union[int, Tuple[int, int]]=(8, 8), n: int = 2, fixed: bool = False, eps: float = 0.001, verbose: int = 4) -> None: ...
    entropies: Incomplete
    active_idx: Incomplete
    def kernel(self) -> Tuple[int, Tuple[int, int], ndarray]: ...

from _typeshed import Incomplete
from pyscf import lib as lib, scf as scf
from pyscf.lib import logger as logger

class Chooser:
    log: Incomplete
    orbs: Incomplete
    occ: Incomplete
    entropies: Incomplete
    max_size: Incomplete
    verbose: Incomplete
    fixed: Incomplete
    def __init__(self, orbs, occ, entropies, max_size=(8, 8), fixed: bool = False, verbose: int = 4) -> None: ...
    def kernel(self): ...

class APC:
    log: Incomplete
    mf: Incomplete
    n: Incomplete
    eps: Incomplete
    max_size: Incomplete
    verbose: Incomplete
    fixed: Incomplete
    def __init__(self, mf, max_size=(8, 8), n: int = 2, fixed: bool = False, eps: float = 0.001, verbose: int = 4) -> None: ...
    entropies: Incomplete
    active_idx: Incomplete
    def kernel(self): ...

from pyscf import lib as lib
from pyscf.cc import ccsd as ccsd, ccsd_lambda as ccsd_lambda
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.cc.ccsd import CCSD, _ChemistsERIs
from typing import Optional, Tuple

def kernel(mycc: CCSD, eris: Optional[_ChemistsERIs]=None, t1: Optional[ndarray]=None, t2: Optional[ndarray]=None, l1: None=None, l2: None=None, max_cycle: int = 50, tol: float = 1e-08, verbose: int=...) -> Tuple[bool, ndarray, ndarray]: ...
def make_intermediates(mycc, t1, t2, eris): ...
def update_lambda(mycc, t1, t2, l1, l2, eris=None, imds=None): ...

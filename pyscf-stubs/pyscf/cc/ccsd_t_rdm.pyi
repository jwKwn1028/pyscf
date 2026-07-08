from pyscf import lib as lib
from pyscf.cc import ccsd_rdm as ccsd_rdm
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.cc.rccsd import RCCSD, _ChemistsERIs
from typing import Optional, Tuple

def make_rdm1(mycc, t1, t2, l1, l2, eris=None, ao_repr: bool = False): ...
def make_rdm2(mycc, t1, t2, l1, l2, eris=None): ...
def t3_symm_ip_py(A: ndarray, nocc3: int, nvir: int, pattern: str, alpha: float = 1.0, beta: float = 0.0) -> ndarray: ...

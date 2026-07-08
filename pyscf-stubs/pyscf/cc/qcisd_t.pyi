from pyscf import lib as lib
from pyscf.lib import logger as logger
from numpy import float64, ndarray
from pyscf.cc.ccsd import _ChemistsERIs
from pyscf.cc.qcisd import QCISD
from typing import Optional

def kernel(mycc: QCISD, eris: _ChemistsERIs, t1: Optional[ndarray]=None, t2: Optional[ndarray]=None, verbose: int=...) -> float64: ...

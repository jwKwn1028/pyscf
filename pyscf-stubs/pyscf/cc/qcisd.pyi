from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.cc.ccsd import _ChemistsERIs, CCSDBase as CCSDBase, as_scanner as as_scanner
from pyscf.lib import logger as logger
from h5py._hl.dataset import Dataset
from numpy import float64, ndarray
from pyscf.lib.misc import H5TmpFile
from typing import Optional, Tuple

BLKMIN: Incomplete
MEMORYMIN: Incomplete

def kernel(mycc, eris=None, t1=None, t2=None, max_cycle: int = 50, tol: float = 1e-08, tolnormt: float = 1e-06, verbose=None): ...
def update_amps(mycc: "QCISD", t1: ndarray, t2: ndarray, eris: _ChemistsERIs) -> Tuple[ndarray, ndarray]: ...
def energy(mycc: "QCISD", t1: Optional[ndarray]=None, t2: Optional[ndarray]=None, eris: Optional[_ChemistsERIs]=None) -> float64: ...

class QCISD(CCSDBase):
    def dump_flags(self, verbose: None=None) -> "QCISD": ...
    energy = energy
    update_amps = update_amps
    kernel: Incomplete
    ccsd: Incomplete
    as_scanner = as_scanner
    def qcisd_t(self, t1: None=None, t2: None=None, eris: None=None) -> float64: ...
RQCISD = QCISD

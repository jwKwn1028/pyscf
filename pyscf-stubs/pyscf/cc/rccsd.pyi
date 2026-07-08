from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib
from pyscf.cc import ccsd as ccsd
from pyscf.lib import logger as logger
from pyscf.mp import mp2 as mp2
from numpy import float64, ndarray
from pyscf.pbc.cc.ccsd import RCCSD
from pyscf.pbc.ci.cisd import RCISD
from typing import Callable, Optional, Tuple, Union

BLKMIN: Incomplete
MEMORYMIN: Incomplete

def update_amps(cc: Union[RCCSD, RCCSD], t1: ndarray, t2: ndarray, eris: "_ChemistsERIs") -> Tuple[ndarray, ndarray]: ...
def energy(cc: Union[RCCSD, RCCSD], t1: Optional[ndarray]=None, t2: Optional[ndarray]=None, eris: Optional[_ChemistsERIs]=None) -> float64: ...

class RCCSD(ccsd.CCSD):
    def kernel(self, t1: None=None, t2: None=None, eris: Optional[_ChemistsERIs]=None, mbpt2: bool = False) -> Union[Tuple[float, ndarray, ndarray], Tuple[float64, ndarray, ndarray]]: ...
    t1: Incomplete
    def ccsd(self, t1: None=None, t2: None=None, eris: Optional[_ChemistsERIs]=None, mbpt2: bool = False) -> Union[Tuple[float, ndarray, ndarray], Tuple[float64, ndarray, ndarray]]: ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> "_ChemistsERIs": ...
    energy = energy
    update_amps = update_amps
    def solve_lambda(self, t1: Optional[ndarray]=None, t2: Optional[ndarray]=None, l1: None=None, l2: None=None, eris: None=None) -> Tuple[ndarray, ndarray]: ...

class _ChemistsERIs(ccsd._ChemistsERIs):
    def get_ovvv(self, *slices) -> ndarray: ...

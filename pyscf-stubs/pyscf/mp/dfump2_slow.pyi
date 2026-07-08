from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.mp import dfump2 as dfump2
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mp.dfump2 import _DFINCOREERIS
from typing import Optional, Tuple

WITH_T2: Incomplete

def kernel(mp: "DFUMP2", mo_energy: None=None, mo_coeff: None=None, eris: Optional[_DFINCOREERIS]=None, with_t2: bool=..., verbose: None=None) -> Tuple[NPArrayWithTag, Tuple[ndarray, ndarray, ndarray]]: ...

class DFUMP2(dfump2.DFUMP2):
    def init_amps(self, mo_energy: None=None, mo_coeff: None=None, eris: Optional[_DFINCOREERIS]=None, with_t2: bool=...) -> Tuple[NPArrayWithTag, Tuple[ndarray, ndarray, ndarray]]: ...
UMP2 = DFUMP2

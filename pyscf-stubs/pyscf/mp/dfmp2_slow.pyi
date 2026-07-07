from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.mp import dfmp2 as dfmp2

WITH_T2: Incomplete

def kernel(mp, mo_energy=None, mo_coeff=None, eris=None, with_t2=..., verbose=None): ...

class DFMP2(dfmp2.DFMP2):
    def init_amps(self, mo_energy=None, mo_coeff=None, eris=None, with_t2=...): ...
MP2 = DFMP2

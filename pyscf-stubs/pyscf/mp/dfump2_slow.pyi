from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.mp import dfump2 as dfump2

WITH_T2: Incomplete

def kernel(mp, mo_energy=None, mo_coeff=None, eris=None, with_t2=..., verbose=None): ...

class DFUMP2(dfump2.DFUMP2):
    def init_amps(self, mo_energy=None, mo_coeff=None, eris=None, with_t2=...): ...
UMP2 = DFUMP2

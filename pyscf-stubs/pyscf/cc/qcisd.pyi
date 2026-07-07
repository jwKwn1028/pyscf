from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.cc.ccsd import CCSDBase as CCSDBase, as_scanner as as_scanner
from pyscf.lib import logger as logger

BLKMIN: Incomplete
MEMORYMIN: Incomplete

def kernel(mycc, eris=None, t1=None, t2=None, max_cycle: int = 50, tol: float = 1e-08, tolnormt: float = 1e-06, verbose=None): ...
def update_amps(mycc, t1, t2, eris): ...
def energy(mycc, t1=None, t2=None, eris=None): ...

class QCISD(CCSDBase):
    def dump_flags(self, verbose=None): ...
    energy = energy
    update_amps = update_amps
    kernel: Incomplete
    ccsd: Incomplete
    as_scanner = as_scanner
    def qcisd_t(self, t1=None, t2=None, eris=None): ...
RQCISD = QCISD

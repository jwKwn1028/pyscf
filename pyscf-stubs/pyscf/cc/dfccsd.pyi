from _typeshed import Incomplete
from pyscf import __config__ as __config__, df as df, lib as lib, scf as scf
from pyscf.cc import ccsd as ccsd
from pyscf.lib import logger as logger

MEMORYMIN: Incomplete

class RCCSD(ccsd.CCSD):
    with_df: Incomplete
    def __init__(self, mf, frozen=None, mo_coeff=None, mo_occ=None) -> None: ...
    def reset(self, mol=None): ...
    def ao2mo(self, mo_coeff=None): ...
DFCCSD = RCCSD
DFRCCSD = RCCSD

class _ChemistsERIs(ccsd._ChemistsERIs): ...

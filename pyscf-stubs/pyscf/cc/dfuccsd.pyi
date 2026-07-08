from _typeshed import Incomplete
from pyscf import __config__ as __config__, df as df, lib as lib, scf as scf
from pyscf.cc import ccsd as ccsd, dfccsd as dfccsd, uccsd as uccsd
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.lib.logger import Logger
from typing import Optional, Tuple

MEMORYMIN: Incomplete

class UCCSD(uccsd.UCCSD):
    with_df: Incomplete
    def __init__(self, mf, frozen=None, mo_coeff=None, mo_occ=None) -> None: ...
    def reset(self, mol=None): ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> "_ChemistsERIs": ...
DFCCSD = UCCSD
DFUCCSD = UCCSD

class _ChemistsERIs(uccsd._ChemistsERIs): ...

from _typeshed import Incomplete
from pyscf import __config__ as __config__, df as df, lib as lib, scf as scf
from pyscf.cc import ccsd as ccsd
from pyscf.lib import logger as logger
from h5py._hl.dataset import Dataset
from numpy import ndarray
from pyscf.cc.dfuccsd import UCCSD
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.scf.hf import RHF
from typing import Optional, Union

MEMORYMIN: Incomplete

class RCCSD(ccsd.CCSD):
    with_df: Incomplete
    def __init__(self, mf: RHF, frozen: None=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None) -> None: ...
    def reset(self, mol=None): ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> "_ChemistsERIs": ...
DFCCSD = RCCSD
DFRCCSD = RCCSD

class _ChemistsERIs(ccsd._ChemistsERIs): ...

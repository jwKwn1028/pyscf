from pyscf.pbc.cc import ccsd as ccsd, eom_kccsd_ghf as eom_kccsd_ghf, eom_kccsd_rhf as eom_kccsd_rhf, eom_kccsd_uhf as eom_kccsd_uhf
from pyscf.pbc.cc.kccsd_rhf_ksymm import KsymAdaptedRCCSD as KsymAdaptedRCCSD
from _typeshed import Incomplete
from pyscf.pbc.cc.ccsd import UCCSD
from pyscf.pbc.cc.kccsd import GCCSD
from pyscf.pbc.cc.kccsd_uhf import KUCCSD
from pyscf.pbc.scf.hf import RHF
from pyscf.pbc.scf.kghf import KGHF
from pyscf.pbc.scf.khf import KRHF
from pyscf.pbc.scf.kuhf import KUHF
from pyscf.pbc.scf.uhf import UHF
from typing import Any, List, Optional, Tuple, Union

def RCCSD(mf: RHF, frozen: Optional[Union[int, List[int]]]=None, mo_coeff: None=None, mo_occ: None=None) -> Incomplete: ...
CCSD = RCCSD

def UCCSD(mf: UHF, frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> UCCSD: ...
def GCCSD(mf, frozen=None, mo_coeff=None, mo_occ=None): ...
def KGCCSD(mf: Union[KGHF, KRHF], frozen: Optional[Union[int, List[List[int]], List[List[Union[int, Any]]], List[int]]]=None, mo_coeff: None=None, mo_occ: None=None) -> GCCSD: ...
def KRCCSD(mf: KRHF, frozen: Optional[Union[int, List[List[int]], List[List[Union[int, Any]]], List[int]]]=None, mo_coeff: None=None, mo_occ: None=None) -> Incomplete: ...
KCCSD = KRCCSD

def KUCCSD(mf: Union[KUHF, KRHF], frozen: Optional[Tuple[List[List[int]], List[List[int]]]]=None, mo_coeff: None=None, mo_occ: None=None) -> KUCCSD: ...

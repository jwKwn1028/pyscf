from pyscf.pbc import scf as scf
from pyscf.pbc.mp import kmp2 as kmp2, kmp2_ksymm as kmp2_ksymm, mp2 as mp2
from pyscf.pbc.mp.kmp2 import KMP2
from pyscf.pbc.mp.kmp2_ksymm import KsymAdaptedKMP2
from pyscf.pbc.scf.khf import KRHF
from pyscf.pbc.scf.khf_ksymm import KsymAdaptedKRHF
from typing import Union

def RMP2(mf, frozen=None, mo_coeff=None, mo_occ=None): ...
MP2 = RMP2

def UMP2(mf, frozen=None, mo_coeff=None, mo_occ=None): ...
def GMP2(mf, frozen=None, mo_coeff=None, mo_occ=None): ...
def KRMP2(mf: Union[KsymAdaptedKRHF, KRHF], frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> Union[KMP2, KsymAdaptedKMP2]: ...
KMP2 = KRMP2

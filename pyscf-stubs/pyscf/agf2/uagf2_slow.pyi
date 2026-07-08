from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, lib as lib
from pyscf.agf2 import ragf2 as ragf2, ragf2_slow as ragf2_slow, uagf2 as uagf2
from pyscf.lib import logger as logger
from pyscf.agf2.aux_space import GreensFunction, SelfEnergy
from pyscf.agf2.uagf2 import _ChemistsERIs
from pyscf.lib.diis import DIIS
from pyscf.scf.uhf import UHF
from typing import Optional, Tuple, Union

def build_se_part(agf2: "UAGF2", eri: "_ChemistsERIs", gf_occ: Tuple[GreensFunction, GreensFunction], gf_vir: Tuple[GreensFunction, GreensFunction], os_factor: float = 1.0, ss_factor: float = 1.0) -> Tuple[SelfEnergy, SelfEnergy]: ...

class UAGF2(uagf2.UAGF2):
    nmom: Incomplete
    def __init__(self, mf: UHF, nmom: Union[Tuple[int, int], Tuple[None, int]]=(None, 0), frozen: None=None, mo_energy: None=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    build_se_part = build_se_part
    def build_se(self, eri: Optional[_ChemistsERIs]=None, gf: Optional[Tuple[GreensFunction, GreensFunction]]=None, os_factor: None=None, ss_factor: None=None, se_prev: None=None) -> Tuple[SelfEnergy, SelfEnergy]: ...
    def dump_flags(self, verbose: None=None) -> "UAGF2": ...
    def run_diis(self, se: Tuple[SelfEnergy, SelfEnergy], diis: Optional[DIIS]=None) -> Tuple[SelfEnergy, SelfEnergy]: ...

class _ChemistsERIs(uagf2._ChemistsERIs): ...

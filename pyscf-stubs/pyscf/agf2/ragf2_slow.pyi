from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.agf2 import ragf2 as ragf2
from pyscf.lib import logger as logger
from pyscf.agf2.aux_space import GreensFunction, SelfEnergy
from pyscf.agf2.ragf2 import _ChemistsERIs
from pyscf.lib.diis import DIIS
from pyscf.scf.hf import RHF
from typing import Optional, Tuple, Union

def build_se_part(agf2: "RAGF2", eri: "_ChemistsERIs", gf_occ: GreensFunction, gf_vir: GreensFunction, os_factor: float = 1.0, ss_factor: float = 1.0) -> SelfEnergy: ...

class RAGF2(ragf2.RAGF2):
    nmom: Incomplete
    def __init__(self, mf: RHF, nmom: Union[Tuple[int, int], Tuple[None, int]]=(None, 0), frozen: None=None, mo_energy: None=None, mo_coeff: None=None, mo_occ: None=None) -> None: ...
    build_se_part = build_se_part
    def build_se(self, eri: Optional[_ChemistsERIs]=None, gf: Optional[GreensFunction]=None, os_factor: None=None, ss_factor: None=None, se_prev: None=None) -> SelfEnergy: ...
    def dump_flags(self, verbose: None=None) -> "RAGF2": ...
    def run_diis(self, se: SelfEnergy, diis: Optional[DIIS]=None) -> SelfEnergy: ...

class _ChemistsERIs(ragf2._ChemistsERIs): ...

from _typeshed import Incomplete
from collections.abc import Generator
from pyscf import __config__ as __config__, ao2mo as ao2mo, df as df, lib as lib
from pyscf.agf2 import mpi_helper as mpi_helper, ragf2 as ragf2
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.agf2.aux_space import GreensFunction, SelfEnergy
from pyscf.agf2.dfuagf2 import DFUAGF2
from typing import Iterator, Optional, Tuple, Union

BLKMIN: Incomplete

def build_se_part(agf2: "DFRAGF2", eri: "_ChemistsERIs", gf_occ: GreensFunction, gf_vir: GreensFunction, os_factor: float = 1.0, ss_factor: float = 1.0) -> SelfEnergy: ...
def get_jk(agf2: Union[DFUAGF2, DFRAGF2], eri: Union[ndarray, Tuple[ndarray, ndarray]], rdm1: ndarray, with_j: bool = True, with_k: bool = True) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, None]]: ...

class DFRAGF2(ragf2.RAGF2):
    allow_lowmem_build: bool
    def __init__(self, mf, frozen=None, mo_energy=None, mo_coeff=None, mo_occ=None) -> None: ...
    build_se_part = build_se_part
    get_jk = get_jk
    def ao2mo(self, mo_coeff: None=None) -> "_ChemistsERIs": ...
    def reset(self, mol=None): ...
    @property
    def with_df(self): ...
    @with_df.setter
    def with_df(self, val) -> None: ...

class DF(df.DF):
    def prange(self, start: Optional[int]=None, stop: Optional[int]=None, step: Optional[int]=None) -> Iterator[Tuple[int, int]]: ...

class _ChemistsERIs(ragf2._ChemistsERIs): ...

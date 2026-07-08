from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM
from pyscf.pbc import df as df, dft as dft, scf as scf
from pyscf.pbc.df.df import CDERIArray as CDERIArray
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.lib.kpts_helper import round_to_fbz as round_to_fbz, unique as unique
from pyscf.pbc.mp import kmp2 as kmp2
from pyscf.pbc.mp.kmp2 import padding_k_idx as padding_k_idx
from pyscf.pbc.scf.khf import KRHF, get_occ as get_occ
from pyscf.pbc.tools.pbc import get_monkhorst_pack_size as get_monkhorst_pack_size
from numpy import float64, ndarray
from typing import List, Optional, Union

def kernel(mp: "KMP2_stagger", mo_energy: ndarray, mo_coeff: Union[ndarray, List[ndarray]], verbose: int=...) -> float64: ...

class KMP2_stagger(kmp2.KMP2):
    cell: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    e_corr: Incomplete
    flag_submesh: Incomplete
    kpts: Incomplete
    mo_energy: Incomplete
    mo_coeff: Incomplete
    mo_occ: Incomplete
    with_df_ints: bool
    nkpts: Incomplete
    frozen: Incomplete
    khelper: Incomplete
    kpts_vir: Incomplete
    kpts_occ: Incomplete
    nkpts_ov: Incomplete
    kpts_idx_vir: Incomplete
    kpts_idx_occ: Incomplete
    def __init__(self, mf: KRHF, frozen: Optional[List[int]]=None, flag_submesh: bool = False) -> None: ...
    def dump_flags(self) -> "KMP2_stagger": ...
    def kernel(self) -> float64: ...

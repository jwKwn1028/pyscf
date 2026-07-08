from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, df as df, lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.mp import dfmp2 as dfmp2, ump2 as ump2
from pyscf.mp.ump2 import make_rdm1 as make_rdm1, make_rdm2 as make_rdm2
from h5py._hl.dataset import Dataset
from io import TextIOWrapper
from numpy import ndarray
from pyscf.df.df import DF
from pyscf.lib.logger import Logger
from pyscf.lib.misc import H5FileWrap, H5TmpFile
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mp.dfump2_slow import DFUMP2
from pyscf.pbc.df.df import GDF
from typing import List, Optional, Tuple, Union

WITH_T2: Incomplete
THRESH_LINDEP: Incomplete
libmp: Incomplete

def kernel(mp: "DFUMP2", mo_energy: None=None, mo_coeff: None=None, eris: Optional[Union[_DFOUTCOREERIS, _DFINCOREERIS]]=None, with_t2: bool=..., verbose: None=None) -> Tuple[NPArrayWithTag, Tuple[ndarray, ndarray, ndarray]]: ...

class DFUMP2(ump2.UMP2):
    __init__: Incomplete
    get_nocc = ump2.get_nocc
    get_nmo = ump2.get_nmo
    get_frozen_mask = ump2.get_frozen_mask
    kernel: Incomplete
    make_fno = ump2.make_fno
    make_rdm1 = make_rdm1
    make_rdm2 = make_rdm2
    reset: Incomplete
    def split_mo_coeff(self, mo_coeff: None=None) -> List[List[ndarray]]: ...
    def split_mo_energy(self, mo_energy: None=None) -> List[List[ndarray]]: ...
    def split_mo_occ(self, mo_occ=None): ...
    def ao2mo(self, mo_coeff: None=None, ovL: Optional[Union[List[ndarray], str]]=None, ovL_to_save: Optional[str]=None) -> Union[_DFOUTCOREERIS, _DFINCOREERIS]: ...
    def nuc_grad_method(self) -> None: ...
    def update_amps(self, t2, eris) -> None: ...
    def init_amps(self, mo_energy: None=None, mo_coeff: None=None, eris: Optional[Union[_DFOUTCOREERIS, _DFINCOREERIS]]=None, with_t2: bool=...) -> Tuple[NPArrayWithTag, Tuple[ndarray, ndarray, ndarray]]: ...
    Gradients = NotImplemented
MP2 = DFUMP2
UMP2 = DFUMP2

class _DFINCOREERIS:
    with_df: Incomplete
    occ_coeff: Incomplete
    vir_coeff: Incomplete
    max_memory: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    dtype: Incomplete
    dsize: int
    ovL: Incomplete
    def __init__(self, with_df: Union[DF, GDF], occ_coeff: List[ndarray], vir_coeff: List[ndarray], max_memory: int, ovL: Optional[List[ndarray]]=None, verbose: Optional[int]=None, stdout: Optional[TextIOWrapper]=None) -> None: ...
    @property
    def nocc(self) -> List[int]: ...
    @property
    def nvir(self) -> List[int]: ...
    @property
    def naux(self) -> int: ...
    def build(self) -> None: ...
    def get_occ_blk(self, s: int, i0: int, i1: int) -> ndarray: ...
    def get_ov_blk(self, s, ia0, ia1): ...

class _DFOUTCOREERIS(_DFINCOREERIS):
    def __init__(self, with_df: Union[DF, GDF], occ_coeff: List[ndarray], vir_coeff: List[ndarray], max_memory: int, ovL: Optional[str]=None, ovL_to_save: Optional[str]=None, verbose: Optional[int]=None, stdout: Optional[TextIOWrapper]=None) -> None: ...
    feri: Incomplete
    ovL: Incomplete
    def build(self) -> None: ...

from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, lib as lib
from pyscf.data import nist as nist
from pyscf.lib import linalg_helper as linalg_helper, logger as logger
from pyscf.pbc import scf as scf
from pyscf.pbc.df.df_ao2mo import warn_pbc2d_eri as warn_pbc2d_eri
from pyscf.pbc.lib.kpts_helper import conj_mapping as conj_mapping, get_kconserv_ria as get_kconserv_ria, is_gamma_point as is_gamma_point
from pyscf.pbc.tdscf.rhf import TDBase as TDBase
from pyscf.tdscf import rhf as rhf
from numpy import int64, ndarray
from pyscf.pbc.dft.krks import KRKS
from pyscf.pbc.dft.kuks import KUKS
from pyscf.pbc.scf.khf import KRHF
from pyscf.pbc.scf.kuhf import KUHF
from typing import Callable, List, Optional, Tuple, Union

REAL_EIG_THRESHOLD: Incomplete

def get_ab(mf: Union[KRHF, KRKS], kshift: int = 0) -> Tuple[ndarray, ndarray]: ...

class KTDBase(TDBase):
    conv_tol: Incomplete
    kshift_lst: Incomplete
    def __init__(self, mf: Union[KUHF, KUKS, KRKS, KRHF], kshift_lst: None=None) -> None: ...
    def dump_flags(self, verbose: None=None) -> None: ...
    def check_sanity(self) -> None: ...
    get_nto: Incomplete

class TDA(KTDBase):
    def get_ab(self, mf: None=None, kshift: int = 0) -> Tuple[ndarray, ndarray]: ...
    def gen_vind(self, mf: Optional[Union[KRHF, KRKS]]=None, kshift: Union[int64, int] = 0) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: Union[KRHF, KRKS], kshift: Union[int64, int], nstates: Optional[int]=None) -> ndarray: ...
    converged: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None) -> Tuple[List[ndarray], List[List[Tuple[List[ndarray], int]]]]: ...
CIS = TDA
KTDA = TDA

class TDHF(KTDBase):
    get_ab: Incomplete
    def gen_vind(self, mf: Union[KRHF, KRKS], kshift: Union[int64, int] = 0) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: Union[KRHF, KRKS], kshift: Union[int64, int], nstates: Optional[int]=None) -> ndarray: ...
    get_precond: Incomplete
    converged: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None) -> Tuple[List[ndarray], List[List[Tuple[List[ndarray], List[ndarray]]]]]: ...
RPA = TDHF
KTDHF = TDHF

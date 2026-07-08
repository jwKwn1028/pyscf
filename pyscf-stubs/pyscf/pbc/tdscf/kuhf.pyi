from _typeshed import Incomplete
from functools import reduce as reduce
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc import scf as scf
from pyscf.pbc.lib.kpts_helper import conj_mapping as conj_mapping, get_kconserv_ria as get_kconserv_ria, is_gamma_point as is_gamma_point
from pyscf.pbc.tdscf.krhf import KTDBase as KTDBase
from pyscf.tdscf import uhf as uhf
from numpy import int64, ndarray
from pyscf.pbc.dft.kuks import KUKS
from pyscf.pbc.scf.kuhf import KUHF
from typing import Callable, List, Optional, Tuple, Union

REAL_EIG_THRESHOLD: Incomplete

def get_ab(mf, kshift: int = 0): ...

class TDA(KTDBase):
    def get_ab(self, mf=None, kshift: int = 0): ...
    def gen_vind(self, mf: Union[KUKS, KUHF], kshift: Union[int64, int] = 0) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: Union[KUKS, KUHF], kshift: Union[int64, int], nstates: Optional[int]=None) -> ndarray: ...
    converged: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None) -> Tuple[List[ndarray], List[List[Tuple[Tuple[List[ndarray], List[ndarray]], Tuple[int, int]]]]]: ...
CIS = TDA
KTDA = TDA

class TDHF(KTDBase):
    get_ab: Incomplete
    def gen_vind(self, mf: Union[KUKS, KUHF], kshift: Union[int64, int] = 0) -> Tuple[Callable, ndarray]: ...
    def get_init_guess(self, mf: Union[KUKS, KUHF], kshift: Union[int64, int], nstates: Optional[int]=None, wfnsym: None=None) -> ndarray: ...
    get_precond: Incomplete
    converged: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0: None=None) -> Tuple[List[ndarray], List[List[Tuple[Tuple[List[ndarray], List[ndarray]], Tuple[List[ndarray], List[ndarray]]]]]]: ...
RPA = TDHF
KTDHF = TDHF

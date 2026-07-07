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

REAL_EIG_THRESHOLD: Incomplete

def get_ab(mf, kshift: int = 0): ...

class KTDBase(TDBase):
    conv_tol: Incomplete
    kshift_lst: Incomplete
    def __init__(self, mf, kshift_lst=None) -> None: ...
    def dump_flags(self, verbose=None) -> None: ...
    def check_sanity(self) -> None: ...
    get_nto: Incomplete

class TDA(KTDBase):
    def get_ab(self, mf=None, kshift: int = 0): ...
    def gen_vind(self, mf=None, kshift: int = 0): ...
    def get_init_guess(self, mf, kshift, nstates=None): ...
    converged: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0=None): ...
CIS = TDA
KTDA = TDA

class TDHF(KTDBase):
    get_ab: Incomplete
    def gen_vind(self, mf, kshift: int = 0): ...
    def get_init_guess(self, mf, kshift, nstates=None): ...
    get_precond: Incomplete
    converged: Incomplete
    e: Incomplete
    xy: Incomplete
    def kernel(self, x0=None): ...
RPA = TDHF
KTDHF = TDHF

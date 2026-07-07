import contextlib
from _typeshed import Incomplete
from collections.abc import Generator
from pyscf import __config__ as __config__, gto as gto, lib as lib, mcscf as mcscf, scf as scf
from pyscf.df import df_jk as df_jk
from pyscf.lib import logger as logger
from pyscf.sgx import sgx_jk as sgx_jk

def sgx_fit(mf, auxbasis=None, with_df=None, pjs: bool = False): ...

class _SGXHF:
    __name_mixin__: str
    auxbasis: Incomplete
    with_df: Incomplete
    rebuild_nsteps: int
    def __init__(self, mf, df=None, auxbasis=None) -> None: ...
    def undo_sgx(self): ...
    def build(self, mol=None, **kwargs): ...
    def reset(self, mol=None): ...
    def pre_kernel(self, envs) -> None: ...
    def get_jk(self, mol=None, dm=None, hermi: int = 1, with_j: bool = True, with_k: bool = True, omega=None): ...
    def get_veff(self, mol=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1): ...
    @contextlib.contextmanager
    def with_full_dm(self, dm, dm_last) -> Generator[Incomplete]: ...
    def post_kernel(self, envs) -> None: ...
    def to_gpu(self) -> None: ...
    def method_not_implemented(self, *args, **kwargs) -> None: ...
    def nuc_grad_method(self): ...
    Gradients = nuc_grad_method
    Hessian = method_not_implemented
    NMR = method_not_implemented
    NSR = method_not_implemented
    Polarizability = method_not_implemented
    RotationalGTensor = method_not_implemented
    MP2 = method_not_implemented
    CISD = method_not_implemented
    CCSD = method_not_implemented
    CASCI = method_not_implemented
    CASSCF = method_not_implemented

class SGX(lib.StreamObject):
    mol: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    max_memory: Incomplete
    grids_thrd: float
    grids_level_i: int
    grids_level_f: int
    use_opt_grids: bool
    fit_ovlp: bool
    grids_switch_thrd: float
    dfj: bool
    optk: bool
    sgx_tol_energy: str
    sgx_tol_potential: str
    bound_algo: str
    grids: Incomplete
    auxmol: Incomplete
    debug: bool
    blockdim: int
    direct_j: bool
    def __init__(self, mol, auxbasis=None) -> None: ...
    @property
    def auxbasis(self): ...
    @auxbasis.setter
    def auxbasis(self, x) -> None: ...
    def dump_flags(self, verbose=None): ...
    def build(self, level=None): ...
    def kernel(self, *args, **kwargs): ...
    def reset(self, mol=None): ...
    def get_jk(self, dm, hermi: int = 1, vhfopt=None, with_j: bool = True, with_k: bool = True, direct_scf_tol=..., omega=None): ...
    to_gpu = lib.to_gpu

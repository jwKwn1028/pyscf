from _typeshed import Incomplete
from collections.abc import Generator
from pyscf import __config__ as __config__, lib as lib
from pyscf.dft import numint as numint, xc_deriv as xc_deriv
from pyscf.dft.numint import BLKSIZE as BLKSIZE
from pyscf.dft.numint2c import mcfun_eval_xc_adapter as mcfun_eval_xc_adapter

def eval_ao(mol, coords, deriv: int = 0, with_s: bool = True, shls_slice=None, non0tab=None, cutoff=None, out=None, verbose=None): ...
def eval_rho(mol, ao, dm, non0tab=None, xctype: str = 'LDA', hermi: int = 0, with_lapl: bool = False, verbose=None): ...
def r_vxc(ni, mol, grids, xc_code, dms, spin: int = 0, relativity: int = 1, hermi: int = 1, max_memory: int = 2000, verbose=None): ...
def r_fxc(ni, mol, grids, xc_code, dm0, dms, spin: int = 0, relativity: int = 1, hermi: int = 0, rho0=None, vxc=None, fxc=None, max_memory: int = 2000, verbose=None): ...
def cache_xc_kernel(ni, mol, grids, xc_code, mo_coeff, mo_occ, spin: int = 1, max_memory: int = 2000): ...
def cache_xc_kernel1(ni, mol, grids, xc_code, dm, spin: int = 1, max_memory: int = 2000): ...
def get_rho(ni, mol, dm, grids, max_memory: int = 2000): ...

class RNumInt(lib.StreamObject, numint.LibXCMixin):
    collinear: Incomplete
    spin_samples: Incomplete
    collinear_thrd: Incomplete
    collinear_samples: Incomplete
    get_rho = get_rho
    cache_xc_kernel = cache_xc_kernel
    cache_xc_kernel1 = cache_xc_kernel1
    get_vxc = r_vxc
    r_vxc = r_vxc
    get_fxc = r_fxc
    r_fxc = r_fxc
    eval_xc_eff: Incomplete
    mcfun_eval_xc_adapter = mcfun_eval_xc_adapter
    eval_ao: Incomplete
    eval_rho: Incomplete
    def eval_rho1(self, mol, ao, dm, screen_index=None, xctype: str = 'LDA', hermi: int = 0, with_lapl: bool = True, cutoff=None, ao_cutoff=None, pair_mask=None, verbose=None): ...
    def eval_rho2(self, mol, ao, mo_coeff, mo_occ, non0tab=None, xctype: str = 'LDA', with_lapl: bool = True, verbose=None) -> None: ...
    def block_loop(self, mol, grids, nao, deriv: int = 0, max_memory: int = 2000, non0tab=None, blksize=None, buf=None, with_s: bool = False) -> Generator[Incomplete]: ...

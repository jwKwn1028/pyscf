from _typeshed import Incomplete
from collections.abc import Generator
from pyscf import __config__ as __config__, lib as lib
from pyscf.dft import numint as numint, xc_deriv as xc_deriv
from pyscf.dft.numint import BLKSIZE as BLKSIZE
from pyscf.dft.numint2c import mcfun_eval_xc_adapter as mcfun_eval_xc_adapter
from numpy import bool, float64, ndarray
from pyscf.dft.gen_grid import Grids
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Callable, Iterator, Optional, Tuple, Union

def eval_ao(mol: Mole, coords: ndarray, deriv: int = 0, with_s: Union[bool, bool] = True, shls_slice: None=None, non0tab: Optional[ndarray]=None, cutoff: Optional[float]=None, out: Optional[ndarray]=None, verbose: None=None) -> ndarray: ...
def eval_rho(mol: Mole, ao: Union[ndarray, Tuple[ndarray, ndarray]], dm: ndarray, non0tab: Optional[ndarray]=None, xctype: str = 'LDA', hermi: int = 0, with_lapl: bool = False, verbose: None=None) -> ndarray: ...
def r_vxc(ni: "RNumInt", mol: Mole, grids: Grids, xc_code: str, dms: Union[ndarray, NPArrayWithTag], spin: int = 0, relativity: int = 1, hermi: int = 1, max_memory: Union[float, int] = 2000, verbose: None=None) -> Tuple[float64, float64, ndarray]: ...
def r_fxc(ni: "RNumInt", mol: Mole, grids: Grids, xc_code: str, dm0: ndarray, dms: ndarray, spin: int = 0, relativity: int = 1, hermi: int = 0, rho0: None=None, vxc: None=None, fxc: None=None, max_memory: int = 2000, verbose: None=None) -> ndarray: ...
def cache_xc_kernel(ni, mol, grids, xc_code, mo_coeff, mo_occ, spin: int = 1, max_memory: int = 2000): ...
def cache_xc_kernel1(ni: "RNumInt", mol: Mole, grids: Grids, xc_code: str, dm: ndarray, spin: int = 1, max_memory: int = 2000) -> Tuple[ndarray, ndarray, ndarray]: ...
def get_rho(ni: "RNumInt", mol: Mole, dm: ndarray, grids: Grids, max_memory: int = 2000) -> ndarray: ...

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
    def block_loop(self, mol: Mole, grids: Grids, nao: int, deriv: int = 0, max_memory: Union[float, int] = 2000, non0tab: None=None, blksize: None=None, buf: None=None, with_s: Union[bool, bool] = False) -> Iterator[Tuple[ndarray, ndarray, ndarray, ndarray]]: ...

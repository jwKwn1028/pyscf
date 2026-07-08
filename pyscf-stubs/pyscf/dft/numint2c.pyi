from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.dft import numint as numint, xc_deriv as xc_deriv
from pyscf.dft.numint import NumInt, BLKSIZE as BLKSIZE
from numpy import float64, ndarray
from pyscf.dft.gen_grid import Grids
from pyscf.dft.r_numint import RNumInt
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.numint2c import KNumInt2C, NumInt2C
from pyscf.pbc.gto.cell import Cell
from typing import List, Optional, Tuple, Union

def eval_rho(mol: Union[Cell, Mole], ao: ndarray, dm: ndarray, non0tab: Optional[ndarray]=None, xctype: str = 'LDA', hermi: int = 0, with_lapl: bool = True, verbose: None=None) -> ndarray: ...
def mcfun_eval_xc_adapter(ni, xc_code): ...

class NumInt2C(lib.StreamObject, numint.LibXCMixin):
    collinear: Incomplete
    spin_samples: Incomplete
    collinear_thrd: Incomplete
    collinear_samples: Incomplete
    make_mask: Incomplete
    eval_ao: Incomplete
    eval_rho: Incomplete
    def eval_rho1(self, mol, ao, dm, screen_index=None, xctype: str = 'LDA', hermi: int = 0, with_lapl: bool = True, cutoff=None, ao_cutoff=None, pair_mask=None, verbose=None): ...
    def eval_rho2(self, mol: Mole, ao: ndarray, mo_coeff: ndarray, mo_occ: ndarray, non0tab: None=None, xctype: str = 'LDA', with_lapl: bool = True, verbose: None=None) -> ndarray: ...
    def cache_xc_kernel(self, mol, grids, xc_code, mo_coeff, mo_occ, spin: int = 0, max_memory: int = 2000): ...
    def cache_xc_kernel1(self, mol, grids, xc_code, dm, spin: int = 0, max_memory: int = 2000): ...
    def get_rho(self, mol: Mole, dm: ndarray, grids: Grids, max_memory: int = 2000) -> ndarray: ...
    def nr_vxc(self, mol: Mole, grids: Grids, xc_code: str, dms: Union[ndarray, NPArrayWithTag], spin: int = 0, relativity: int = 0, hermi: int = 1, max_memory: Union[float, int] = 2000, verbose: None=None) -> Union[Tuple[float64, float64, NPArrayWithTag], Tuple[float64, float64, ndarray]]: ...
    get_vxc = nr_vxc
    nr_gks_vxc = nr_vxc
    def nr_nlc_vxc(self, mol: Mole, grids: Grids, xc_code: str, dm: ndarray, spin: int = 0, relativity: int = 0, hermi: int = 1, max_memory: float = 2000, verbose: None=None) -> Tuple[float64, float64, ndarray]: ...
    def nr_fxc(self, mol: Mole, grids: Grids, xc_code: str, dm0: ndarray, dms: ndarray, spin: int = 0, relativity: int = 0, hermi: int = 0, rho0: None=None, vxc: None=None, fxc: None=None, max_memory: int = 2000, verbose: None=None) -> ndarray: ...
    get_fxc = nr_fxc
    nr_gks_fxc = nr_fxc
    eval_xc_eff: Incomplete
    mcfun_eval_xc_adapter = mcfun_eval_xc_adapter
    block_loop: Incomplete
    def to_gpu(self): ...

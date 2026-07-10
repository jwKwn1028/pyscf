from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.dft import numint as numint, numint2c as numint2c
from pyscf.pbc.lib.kpts import KPoints as KPoints

class NumInt2C(lib.StreamObject, numint.LibXCMixin):
    collinear: Incomplete
    spin_samples: Incomplete
    collinear_thrd: Incomplete
    collinear_samples: Incomplete
    make_mask: Incomplete
    eval_ao: Incomplete
    eval_rho: Incomplete
    eval_rho2: Incomplete
    def eval_rho1(self, cell, ao, dm, screen_index=None, xctype: str = 'LDA', hermi: int = 0, with_lapl: bool = True, cutoff=None, ao_cutoff=None, pair_mask=None, verbose=None): ...
    def cache_xc_kernel(self, cell, grids, xc_code, mo_coeff, mo_occ, spin: int = 0, kpt=None, max_memory: int = 2000): ...
    def cache_xc_kernel1(self, cell, grids, xc_code, dm, spin: int = 0, kpt=None, max_memory: int = 2000): ...
    def get_rho(self, cell, dm, grids, kpt=..., max_memory: int = 2000): ...
    def nr_vxc(self, cell, grids, xc_code, dms, spin: int = 0, relativity: int = 0, hermi: int = 1, kpt=None, kpts_band=None, max_memory: int = 2000, verbose=None): ...
    get_vxc = nr_vxc
    nr_gks_vxc = nr_vxc
    def nr_fxc(self, cell, grids, xc_code, dm0, dms, spin: int = 0, relativity: int = 0, hermi: int = 0, rho0=None, vxc=None, fxc=None, kpt=None, max_memory: int = 2000, verbose=None): ...
    get_fxc = nr_fxc
    nr_gks_fxc = nr_fxc
    eval_xc_eff: Incomplete
    mcfun_eval_xc_adapter = numint2c.mcfun_eval_xc_adapter
    block_loop: Incomplete

class KNumInt2C(lib.StreamObject, numint.LibXCMixin):
    kpts: Incomplete
    def __init__(self, kpts=...) -> None: ...
    collinear: Incomplete
    spin_samples: Incomplete
    collinear_thrd: Incomplete
    collinear_samples: Incomplete
    make_mask: Incomplete
    eval_ao: Incomplete
    def reset(self, cell=None): ...
    def eval_rho(self, cell, ao_kpts, dm_kpts, non0tab=None, xctype: str = 'LDA', hermi: int = 0, with_lapl: bool = True, verbose=None): ...
    def eval_rho1(self, cell, ao_kpts, dm_kpts, screen_index=None, xctype: str = 'LDA', hermi: int = 0, with_lapl: bool = True, cutoff=None, ao_cutoff=None, pair_mask=None, verbose=None): ...
    def eval_rho2(self, cell, ao_kpts, mo_coeff_kpts, mo_occ_kpts, non0tab=None, xctype: str = 'LDA', with_lapl: bool = True, verbose=None): ...
    def cache_xc_kernel(self, cell, grids, xc_code, mo_coeff_kpts, mo_occ_kpts, spin: int = 0, kpts=None, max_memory: int = 2000): ...
    def cache_xc_kernel1(self, cell, grids, xc_code, dm_kpts, spin: int = 0, kpts=None, max_memory: int = 2000): ...
    def get_rho(self, cell, dm, grids, kpts=..., max_memory: int = 2000): ...
    def nr_vxc(self, cell, grids, xc_code, dms, spin: int = 0, relativity: int = 0, hermi: int = 1, kpts=None, kpts_band=None, max_memory: int = 2000, verbose=None): ...
    get_vxc = nr_vxc
    nr_gks_vxc = nr_vxc
    get_fxc: Incomplete
    nr_gks_fxc: Incomplete
    nr_fxc: Incomplete
    eval_xc_eff: Incomplete
    mcfun_eval_xc_adapter = numint2c.mcfun_eval_xc_adapter
    block_loop: Incomplete

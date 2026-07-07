import pyscf.scf.ghf as mol_ghf
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.scf import addons as addons, hf as pbchf

def get_jk(mf, cell=None, dm=None, hermi: int = 0, kpt=None, kpts_band=None, with_j: bool = True, with_k: bool = True, **kwargs): ...

class GHF(pbchf.SCF):
    with_soc: Incomplete
    def __init__(self, cell, kpt=None, exxdiv=...) -> None: ...
    init_guess_by_chkfile: Incomplete
    init_guess_by_minao: Incomplete
    init_guess_by_atom: Incomplete
    init_guess_by_huckel: Incomplete
    get_jk = get_jk
    get_occ = mol_ghf.get_occ
    get_grad: Incomplete
    analyze: Incomplete
    mulliken_pop: Incomplete
    mulliken_meta: Incomplete
    spin_square: Incomplete
    stability: Incomplete
    gen_response = NotImplemented
    def get_hcore(self, cell=None, kpt=None): ...
    def get_ovlp(self, cell=None, kpt=None): ...
    def get_veff(self, cell=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpt=None, kpts_band=None): ...
    def get_bands(self, kpts_band, cell=None, dm=None, kpt=None) -> None: ...
    def x2c1e(self): ...
    x2c = x2c1e
    sfx2c1e = x2c1e
    def to_ks(self, xc: str = 'HF'): ...
    def convert_from_(self, mf): ...
    to_gpu = lib.to_gpu

from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.gto import mole as mole
from pyscf.lib import logger as logger
from pyscf.pbc import tools as tools
from pyscf.pbc.df import aft as aft, aft_jk as aft_jk, ft_ao as ft_ao, gdf_builder as gdf_builder
from pyscf.pbc.lib.kpts_helper import is_zero as is_zero
from pyscf.pbc.scf import ghf as ghf, kghf as kghf, khf as khf
from pyscf.x2c import x2c as x2c

def sfx2c1e(mf): ...
sfx2c = sfx2c1e

class SFX2C1E_SCF(x2c._X2C_SCF):
    __name_mixin__: str
    with_x2c: Incomplete
    def __init__(self, mf) -> None: ...
    def get_hcore(self, cell=None, kpts=None, kpt=None): ...

class PBCX2CHelper(x2c.X2C):
    exp_drop: Incomplete
    approx: Incomplete
    xuncontract: Incomplete
    basis: Incomplete
    cell: Incomplete
    def __init__(self, cell, kpts=None) -> None: ...
    def reset(self, cell=None): ...

class SpinFreeX2CHelper(PBCX2CHelper):
    def get_hcore(self, cell=None, kpts=None): ...
    def get_xmat(self, cell=None, kpts=None): ...
    def dump_flags(self, verbose=None): ...

def get_pnucp(mydf, kpts=None): ...

from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.gto import mole as mole
from pyscf.lib import logger as logger
from pyscf.pbc import tools as tools
from pyscf.pbc.df import aft as aft, aft_jk as aft_jk, ft_ao as ft_ao, gdf_builder as gdf_builder
from pyscf.pbc.lib.kpts_helper import is_zero as is_zero
from pyscf.pbc.scf import ghf as ghf, kghf as kghf, khf as khf
from pyscf.pbc.x2c import sfx2c1e as sfx2c1e
from pyscf.x2c import x2c as x2c

def x2c1e_gscf(mf): ...

class X2C1E_GSCF(x2c._X2C_SCF):
    __name_mixin__: str
    with_x2c: Incomplete
    def __init__(self, mf) -> None: ...
    def get_hcore(self, cell=None, kpts=None, kpt=None): ...

class SpinOrbitalX2C1EHelper(sfx2c1e.PBCX2CHelper):
    def get_hcore(self, cell=None, kpts=None): ...
    def dump_flags(self, verbose=None): ...

def get_1c_pvxp(cell, kpts=None): ...
def get_pbc_pvxp(mydf, kpts=None): ...

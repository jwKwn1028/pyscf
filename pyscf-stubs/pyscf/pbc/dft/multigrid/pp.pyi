from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc import tools as tools
from pyscf.pbc.df import fft as fft
from pyscf.pbc.gto import pseudo as pseudo
from pyscf.pbc.gto.pseudo import pp_int as pp_int
from pyscf.pbc.lib.kpts import KPoints as KPoints
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point

PP_WITH_RHO_CORE: Incomplete

def make_rho_core(cell, mesh=None, precision=None, atm_id=None): ...
def get_pp_loc_part1_gs(cell, Gv): ...
def get_vpploc_part1_ip1(mydf, kpts=...): ...
def vpploc_part1_nuc_grad(mydf, dm, kpts=..., atm_id=None, precision=None): ...
def fake_cell_vloc_part1(cell, atm_id=None, precision=None): ...

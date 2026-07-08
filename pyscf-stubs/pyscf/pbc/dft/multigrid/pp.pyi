from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc import tools as tools
from pyscf.pbc.df import fft as fft
from pyscf.pbc.gto import pseudo as pseudo
from pyscf.pbc.gto.pseudo import pp_int as pp_int
from pyscf.pbc.lib.kpts import KPoints as KPoints
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point
from numpy import float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.multigrid.multigrid_pair import MultiGridNumInt
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Tuple, Union

PP_WITH_RHO_CORE: Incomplete

def make_rho_core(cell: Cell, mesh: None=None, precision: None=None, atm_id: None=None) -> ndarray: ...
def get_pp_loc_part1_gs(cell, Gv): ...
def get_vpploc_part1_ip1(mydf, kpts=...): ...
def vpploc_part1_nuc_grad(mydf: MultiGridNumInt, dm: Union[ndarray, NPArrayWithTag], kpts: ndarray=..., atm_id: None=None, precision: None=None) -> ndarray: ...
def fake_cell_vloc_part1(cell: Cell, atm_id: None=None, precision: None=None) -> Union[Tuple[Cell, float64], Tuple[Cell, int]]: ...

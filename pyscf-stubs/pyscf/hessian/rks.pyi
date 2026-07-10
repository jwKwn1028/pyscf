from _typeshed import Incomplete
from pyscf import dft as dft, gto as gto, lib as lib
from pyscf.dft import gen_grid as gen_grid, numint as numint
from pyscf.grad import rks as rks
from pyscf.hessian import rhf as rhf_hess
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.dft.gen_grid import Grids
from pyscf.dft.rks import RKS
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from typing import List, Optional, Union

min_grid_blksize: Incomplete
NLC_REMOVE_ZERO_RHO_GRID_THRESHOLD: float
libdft: Incomplete
contract: Incomplete

def partial_hess_elec(hessobj: "Hessian", mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, atmlst: Optional[Union[range, List[int]]]=None, max_memory: int = 4000, verbose: Optional[Logger]=None) -> ndarray: ...
def make_h1(hessobj: "Hessian", mo_coeff: ndarray, mo_occ: ndarray, chkfile: None=None, atmlst: Optional[Union[range, List[int]]]=None, verbose: Optional[Logger]=None) -> ndarray: ...

XX: Incomplete
XY: Incomplete
XZ: Incomplete
YX: Incomplete
YY: Incomplete
YZ: Incomplete
ZX: Incomplete
ZY: Incomplete
ZZ: Incomplete
XXX: Incomplete
XXY: Incomplete
XXZ: Incomplete
XYY: Incomplete
XYZ: Incomplete
XZZ: Incomplete
YYY: Incomplete
YYZ: Incomplete
YZZ: Incomplete
ZZZ: Incomplete

def get_d2mu_dr2(ao): ...
def get_d3mu_dr3(ao): ...
def get_d2rho_dAdr_orbital_response(d2mu_dr2, dmu_dr, mu, dm0, aoslices): ...
def get_d2rho_dAdr_grid_response(d2mu_dr2, dmu_dr, mu, dm0, atom_to_grid_index_map=None, i_atom=None): ...
def get_drhodA_dgammadA_orbital_response(d2mu_dr2, dmu_dr, mu, drho_dr, dm0, aoslices): ...
def get_drhodA_dgammadA_grid_response(d2mu_dr2, dmu_dr, mu, drho_dr, dm0, atom_to_grid_index_map=None, i_atom=None): ...
def get_d2rhodAdB_d2gammadAdB(mol, grids_coords, dm0): ...
def contract_d2rhodAdB_d2gammadAdB(d3mu_dr3, d2mu_dr2, dmu_dr, mu, drho_dr, dm0, aoslices, fw_rho, fw_gamma): ...
def get_dweight_dA(mol, grids): ...
def get_vnlc_resp(mf, mol, mo_coeff, mo_occ, dm1s, max_memory): ...

class Hessian(rhf_hess.HessianBase):
    grids: Incomplete
    grid_response: bool
    def __init__(self, mf: RKS) -> None: ...
    partial_hess_elec = partial_hess_elec
    hess_elec = rhf_hess.hess_elec
    make_h1 = make_h1

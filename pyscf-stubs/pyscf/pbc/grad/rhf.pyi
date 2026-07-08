from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.grad import rhf as mol_rhf
from pyscf.lib import logger as logger
from pyscf.pbc.dft.multigrid import MultiGridNumInt2 as MultiGridNumInt2
from pyscf.pbc.gto.pseudo import pp_int as pp_int
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Union

SCREEN_VHF_DM_CONTRA: Incomplete
libpbc: Incomplete

def grad_elec(mf_grad: Incomplete, mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, atmlst: None=None, kpt: ndarray=...) -> ndarray: ...
def get_ovlp(cell: Cell, kpt: ndarray=...) -> ndarray: ...
def get_veff(mf_grad: Incomplete, mol: Cell, dm: NPArrayWithTag, kpt: ndarray=...) -> ndarray: ...
def grad_nuc(cell: Cell, atmlst: None=None, ew_eta: None=None, ew_cut: None=None) -> ndarray: ...

class GradientsBase(mol_rhf.GradientsBase):
    def grad_nuc(self, mol: None=None, atmlst: None=None) -> ndarray: ...
    def get_ovlp(self, mol: Optional[Cell]=None, kpt: ndarray=...) -> ndarray: ...
    def optimizer(self, solver: str = 'ase'): ...

class Gradients(GradientsBase):
    def get_veff(self, mol: Optional[Cell]=None, dm: Optional[NPArrayWithTag]=None, kpt: ndarray=...) -> ndarray: ...
    make_rdm1e: Incomplete
    grad_elec = grad_elec

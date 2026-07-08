from _typeshed import Incomplete
from pyscf import __config__ as __config__
from pyscf.lib import logger as logger
from pyscf.pbc.dft.multigrid import MultiGridNumInt2 as MultiGridNumInt2
from pyscf.pbc.grad import rhf as rhf_grad
from pyscf.pbc.gto.pseudo import pp_int as pp_int
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.grad.uks import Gradients
from pyscf.pbc.gto.cell import Cell
from typing import Optional

def grad_elec(mf_grad: "Gradients", mo_energy: Optional[ndarray]=None, mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, atmlst: None=None, kpt: ndarray=...) -> ndarray: ...
def get_veff(mf_grad: "Gradients", mol: Cell, dm: NPArrayWithTag, kpt: ndarray=...) -> ndarray: ...

class Gradients(rhf_grad.GradientsBase):
    def get_veff(self, mol: Optional[Cell]=None, dm: Optional[NPArrayWithTag]=None, kpt: ndarray=...) -> ndarray: ...
    make_rdm1e: Incomplete
    grad_elec = grad_elec

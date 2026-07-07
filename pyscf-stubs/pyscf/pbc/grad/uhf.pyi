from _typeshed import Incomplete
from pyscf import __config__ as __config__
from pyscf.lib import logger as logger
from pyscf.pbc.dft.multigrid import MultiGridNumInt2 as MultiGridNumInt2
from pyscf.pbc.grad import rhf as rhf_grad
from pyscf.pbc.gto.pseudo import pp_int as pp_int
from pyscf.pbc.lib.kpts_helper import gamma_point as gamma_point

def grad_elec(mf_grad, mo_energy=None, mo_coeff=None, mo_occ=None, atmlst=None, kpt=...): ...
def get_veff(mf_grad, mol, dm, kpt=...): ...

class Gradients(rhf_grad.GradientsBase):
    def get_veff(self, mol=None, dm=None, kpt=...): ...
    make_rdm1e: Incomplete
    grad_elec = grad_elec

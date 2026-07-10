from _typeshed import Incomplete
from pyscf.lib import logger as logger
from pyscf.pbc import gto as gto
from pyscf.pbc.grad import krhf as krhf_grad
from pyscf.pbc.gto.pseudo import pp_int as pp_int

def grad_elec(mf_grad, mo_energy=None, mo_coeff=None, mo_occ=None, atmlst=None): ...
def get_veff(mf_grad, dm, kpts): ...
def make_rdm1e(mo_energy, mo_coeff, mo_occ): ...

class Gradients(krhf_grad.GradientsBase):
    def get_veff(self, dm=None, kpts=None): ...
    def make_rdm1e(self, mo_energy=None, mo_coeff=None, mo_occ=None): ...
    grad_elec = grad_elec
    extra_force: Incomplete
    as_scanner: Incomplete
    kernel: Incomplete

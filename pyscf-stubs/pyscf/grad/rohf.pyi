from pyscf import lib as lib, scf as scf
from pyscf.grad import rhf as rhf_grad, uhf as uhf_grad

def make_rdm1e(mf_grad, mo_energy, mo_coeff, mo_occ): ...

class Gradients(rhf_grad.Gradients):
    get_veff = uhf_grad.get_veff
    make_rdm1e = make_rdm1e
    grad_elec = uhf_grad.grad_elec
Grad = Gradients

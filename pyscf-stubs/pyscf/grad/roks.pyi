from pyscf import dft as dft, lib as lib
from pyscf.grad import rks as rks_grad, rohf as rohf_grad, uhf as uhf_grad, uks as uks_grad
from pyscf.scf import addons as addons

class Gradients(rks_grad.Gradients):
    get_veff = uks_grad.get_veff
    make_rdm1e = rohf_grad.make_rdm1e
    grad_elec = uhf_grad.grad_elec
Grad = Gradients

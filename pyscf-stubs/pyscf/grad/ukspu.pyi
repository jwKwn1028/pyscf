from pyscf import lib as lib
from pyscf.dft.rkspu import reference_mol as reference_mol
from pyscf.dft.ukspu import UKSpU as UKSpU
from pyscf.grad import uks as uks_grad
from pyscf.grad.rkspu import generate_first_order_local_orbitals as generate_first_order_local_orbitals

class Gradients(uks_grad.Gradients):
    def get_veff(self, mol=None, dm=None): ...
    def extra_force(self, atom_id, envs): ...

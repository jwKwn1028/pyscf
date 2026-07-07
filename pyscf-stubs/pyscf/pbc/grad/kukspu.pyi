from pyscf import lib as lib
from pyscf.pbc.dft.krkspu import reference_mol as reference_mol
from pyscf.pbc.grad import kuks as kuks_grad
from pyscf.pbc.grad.krkspu import generate_first_order_local_orbitals as generate_first_order_local_orbitals

class Gradients(kuks_grad.Gradients):
    def get_veff(self, dm=None, kpts=None): ...
    def extra_force(self, atom_id, envs): ...

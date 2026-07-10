from pyscf import lib as lib
from pyscf.pbc import gto as gto
from pyscf.pbc.dft.krkspu import reference_mol as reference_mol
from pyscf.pbc.grad import krks as krks_grad

def generate_first_order_local_orbitals(cell, minao_ref: str = 'MINAO', kpts=None): ...

class Gradients(krks_grad.Gradients):
    def get_veff(self, dm=None, kpts=None): ...
    def extra_force(self, atom_id, envs): ...

from pyscf import lib as lib
from pyscf.pbc import gto as gto
from pyscf.pbc.dft.krkspu import KRKSpU, reference_mol as reference_mol
from pyscf.pbc.grad import krks as krks_grad
from numpy import ndarray
from pyscf.pbc.gto.cell import Cell
from typing import Callable, Optional, Union

def generate_first_order_local_orbitals(cell: Cell, minao_ref: Union[Cell, str] = 'MINAO', kpts: Optional[ndarray]=None) -> Callable: ...

class Gradients(krks_grad.Gradients):
    def get_veff(self, dm=None, kpts=None): ...
    def extra_force(self, atom_id, envs): ...

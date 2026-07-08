from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.grad import uks as uks_grad
from pyscf.lib import logger as logger
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Optional

def get_veff(ks_grad: "Gradients", mol: Optional[Mole]=None, dm: Optional[NPArrayWithTag]=None) -> NPArrayWithTag: ...

class Gradients(uks_grad.Gradients):
    def __init__(self, mf) -> None: ...
    auxbasis_response: bool
    get_jk: Incomplete
    get_j: Incomplete
    get_k: Incomplete
    get_veff = get_veff
    def extra_force(self, atom_id, envs): ...
Grad = Gradients

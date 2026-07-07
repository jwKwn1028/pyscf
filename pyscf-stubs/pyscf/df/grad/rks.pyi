from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.grad import rks as rks_grad
from pyscf.lib import logger as logger

def get_veff(ks_grad, mol=None, dm=None): ...

class Gradients(rks_grad.Gradients):
    def __init__(self, mf) -> None: ...
    auxbasis_response: bool
    get_jk: Incomplete
    get_j: Incomplete
    get_k: Incomplete
    get_veff = get_veff
    def extra_force(self, atom_id, envs): ...
Grad = Gradients

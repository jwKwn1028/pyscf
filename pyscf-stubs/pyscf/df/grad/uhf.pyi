from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.grad import uhf as uhf_grad
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Optional, Union

class Gradients(uhf_grad.Gradients):
    def __init__(self, mf) -> None: ...
    auxbasis_response: bool
    get_jk: Incomplete
    get_j: Incomplete
    get_k: Incomplete
    def get_veff(self, mol: Optional[Mole]=None, dm: Optional[NPArrayWithTag]=None) -> Union[ndarray, NPArrayWithTag]: ...
    def extra_force(self, atom_id, envs): ...
Grad = Gradients

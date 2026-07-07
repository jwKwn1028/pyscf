from pyscf import lib as lib
from pyscf.dft import numint as numint
from pyscf.grad import tdrhf as tdrhf_grad
from pyscf.lib import logger as logger
from pyscf.scf import ucphf as ucphf

def grad_elec(td_grad, x_y, atmlst=None, max_memory: int = 2000, verbose=...): ...

class Gradients(tdrhf_grad.Gradients):
    def grad_elec(self, xy, singlet=None, atmlst=None): ...
Grad = Gradients

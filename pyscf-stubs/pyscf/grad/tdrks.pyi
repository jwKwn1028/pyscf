from pyscf import lib as lib
from pyscf.dft import numint as numint, rks as rks
from pyscf.grad import tdrhf as tdrhf
from pyscf.lib import logger as logger
from pyscf.scf import cphf as cphf

def grad_elec(td_grad, x_y, singlet: bool = True, atmlst=None, max_memory: int = 2000, verbose=...): ...

class Gradients(tdrhf.Gradients):
    def grad_elec(self, xy, singlet, atmlst=None): ...
Grad = Gradients

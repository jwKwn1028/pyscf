from pyscf import lib as lib
from pyscf.grad import mp2 as mp2_grad
from pyscf.grad.mp2 import has_frozen_orbitals as has_frozen_orbitals
from pyscf.lib import logger as logger
from pyscf.mp import ump2 as ump2
from pyscf.scf import ucphf as ucphf

def grad_elec(mp_grad, t2, atmlst=None, verbose=...): ...

class Gradients(mp2_grad.Gradients):
    grad_elec = grad_elec
Grad = Gradients

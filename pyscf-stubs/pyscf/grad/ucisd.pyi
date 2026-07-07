from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.ci import ucisd as ucisd
from pyscf.grad import cisd as cisd_grad
from pyscf.lib import logger as logger

def grad_elec(cigrad, civec=None, eris=None, atmlst=None, verbose=...): ...

class Gradients(cisd_grad.Gradients):
    grad_elec = grad_elec
Grad = Gradients

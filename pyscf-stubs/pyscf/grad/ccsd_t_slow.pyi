from pyscf import lib as lib
from pyscf.grad import ccsd as ccsd_grad

def grad_elec(cc_grad, t1=None, t2=None, l1=None, l2=None, eris=None, atmlst=None, verbose=...): ...

class Gradients(ccsd_grad.Gradients):
    grad_elec = grad_elec

from pyscf import lib as lib
from pyscf.cc import uccsd_t_rdm as uccsd_t_rdm
from pyscf.grad import uccsd as uccsd_grad

def grad_elec(cc_grad, t1=None, t2=None, l1=None, l2=None, eris=None, atmlst=None, verbose=...): ...

class Gradients(uccsd_grad.Gradients):
    grad_elec = grad_elec

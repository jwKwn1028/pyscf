from pyscf import lib as lib
from pyscf.cc import ccsd as ccsd, uccsd as uccsd, uccsd_rdm as uccsd_rdm
from pyscf.grad import ccsd as ccsd_grad
from pyscf.grad.mp2 import has_frozen_orbitals as has_frozen_orbitals
from pyscf.lib import logger as logger
from pyscf.scf import ucphf as ucphf

def grad_elec(cc_grad, t1=None, t2=None, l1=None, l2=None, eris=None, atmlst=None, d1=None, d2=None, verbose=...): ...

class Gradients(ccsd_grad.Gradients):
    grad_elec = grad_elec
Grad = Gradients

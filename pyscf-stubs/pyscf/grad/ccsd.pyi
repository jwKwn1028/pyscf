from _typeshed import Incomplete
from pyscf import gto as gto, lib as lib
from pyscf.cc import ccsd as ccsd, ccsd_rdm as ccsd_rdm
from pyscf.grad import rhf as rhf_grad
from pyscf.grad.mp2 import has_frozen_orbitals as has_frozen_orbitals
from pyscf.lib import logger as logger
from pyscf.scf import cphf as cphf

def grad_elec(cc_grad, t1=None, t2=None, l1=None, l2=None, eris=None, atmlst=None, d1=None, d2=None, verbose=...): ...
def as_scanner(grad_cc): ...

class CCSD_GradScanner(lib.GradScanner):
    def __init__(self, g) -> None: ...
    def __call__(self, mol_or_geom, **kwargs): ...
    @property
    def converged(self): ...

class Gradients(rhf_grad.GradientsBase):
    grad_elec = grad_elec
    atmlst: Incomplete
    de: Incomplete
    def kernel(self, t1=None, t2=None, l1=None, l2=None, eris=None, atmlst=None, verbose=None): ...
    def grad_nuc(self, mol=None, atmlst=None): ...
    as_scanner = as_scanner
    to_gpu = lib.to_gpu
Grad = Gradients

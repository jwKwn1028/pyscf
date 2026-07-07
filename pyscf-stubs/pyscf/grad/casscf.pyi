from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, gto as gto, lib as lib, mcscf as mcscf
from pyscf.grad import casci as casci_grad
from pyscf.lib import logger as logger
from pyscf.mcscf.addons import StateAverageMCSCFSolver as StateAverageMCSCFSolver

def grad_elec(mc_grad, mo_coeff=None, ci=None, atmlst=None, verbose=None): ...
def as_scanner(mcscf_grad): ...

class CASSCF_GradScanner(lib.GradScanner):
    def __init__(self, g) -> None: ...
    def __call__(self, mol_or_geom, **kwargs): ...

class Gradients(casci_grad.Gradients):
    grad_elec = grad_elec
    atmlst: Incomplete
    de: Incomplete
    def kernel(self, mo_coeff=None, ci=None, atmlst=None, verbose=None): ...
    as_scanner = as_scanner
    to_gpu = lib.to_gpu
Grad = Gradients

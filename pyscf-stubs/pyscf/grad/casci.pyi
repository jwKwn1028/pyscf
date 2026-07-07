from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, gto as gto, lib as lib, mcscf as mcscf
from pyscf.grad import rhf as rhf_grad
from pyscf.lib import logger as logger
from pyscf.mcscf.addons import StateAverageMCSCFSolver as StateAverageMCSCFSolver
from pyscf.scf import cphf as cphf

RANGE_TYPE = range

def grad_elec(mc_grad, mo_coeff=None, ci=None, atmlst=None, verbose=None): ...
def as_scanner(mcscf_grad, state=None): ...

class CASCI_GradScanner(lib.GradScanner):
    state: Incomplete
    def __init__(self, g, state) -> None: ...
    def __call__(self, mol_or_geom, state=None, **kwargs): ...

class Gradients(rhf_grad.GradientsBase):
    state: Incomplete
    def __init__(self, mc) -> None: ...
    def dump_flags(self, verbose=None): ...
    grad_elec = grad_elec
    atmlst: Incomplete
    de: Incomplete
    def kernel(self, mo_coeff=None, ci=None, atmlst=None, state=None, verbose=None): ...
    def hcore_generator(self, mol=None): ...
    def grad_nuc(self, mol=None, atmlst=None): ...
    as_scanner = as_scanner
    to_gpu = lib.to_gpu
Grad = Gradients

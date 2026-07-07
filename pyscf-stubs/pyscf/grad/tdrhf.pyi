from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, lib as lib
from pyscf.grad import rhf as rhf_grad
from pyscf.lib import logger as logger
from pyscf.scf import cphf as cphf

def grad_elec(td_grad, x_y, singlet: bool = True, atmlst=None, max_memory: int = 2000, verbose=...): ...
def as_scanner(td_grad, state: int = 1): ...

class TDSCF_GradScanner(lib.GradScanner):
    state: Incomplete
    def __init__(self, g, state) -> None: ...
    def __call__(self, mol_or_geom, state=None, **kwargs): ...
    @property
    def converged(self): ...

class Gradients(rhf_grad.GradientsBase):
    cphf_max_cycle: Incomplete
    cphf_conv_tol: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    mol: Incomplete
    base: Incomplete
    chkfile: Incomplete
    max_memory: Incomplete
    state: int
    atmlst: Incomplete
    de: Incomplete
    def __init__(self, td) -> None: ...
    def dump_flags(self, verbose=None): ...
    def grad_elec(self, xy, singlet, atmlst=None): ...
    def kernel(self, xy=None, state=None, singlet=None, atmlst=None): ...
    def grad_nuc(self, mol=None, atmlst=None): ...
    as_scanner = as_scanner
    to_gpu = lib.to_gpu
Grad = Gradients

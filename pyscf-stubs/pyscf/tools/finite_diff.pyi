from _typeshed import Incomplete
from pyscf import gto as gto, lib as lib
from pyscf.grad.rhf import GradientsBase as GradientsBase
from pyscf.hessian.rhf import HessianBase as HessianBase
from pyscf.lib import logger as logger

def kernel(method, displacement: float = 0.01): ...

class Gradients(GradientsBase):
    displacement: float
    base: Incomplete
    mol: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    de: Incomplete
    def __init__(self, method) -> None: ...
    def kernel(self): ...
    def as_scanner(self): ...

class GradScanner(lib.GradScanner):
    def __call__(self, mol_or_geom, **kwargs): ...

class Hessian(HessianBase):
    displacement: float
    base: Incomplete
    mol: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    de: Incomplete
    def __init__(self, method) -> None: ...
    def kernel(self): ...
    def as_scanner(self): ...

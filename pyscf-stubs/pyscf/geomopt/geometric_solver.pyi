import geometric
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.geomopt.addons import as_pyscf_method as as_pyscf_method, dump_mol_geometry as dump_mol_geometry, symmetrize as symmetrize
from pyscf.grad.rhf import GradientsBase as GradientsBase
from pyscf.lib import logger as logger

msg: str
INCLUDE_GHOST: Incomplete
ASSERT_CONV: Incomplete

class PySCFEngine(geometric.engine.Engine):
    mol: Incomplete
    scanner: Incomplete
    cycle: int
    e_last: int
    callback: Incomplete
    assert_convergence: bool
    def __init__(self, scanner) -> None: ...
    def calc_new(self, coords, dirname): ...

def kernel(method, assert_convergence=..., include_ghost=..., constraints=None, callback=None, maxsteps: int = 100, **kwargs): ...

class GeometryOptimizer(lib.StreamObject):
    method: Incomplete
    callback: Incomplete
    params: Incomplete
    converged: bool
    max_cycle: int
    def __init__(self, method) -> None: ...
    @property
    def mol(self): ...
    @mol.setter
    def mol(self, x) -> None: ...
    def kernel(self, params=None): ...
    optimize = kernel

class NotConvergedError(RuntimeError): ...
